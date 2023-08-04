import math
import numpy as np

from klasa_matrica import Matrica 
from klasa_metode import Metode


class Postupak:

    def __init__(self, f=None):
        self.f = f
        self.minimum = None
        self.vrijednost_fje_u_min = None

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



    def Gradijentni_spust(self, x0, f, grad, koristi_zlatni_rez=True, pomak=1.0, e=10**(-6), file=None, ispis=False):

        if file!=None:
            o = open(file, "r")
            lines = o.readlines()
            o.close()
            x0 = np.array(list(map(float, lines[0].rstrip().split())))   #list(map(int, ['1','2','3']))
            e = float(lines[1].rstrip().split()[0])
            koristi_zlatni_rez = bool(lines[2].rstrip().split()[0])

        x = np.copy(x0)
        x_best = np.copy(x0)
        count_divergencija = 0
        g = grad(x)
        
        def f_zl_rez(l):
            return f(x - l * g / np.linalg.norm(g))  # f(pocetna toka + pomak * smjer)

        while np.linalg.norm(g) > e  and  count_divergencija<10:
            
            if koristi_zlatni_rez:
                l = self.Zlatni_rez(0, f_zl_rez)
                x -= l * g / np.linalg.norm(g)   #pomicemo u smjeru obrnutom od smjera gradijenta

            else:
                x -= pomak * g

            g = grad(x)

            if f(x_best) <= f(x) :
                count_divergencija += 1
            else:
                x_best = np.copy(x)
                count_divergencija = 0


        self.minimum = x_best
        self.vrijednost_fje_u_min = f(x_best)
        return x




    def Rijesi_linearni_sustav(self, A, b):  #pomocu LUP rijesavamo linearan sustav
        A= Matrica(A.tolist())
        m = Metode(A)

        #pretvaram b u matricu s 1 stupcem - neovisno o tome je li dosao 1 red ili 1 stupac
        b = np.asmatrix(b)
        x,y = b.shape
        if y!=1:
            b = b.T

        b = Matrica(b.tolist())

        LUP, P = m.LUP_dekompozicija()
        
        if LUP is not None:

            # P*b šaljemo u supstituciju unatrag i unaprijed
            b = P*b
            b = m.Supstitucija_unaprijed(b)
            b = m.Supstitucija_unatrag(b)
        
        return np.array(b.matrica)


    def Newton_Raphson(self, x0, f, grad, H, koristi_zlatni_rez=True, pomak=1.0, e=10**(-6), file=None, ispis=False):
        if file!=None:
            o = open(file, "r")
            lines = o.readlines()
            o.close()
            x0 = np.array(list(map(float, lines[0].rstrip().split())))   #list(map(int, ['1','2','3']))
            e = float(lines[1].rstrip().split()[0])
            koristi_zlatni_rez = bool(lines[2].rstrip().split()[0])

        x = np.copy(x0)
        x_best = np.copy(x)
        count_divergencija = 0
        delta_x = 1+e
        
        def f_zl_rez(l):
            return f(x + l * v)  # f(pocetna toka + pomak * smjer)

        while np.linalg.norm( delta_x ) > e  and  count_divergencija<10  and  (x<1e+20).all():

            #delta_x = np.linalg.solve( h, grad(x) )
            #umjesto numpy rijesenja moramo koristiti nas rucni LUP
            delta_x = self.Rijesi_linearni_sustav(H(x),grad(x))
            delta_x = np.squeeze(np.asarray(delta_x))

            v = - delta_x / np.linalg.norm( delta_x )

            if koristi_zlatni_rez:
                l = self.Zlatni_rez(0, f_zl_rez)
                x += l * v
            else:
                x += pomak * delta_x

            if f(x_best) <= f(x):
                count_divergencija += 1
            else:
                x_best = np.copy(x)
                count_divergencija = 0


        self.minimum = x_best
        self.vrijednost_fje_u_min = f(x_best)
        return x


    def Gauss_Newton(self, x0, G, J, koristi_zlatni_rez=True, pomak=1.0, e=10**(-6), file=None, ispis=False):

        if file!=None:
            o = open(file, "r")
            lines = o.readlines()
            o.close()
            x0 = np.array(list(map(float, lines[0].rstrip().split())))
            e = float(lines[1].rstrip().split()[0])
            koristi_zlatni_rez = bool(lines[2].rstrip().split()[0])

        x = np.copy(x0)
        x_best = np.copy(x0)
        count_divergencija = 0
        
        def f_zl_rez(l):
            return np.sum(np.power(G(x + l * v), 2))  # f(pocetna toka + pomak * smjer)

        while True:

            J_x = J(x)
            G_x = G(x)
            A = J_x.T @ J_x
            g = J_x.T @ G_x

            # delta_x = np.linalg.solve( A, -g )
            # delta_x = np.squeeze(np.asarray(delta_x))
            
            #umjesto numpy rijesenja moramo koristiti nas rucni LUP
            delta_x = self.Rijesi_linearni_sustav(A,-g)
            delta_x = np.squeeze(np.asarray(delta_x))

            if koristi_zlatni_rez:
                
                if (delta_x != 0).all():
                    v = - delta_x / np.linalg.norm( delta_x )
                else:
                    v = - delta_x

                l = self.Zlatni_rez(0, f_zl_rez)
                x += l* v
            else:
                x += pomak * delta_x


            if np.sum(np.power(G(x_best), 2)) <= np.sum(np.power(G(x), 2)):
                count_divergencija += 1
            else:
                x_best = np.copy(x)
                count_divergencija = 0

            # if (np.abs(l*v)<=e).all() or count_divergencija>20:
            #     break

            if (np.abs(g)<e).all() or count_divergencija>20 or (x>1e+20).any():
                break


        self.minimum = x_best
        self.vrijednost_fje_u_min = np.sum( np.power(G(x_best),2) )
        return x
