import math
import numpy as np
from klasa_matrica import Matrica
from klasa_metode import Metode

class Postupak:

    def __init__(self, T, t_max, A, B, x0, r, ispis):
        self.A = A
        self.B = B
        self.x0 = x0
        self.r = r
        self.T = T
        self.t_max = t_max
        self.ispis = ispis

    def __del__(self):
        return



    def Runge_Kutta(self, trenutak=None):

        if self.ispis != math.inf:
            print("\n  RUNGE-KUTTA")

        x_k = Matrica()
        x_k.Pridruzivanje(self.x0)

        lista_x = []

        for i in range( int((self.t_max) / self.T) + 1 ):

            if i % self.ispis == 0 and self.ispis != math.inf:
                print("\nTrenutak t =", self.T*i)
                x_k.Ispisi_matricu()

            lista_x.append( np.array(x_k.matrica) )

            if trenutak is None:
                t = self.T * i
            else:
                t = trenutak

            if self.B is not None:
                m1 = self.A * x_k + self.B * self.r(t)
                m2 = self.A * (x_k + self.T /2 * m1)    + self.B * self.r(t + self.T /2)
                m3 = self.A * (x_k + self.T /2 * m2)    + self.B * self.r(t + self.T /2)
                m4 = self.A * (x_k + self.T * m3)       + self.B * self.r(t + self.T)
            else:
                m1 = self.A * x_k
                m2 = self.A * (x_k + self.T /2 * m1)
                m3 = self.A * (x_k + self.T /2 * m2)
                m4 = self.A * (x_k + self.T * m3)

            x_k = x_k + self.T /6 * (m1 + 2*m2 + 2*m3 + m4)

            if trenutak is not None:
                return x_k
                
        return lista_x



    def Euler(self, trenutak=None):

        if self.ispis != math.inf:
            print("\n  EULER")

        x_k = Matrica()
        x_k.Pridruzivanje(self.x0)

        lista_x = []

        for i in range( int((self.t_max) / self.T) + 1 ):

            if i % self.ispis == 0 and self.ispis != math.inf:
                print("\nTrenutak t =", self.T*i)
                x_k.Ispisi_matricu()

            lista_x.append( np.array(x_k.matrica) )

            if trenutak is None:
                t = self.T*(i)
            else:
                t = trenutak

            if self.B is not None:
                x_deriv = self.A * x_k + self.B * self.r(t)
            else:
                x_deriv = self.A * x_k

            x_k = x_k + self.T * x_deriv

            if trenutak is not None:
                return x_k
                
        return lista_x



    def Obrnuti_Euler(self, trenutak=None, x_dobiveni=None):

        if self.ispis != math.inf:
            print("\n  OBRNUTI EULER")

        x_k = Matrica()
        x_k.Pridruzivanje(self.x0)

        #tranfsormirati u eksplicitni oblik

        U = Matrica(np.eye(self.x0.broj_redaka).tolist())

        lijeva_strana = (U - self.A * self.T)

        m = Metode(lijeva_strana)
        LUP, P = m.LUP_dekompozicija()

        if LUP is None:
            print("Postupak nije uspio.")

        lista_x = []

        for i in range( int((self.t_max) / self.T) + 1 ):

            if i % self.ispis == 0 and self.ispis != math.inf:
                print("\nTrenutak t =", self.T*i)
                x_k.Ispisi_matricu()
            
            lista_x.append( np.array(x_k.matrica) )

            if trenutak is None:
                t = self.T*(i+1)
            else:
                t = trenutak
                x_k = x_dobiveni

                if self.B is None:
                    x_deriv = self.A * x_k 
                else:
                    x_deriv = self.A * x_k + self.B * self.r(t)

                x_k = self.x0 + self.T * x_deriv

                return x_k

            if self.B is not None:
                desna_strana = x_k + self.T * self.B * self.r(t)
            else:
                desna_strana = x_k


            #racunamo sustav: lijeva_strana * x_k_novi = desna_strana

            # P*b šaljemo u supstituciju unatrag i unaprijed
            desna_strana = P*desna_strana
            desna_strana = m.Supstitucija_unaprijed(desna_strana)
            desna_strana = m.Supstitucija_unatrag(desna_strana)

            x_k.Pridruzivanje(desna_strana)

        return lista_x



    def Trapez(self, trenutak=None, x_dobiveni=None):

        if self.ispis != math.inf:
            print("\n  TRAPEZ")

        x_k = Matrica()
        x_k.Pridruzivanje(self.x0)

        #tranfsormirati u eksplicitni oblik

        U = Matrica(np.eye(self.x0.broj_redaka).tolist())

        lijeva_strana = (U - self.A * self.T /2)
        
        m = Metode(lijeva_strana)
        LUP, P = m.LUP_dekompozicija()

        if LUP is None:
            print("Postupak nije uspio.")


        lista_x = []

        for i in range( int((self.t_max) / self.T) + 1 ):

            if i % self.ispis == 0 and self.ispis != math.inf:
                print("\nTrenutak t =", self.T*i)
                x_k.Ispisi_matricu()
            
            lista_x.append( np.array(x_k.matrica) )

            if trenutak is None:
                t = self.T* i
                t_plus1 = self.T*(i+1)
            else:
                t = trenutak
                x_k = x_dobiveni

                if self.B is None:
                    x_deriv = self.A * self.x0 
                    x_deriv_plus1 = self.A * x_k 
                else:
                    x_deriv = self.A * self.x0 + self.B * self.r(t)
                    x_deriv_plus1 = self.A * x_k + self.B * self.r(t+self.T)

                x_k = self.x0 + self.T /2 * (x_deriv + x_deriv_plus1)

                return x_k

            if self.B is not None:
                desna_strana = (U + self.A * self.T /2) * x_k  +  self.T /2 * self.B * ( self.r(t) + self.r(t_plus1) )
            else:
                desna_strana = (U + self.A * self.T /2) * x_k


            #racunamo sustav: lijeva_strana * x_k_novi = desna_strana

            # P*b šaljemo u supstituciju unatrag i unaprijed
            desna_strana = P*desna_strana
            desna_strana = m.Supstitucija_unaprijed(desna_strana)
            desna_strana = m.Supstitucija_unatrag(desna_strana)

            x_k.Pridruzivanje(desna_strana)

            if trenutak is not None:
                return x_k

        return lista_x



    def Prediktorsko_korektorski(self, prediktor=Euler, korektor=Obrnuti_Euler, S=2):

        print("\n  PREDIKTORSKO-KOREKTORSKI S =", S)

        ispis1 = self.ispis
        self.ispis = math.inf

        x_k = Matrica()
        x_k.Pridruzivanje(self.x0)

        lista_x = []
        lista_x.append( np.array(x_k.matrica) )

        #u svakom trenutku radimo PE(CE)^S
        for i in range(1, int((self.t_max) / self.T) + 1 ):

            self.x0 = x_k

            #PE
            x_k = prediktor(trenutak= self.T * i)

            for s in range(S):

                #CE
                x_k = korektor(trenutak= self.T * i, x_dobiveni=x_k)
                
            lista_x.append( np.array(x_k.matrica) )
            if i % ispis1 == 0:
                print("\nTrenutak t =", self.T*i)
                x_k.Ispisi_matricu()

        return lista_x
