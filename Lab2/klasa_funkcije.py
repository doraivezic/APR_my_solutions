import math

class Funkcija:

    def __init__(self, broj_fje):

        self.broj_fje = broj_fje
        self.broj_pozivanja = 0

    def Racunaj_vrijednost_fje(self, x=[]):

        self.broj_pozivanja += 1

        if self.broj_fje == 1:
            x1= x[0]
            x2 = x[1]
            return 100 * (x2-x1**2)**2 + (1-x1)**2

        elif self.broj_fje == 2:
            x1= x[0]
            x2 = x[1]
            return (x1-4)**2 + 4*(x2-2)**2

        elif self.broj_fje == 3:
            s = 0.0
            for i in range(len(x)):
                s += (x[i] - (i+1))**2
            return s

        elif self.broj_fje == 31:
            return (x[0]-3)**2

        elif self.broj_fje == 4:
            x1= x[0]
            x2 = x[1]
            return abs( (x1-x2)*(x1+x2) ) + math.sqrt(x1**2 + x2**2)

        elif self.broj_fje == 6:
            s = 0.0
            for i in range(len(x)):
                s += (x[i])**2
            return 0.5  +  ((math.sin(s)**2) - 0.5) / (1+0.001*s)**2

    def Resetiraj(self):
        self.broj_pozivanja = 0

    def __del__(self):
        return
