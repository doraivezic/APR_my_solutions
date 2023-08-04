import sys
from klasa_matrica import Matrica 

EPSILON = 10**(-9)


class Metode:

    def __init__(self, A=None, epsilon = None):
        self.A = A

        self.kvadratna_matrica()

        self.LU = None
        self.LUP = None
        self.P = None
        self.parnost_zamjene_redova = True

        if epsilon is not None:
            global EPSILON
            EPSILON = 10**epsilon

        return

    def kvadratna_matrica(self):
        if self.A.broj_redaka != self.A.broj_stupaca:
            print("Matrica A nije kvadratna. Nije moguće izvršiti tražene operacije.")
            sys.exit(0)
        return


    def LU_dekompozicija(self):
        N = self.A.broj_redaka

        LU = Matrica()
        LU.Pridruzivanje(self.A)


        for i in range(0, N -1):
            for j in range(i+1, N):

                if abs(LU.matrica[i][i]) < EPSILON:
                    print("Stožerni element u LU dekompoziciji je manji od epsilon. Nije moguće nastaviti dekompoziciju.")
                    self.LU = None
                    return None

                LU.matrica[j][i] /= LU.matrica[i][i]

                for k in range(i+1,N):
                    LU.matrica[j][k] -= LU.matrica[j][i] * LU.matrica[i][k]

        self.LU = LU
        return LU



    def Pivot(self, M, i_red, N):
        #trazim pivot za element A[i,i], tj trazim max vrijednsot u stupcu "i" ispod dijagonale
        
        pivot_redak = i_red
        pivot_vrijednost = M.matrica[i_red][i_red]

        for j in range(i_red+1, N):
            if abs(M.matrica[j][i_red]) > abs(pivot_vrijednost):
                pivot_redak = j
                pivot_vrijednost = M.matrica[j][i_red]

        return (pivot_vrijednost, pivot_redak)

    def LUP_dekompozicija(self):

        N = self.A.broj_redaka

        LUP = Matrica()
        LUP.Pridruzivanje(self.A)

        #stvaranje permutacijske matrice
        P = Matrica()
        P.Pridruzivanje(self.A)
        for i in range(len(P.matrica)):
            for j in range(len(P.matrica)):
                if i == j:
                    P.matrica[i][j] = 1
                else:
                    P.matrica[i][j] = 0
        self.parnost_zamjene_redova = True  #koliko puta je P doživio zamjenu redaka (trbat ce nam za izračun determinante)


        for i in range(0, N -1):

            pivot_vrijednost, pivot_redak = self.Pivot(LUP,i,N)
            if abs(pivot_vrijednost) < EPSILON:
                print("Matrica je singularna. Sustav nema rješenja.")
                self.LUP = None
                self.P = None
                return (None,None)

            if i != pivot_redak:
                LUP.Zamijeni_retke(i, pivot_redak)
                P.Zamijeni_retke(i, pivot_redak)
                self.parnost_zamjene_redova = not self.parnost_zamjene_redova


            for j in range(i+1, N):

                # if abs(LUP.matrica[i][i]) < EPSILON:
                #     print("Stožerni element u LU dekompoziciji je manji od epsilon. Nije moguće nastaviti dekompoziciju.")
                #     return None

                LUP.matrica[j][i] /= LUP.matrica[i][i]

                for k in range(i+1,N):
                    LUP.matrica[j][k] -= LUP.matrica[j][i] * LUP.matrica[i][k]

        self.LUP = LUP
        self.P = P
        return (LUP, P)


    def Supstitucija_unaprijed(self, b, LU_or_LUP=True):  #L*y=b -> vraćamo y, ali zapravo samo mijenjamo b

        #LU_or_LUP : False za LU, True za LUP

        if not LU_or_LUP:
            #dekompozicijska_matrica
            D = self.LU
        else:
            D = self.LUP

        if D is None:
            print("Dekompozicijska matrica nije važeća.")
            return None

        if b.broj_redaka != D.broj_redaka:
            print("Dimenzija matrica A i b ne odgovara.")
            return None

        N = D.broj_redaka

        for i in range(1, N):
            for j in range(0, i):
                b.matrica[i][0] -= D.matrica[i][j]*b.matrica[j][0]
            if abs(b.matrica[i][0]) < EPSILON:
                b.matrica[i][0] = 0.0

        return b

    def Supstitucija_unatrag(self, b, LU_or_LUP=True):  #U*x=y -> vraćamo x, ali zapravo samo mijenjamo b

        #LU_or_LUP : False za LU, True za LUP

        if not LU_or_LUP:
            #dekompozicijska_matrica
            D = self.LU
        else:
            D = self.LUP

        if D is None:
            print("Dekompozicijska matrica nije važeća.")
            return None

        if b.broj_redaka != D.broj_redaka:
            print("Dimenzija matrica A i b ne odgovara.")
            return None

        N = D.broj_redaka

        for i in range(N-1, -1, -1):
            if abs(D.matrica[i][i]) < EPSILON:
                print("Nije moguće nastaviti supstituciju unatrag. Element na dijagonali matrice LU/LUP je manji od epsilon.")
                return None
            b.matrica[i][0] /= D.matrica[i][i]
            for j in range(i+1, N):
                b.matrica[i][0] -= D.matrica[i][j]*b.matrica[j][0]/D.matrica[i][i]
            if abs(b.matrica[i][0]) < EPSILON:
                b.matrica[i][0] = 0.0

        return b


    def Inverz(self):

        if self.LUP is None:
            self.LUP_dekompozicija()

        if self.LUP is None:
            print("Inverz ne postoji.")
            return None

        inverzna_matrica = []

        for stupac_iz_P in (~self.P).matrica:
            
            b = Matrica([stupac_iz_P])
            b = ~b
            b = self.Supstitucija_unaprijed(b)
            b = self.Supstitucija_unatrag(b)
            if b is None:
                print("Nije moguće izračunati inverz.")
                return None
            b = ~b
            inverzna_matrica.extend(b.matrica)

        inverzna_matrica = Matrica( inverzna_matrica )
        inverzna_matrica = ~inverzna_matrica

        return inverzna_matrica


    def Determinanta(self):

        if self.LUP is None:
            self.LUP_dekompozicija()

        if self.LUP is None:
            return 0.0

        if self.parnost_zamjene_redova: #det(P^-1)
            det = 1
        else:
            det = -1
        
        #det(L) = 1 uvijek je 1

        #det(U) = mnozenje elemenata na dijagonali matrice LUP
        for i in range(self.LUP.broj_redaka):
            det *= self.LUP.matrica[i][i]

        return det