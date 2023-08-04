from klasa_funkcije import Funkcija
from klasa_ogranicenja import Ogranicenje
import math
import numpy as np

class Postupak:

    def __init__(self, f):
        self.f = f
        self.minimum = None
        self.vrijednost_fje_u_min = None

    def Resetiraj(self):
        self.minimum = None
        self.vrijednost_fje_u_min = None

    def __del__(self):
        return






    def Hooke_Jevees(self, x0, f, dx=1, e=10**(-6), file=None, ispis=False):

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
                print(xB,xP,xN, f(xB), f(xN))

            if f(xN)<f(xB):   #ako je novi pomak bolji od starog (ili pocetnog)
                xP = 2*xN - xB
                xB = np.copy(xN)
            else:
                dx/=2  #smanjujemo dx
                xP = np.copy(xB)
             
        return xB






    def Box(self, x0, xd, xg, f, impl_ogr=[], e=10**(-6), alfa=1.3, file=None, ispis=False):

        if file!=None:
            o = open(file, "r")
            lines = o.readlines()
            o.close()
            x0 = np.array(list(map(float, lines[0].rstrip().split())))   #list(map(int, ['1','2','3']))
            e = float(lines[1].rstrip().split()[0])
            alfa = np.array(list(map(float, lines[2].rstrip().split())))
            
        #provjeri da li za X0 vrijedi (Xd <= X0 <= Xg) te (g(X0) >= 0)
        if not (xd<=x0).all() or not (x0<=xg).all():
            print("Eksplicitna ograničenja nisu zadovoljena za početnu točku")
            return
        for ogr in impl_ogr:
            if ogr(x0) < 0:
                print("Implicitna ograničenja nisu zadovoljena za početnu točku")
                return

        xc = np.copy(x0)
        X = []
        n = len(x0)



        def Odredi_centroid(h = None):
            if h is None:
                return np.mean(X, axis=0)
            X_bez_najlosijeg = np.delete(np.copy(X), h, 0)  #ukloni red h iz simpleksa
            return np.mean(X_bez_najlosijeg, axis=0)  #napravi aritmeticku sredinu nad svakim stupcem

        def Odredi_indekse_h_h2():
            fX=[]
            for i in range(len(X)):
                fX.append(f(X[i]))

            tmp = max(fX)
            h = fX.index(tmp)   #index najlošijeg

            fX[h] = -math.inf
            tmp = max(fX)
            h2 = fX.index(tmp)   #index drugog najlošijeg

            return h,h2



        for i in range(2*n):
            X.append(np.copy(x0).tolist())

        for t in range(2*n-1):

            for i in range(n):
                R = np.random.rand()
                X[t][i] = xd[i] + R*(xg[i] - xd[i])
        
            nastavi = True
            while nastavi:
                nastavi = False
                for ogr in impl_ogr:
                    if ogr(X[t]) < 0:
                        nastavi = True
                if nastavi:
                    X[t] = (1/2 * (np.array(X[t],dtype=object) + xc)).tolist()
            
            xc = Odredi_centroid()

        X = np.array(X)


        def Uvjet_zaustavljanja(X):
            s = 0.0
            for j in range(len(X)):
                s += ( f(X[j]) - f(xc) )**2
            if math.sqrt( 1/len(X) * s) <= e:
                return False
            else:
                return True

        while Uvjet_zaustavljanja(X):
            #odredi indekse h, h2 : F(X[h]) = max, F(X[h2]) = drugi najlosiji;
            h, h2 = Odredi_indekse_h_h2()

            #izracunaj Xc (bez X[h]);
            xc = Odredi_centroid(h)

            #Xr = (1+a)*Xc - a*X[h]; // refleksija
            xr = (1+alfa)*xc - alfa*X[h]

            for i in range(n):

                if xr[i]<xd[i]:
                    #pomicemo na granicu ekspl. ogranicenja
                    xr[i]=xd[i]
                
                elif xr[i]>xg[i]:
                    xr[i] = xg[i]

            #provjeravamo implicitna ogr.
            end = False
            while not end:
                end = True
                for ogr in impl_ogr:
                    if ogr(xr) < 0:
                        end = False
                if not end:
                    xr = 1/2 * (xr + xc)   

            #ako je to i dalje najlosija tocka
            if f(xr) > f(X[h2]):
                xr = 1/2 * (xr + xc)   #jos jednom pomakni prema Xc

            if np.linalg.norm(xc-xr) <= e:
                print("Postupak divergira")
                return

            X[h] = xr
        
        self.minimum = xc
        self.vrijednost_fje_u_min = f(xc)
        return


    def Transformacija_mjesoviti(self, x0, f, ogr_nejednakosti=[], ogr_jednakosti=[], e=10**(-6), file=None, ispis=False):

        if file!=None:
            o = open(file, "r")
            lines = o.readlines()
            o.close()
            x0 = np.array(list(map(float, lines[0].rstrip().split())))   #list(map(int, ['1','2','3']))
            e = float(lines[1].rstrip().split()[0])
            
        #postupak pronalaženja početne unutarnje točke
        def G_pocetna_tocka(x):
            rez = 0.0
            for ogr in ogr_nejednakosti:
                if ogr(x) < 0:
                    rez -= ogr(x)
            return rez

        #funkcija koju je potrebno minimizirati
        def U(x):
            rez = f(x)

            tmp = 0
            for ogr in ogr_nejednakosti:
                if ogr(x) <= 0:
                    return math.inf
                tmp += math.log( ogr(x) )
            rez -= 1/t * tmp

            tmp = 0
            for ogr in ogr_jednakosti:
                tmp += t * np.sum( ogr(x) **2 )
            rez += t * tmp
                
            return rez

        t = 1   # 1/r
        #u svakoj iteraciji primjeniti postupak minimizacije bez ogranicenja (Hooke-Jeeves)
        #nakon svake iteracije povećati t 10 puta

        x = np.copy(x0)

        #ako x0 ne zadovoljava sva ogranicenja onda na temelju nje tražimo neku koja zadovoljava
        for ogr in ogr_nejednakosti:
            if ogr(x0) < 0:
                x = self.Hooke_Jevees(x0, G_pocetna_tocka)
                print("Početna točka nakon pronalaska unutarnje točke:",x)
                break

        while True:

            x_new = self.Hooke_Jevees(x, U)

            if np.linalg.norm(x-x_new) <= e:
                self.minimum = x_new
                self.vrijednost_fje_u_min = f(x_new)
                return x_new

            x = x_new

            t *= 10
        




