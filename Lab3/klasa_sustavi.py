import numpy as np
import math

class Sustav:

    def __init__(self, broj_fje, parovi=[]):

        self.broj_fje = broj_fje
        self.broj_pozivanja_G = 0
        self.broj_pozivanja_J = 0
        self.parovi = parovi

    def G(self, x):

        self.broj_pozivanja_G += 1

        if self.broj_fje == 1:
            x1= x[0]
            x2 = x[1]

            g1 = 10*(x2-x1**2)
            g2 = 1-x1
            return np.array([ g1, g2 ])

        elif self.broj_fje == 2:
            x1= x[0]
            x2 = x[1]

            g1 = x1**2 + x2**2 -1
            g2 = x2-x1**2
            return np.array([ g1, g2 ])

        elif self.broj_fje == 6:
            x1= x[0]
            x2 = x[1]
            x3 = x[2]

            matrica_G = np.empty([1,1])

            for par in self.parovi:
                t = par[0]
                y = par[1]
                gi = x1 * math.exp(x2*t) + x3 - y
                matrica_G = np.append(matrica_G, [[gi]], axis=0)

            matrica_G = np.delete(matrica_G, 0,0)

            return matrica_G


    def J(self, x):

        self.broj_pozivanja_J += 1

        if self.broj_fje == 1:
            x1= x[0]
            x2 = x[1]
            return np.array([ [-20*x1, 10],
                                  [-1,0] ])

        elif self.broj_fje == 2:
            x1= x[0]
            x2 = x[1]
            return np.array([ [2*x1, 2*x2],
                             [-2*x1, 1] ])

        elif self.broj_fje == 6:
            x1= x[0]
            x2 = x[1]
            #x3 = x[2]

            matrica_J = np.empty([1,3])

            for par in self.parovi:
                t = par[0]
                #y = par[1]

                ji = [ math.exp(x2*t), t*x1*math.exp(x2*t), 1 ]
                matrica_J = np.append(matrica_J, [ji], axis=0)


            matrica_J = np.delete(matrica_J, 0,0)

            return matrica_J

    def Resetiraj(self):
        self.broj_pozivanja_G = 0
        self.broj_pozivanja_J = 0


    def __del__(self):
        return