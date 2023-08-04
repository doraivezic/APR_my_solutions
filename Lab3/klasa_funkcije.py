import numpy as np

class Funkcija:

    def __init__(self, broj_fje):

        self.broj_fje = broj_fje
        self.broj_pozivanja = 0
        self.broj_pozivanja_gradijenta = 0
        self.broj_pozivanja_H = 0

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
            return 0.25 * x1**4 - x1**2 + 2*x1 + (x2-1)**2


    def Racunaj_Gradijent(self, x=[]):

        self.broj_pozivanja_gradijenta += 1

        if self.broj_fje == 1:
            x1= x[0]
            x2 = x[1]
            return np.array([ 200 * (x2-x1**2) * (-2)*x1 - 2*(1-x1),  200 * (x2-x1**2) ])
            
        elif self.broj_fje == 2:
            x1= x[0]
            x2 = x[1]
            return np.array([ 2*(x1-4) , 8*(x2-2) ])

        elif self.broj_fje == 3:
            x1= x[0]
            x2 = x[1]
            return np.array([ 2*(x1-2) , 2*(x2+3) ])

        elif self.broj_fje == 4:
            x1= x[0]
            x2 = x[1]
            return np.array([ x1**3 - 2*x1 + 2 , 2*(x2-1) ])

    
    def Racunaj_Hesseovu_matricu(self, x=[]):

        self.broj_pozivanja_H += 1

        if self.broj_fje == 1:
            x1= x[0]
            x2 = x[1]
            return np.array([ [1200*x1**2 - 400*x2 + 2 , -400*x1],
                                              [-400*x1 , 200] ])
            
        elif self.broj_fje == 2:
            return np.array([ [2, 0],
                              [0, 8] ])

        elif self.broj_fje == 3:
            return np.array([ [2, 0],
                              [0, 2] ])

        elif self.broj_fje == 4:
            return np.array([ [2, 0],
                              [0, 2] ])


    def Resetiraj(self):
        self.broj_pozivanja = 0
        self.broj_pozivanja_gradijenta = 0
        self.broj_pozivanja_H = 0

    def __del__(self):
        return
