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
            x1= x[0]
            x2 = x[1]
            return (x1-2)**2 + (x2+3)**2

        elif self.broj_fje == 4:
            x1= x[0]
            x2 = x[1]
            return (x1-3)**2 + x2**2


    def Resetiraj(self):
        self.broj_pozivanja = 0

    def __del__(self):
        return
