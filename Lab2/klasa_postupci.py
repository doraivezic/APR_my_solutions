from klasa_funkcije import Funkcija
import math
import numpy as np

class Postupak:

    def __init__(self, f):
        self.f = f
        self.minimum = None

    def Resetiraj(self):
        self.minimum = None

    def __del__(self):
        return




    def Unimodalni_interval(self, tocka, f, h=1.0):

        l = tocka - h
        r = tocka + h
        m = tocka
        step = 1

        #f = self.f.Racunaj_vrijednost_fje
        
        fm = f(tocka)
        fl = f(l)
        fr = f(r)

        if fm < fr and fm < fl :
            return l,r
        elif fm > fr:
            while True :
                l = m
                m = r
                fm = fr   
                step *= 2             
                r = tocka + h * step
                fr = f(r)
                if fm <= fr:
                    break
        else:
            while True:
                r = m
                m = l
                fm = fl
                step *= 2
                l = tocka - h * step
                fl = f(l)
                if fm <= fl:
                    break

        return l,r


    def Zlatni_rez(self, a=None, f=None, b=None, e=10**(-6), file=None, ispis_tocaka=False):

        # pokretanje s predefiniranim intervalom
        if file!=None:
            o = open(file, "r")
            lines = o.readlines()
            o.close()
            a = np.array(list(map(float, lines[0].rstrip().split())))
            b = np.array(list(map(float, lines[1].rstrip().split())))
            e = float(lines[2].rstrip().split()[0])
            
        #pokretanje s pocetnom tockom s pomocu koje se određuje unimodalni interval
        elif b is None:
            a,b = self.Unimodalni_interval(a, f)

        k = 0.5 * (math.sqrt(5) - 1) #zlatni rez

        c = b - k * abs(b - a)
        d = a + k * abs(b - a)

        #f = self.f.Racunaj_vrijednost_fje

        fc = f(c)
        fd = f(d)

        while (b - a) > e :

            if ispis_tocaka:
                print(a,c,d,b)
                print(f(a),fc,fd,f(b))

            if fc < fd :
                b = d
                d = c
                c = b - k * abs(b - a)
                fd = fc
                fc = f(c)
            else:
                a = c
                c = d
                d = a + k * abs(b - a)
                fc = fd
                fd = f(d)

        self.minimum = (a + b)/2  # ili nove vrijednosti a i b
        return (a + b)/2






    def Trazenje_po_koord_osima(self, x, f, e=10**(-6), file=None):

        if file!=None:
            o = open(file, "r")
            lines = o.readlines()
            o.close()
            e = np.array(lines[0].rstrip().split())
            x = np.array(lines[1].rstrip().split())
        
        I = np.eye(len(x))  #jedinicna matrica dimenzije kao i x; sastoji se od e1,e2,..
        
        def f_zl_rez(l):
            return f(np.array(x) + l * I[i])

        while True:
            xs = np.copy(x)
            #trazenje minimuma po svim koordinatnim smjerovima
            for i in range(len(x)):
                lmin = self.Zlatni_rez(x[i], f_zl_rez)
                #x = x + lmin*I[i] to jest:
                x[i] += lmin

            if (abs(x-xs)).max() <= e:
                break

        self.minimum = x
        return






    def Hooke_Jevees(self, x0, f, dx=0.5, e=10**(-6), file=None, ispis=False):

        if file!=None:
            o = open(file, "r")
            lines = o.readlines()
            o.close()
            dx = np.array(list(map(float, lines[0].rstrip().split())))   #list(map(int, ['1','2','3']))
            e = float(lines[1].rstrip().split()[0])
            x0 = np.array(list(map(float, lines[2].rstrip().split())))
        
        xP = np.copy(x0)
        xB = np.copy(x0)

        def istrazi(xP, dx):
            x = np.copy(xP)
            #za svaku koordinatu gledamo je li bolje pomknuti se za +dx, za -dx ili ne pomaknuti se
            for i in range(len(x)):
                P = f(x)  #pocetni f(x)
                x[i] += dx
                N = f(x)
                if N>P:
                    x[i] -= 2*dx
                    N = f(x)
                    if N>P:
                        x[i] += dx
            return x

        while dx > e:

            xN = istrazi(xP, dx)

            if ispis:
                print(xB,xP,xN)

            if f(xN)<f(xB):   #ako je novi pomak bolji od starog (ili pocetnog)
                xP = 2*xN - xB
                xB = np.copy(xN)
            else:
                dx/=2  #smanjujemo dx
                xP = np.copy(xB)
             
        self.minimum = xB
        return






    def Simpleks(self, x0, f, pomak=1, e=10**(-6), alfa=1, beta=0.5, gamma=2, sigma=0.5, file=None, ispis=False):

        if file!=None:
            o = open(file, "r")
            lines = o.readlines()
            o.close()
            x0 = np.array(list(map(float, lines[0].rstrip().split())))   #list(map(int, ['1','2','3']))
            e = float(lines[1].rstrip().split()[0])
            pomak = np.array(list(map(float, lines[2].rstrip().split())))
            alfa = np.array(list(map(float, lines[3].rstrip().split())))
            beta = np.array(list(map(float, lines[4].rstrip().split())))
            gamma = np.array(list(map(float, lines[5].rstrip().split())))
            sigma = np.array(list(map(float, lines[6].rstrip().split())))

        #izracunaj tocke simpleksa X[i], i = 0..n; -> za jednu novu tocku pomaknemo se za neki pomak u svakoj dimenziji (i pocetna tocka ostane ista)
        X = []
        X.append(x0.copy())
        for i in range(len(x0)):
            tmp = np.copy(x0).tolist()
            tmp[i] += pomak
            X.append(tmp)
        X = np.array(X)


        def Odredi_indekse_h_l():
            fX=[]
            for i in range(len(X)):
                fX.append(f(X[i]))

            tmp = min(fX)
            l = fX.index(tmp)   #index najboljeg

            tmp = max(fX)
            h = fX.index(tmp)   #index najlošijeg

            return h,l

        def Odredi_centroid():
            # if len(X)<2:
            #     X_bez_najlosijeg = X
            # else:
            X_bez_najlosijeg = np.delete(np.copy(X), h, 0)  #ukloni red h iz simpleksa
            Xc = np.mean(X_bez_najlosijeg, axis=0)  #napravi aritmeticku sredinu nad svakim stupcem
            return Xc

        def Refleksija():
            return (1+ alfa)*Xc - alfa*X[h]

        def Ekspanzija():
            return (1- gamma)*Xc + gamma*Xr

        def Kontrakcija():
            return (1- beta)*Xc + beta*X[h]

        def Pomak_simpleksa_prema_Xl():
            for i in range(len(X)):
                X[i] = sigma * (X[l] + X[i])
            return X


        #sve dok ne vrijedi uvjet zaustavljanja
        while True:

            #odredi indekse h,l : F(X[h]) = max, F(X[l]) = min;
            h,l = Odredi_indekse_h_l()

            #odredi centroid Xc;
            Xc = Odredi_centroid()

            if ispis:
                print(Xc, f(Xc))

            Xr = Refleksija()

            fXr = f(Xr)
            fXl = f(X[l])

            #ako je reflektirana točka Xr bolja of najbolje onda radimo ekspanziju, 
            # u suprotnom radimo kontrakciju

            if fXr < fXl:  

                Xe = Ekspanzija()

                if f(Xe) < fXl:
                    X[h] = Xe
                else:
                    X[h] = Xr

            else:

                #   {   ako F(Xr)>F(X[j]) za svaki j=0..n, j!=h
                ispunjen_uvjet = True
                X_tmp = np.delete(X, h, 0)
                for j in range(len(X_tmp)):
                    if fXr <= f(X_tmp[j]):
                        ispunjen_uvjet = False
                        break

                if ispunjen_uvjet:

                    if fXr < f(X[h]):
                        X[h] = Xr

                    Xk = Kontrakcija()

                    if f(Xk) < f(X[h]):
                        X[h] = Xk
                    else:
                        #pomakni sve tocke prema X[l];
                        X = Pomak_simpleksa_prema_Xl()

                else:
                    X[h] = Xr


            Xc = Odredi_centroid()
            fXc = f(Xc)
            s = 0.0
            for j in range(len(X)):
                s += ( f(X[j]) - fXc )**2
            if math.sqrt( 1/len(X) * s) <= e:
                break
                
        self.minimum = Xc
        return 