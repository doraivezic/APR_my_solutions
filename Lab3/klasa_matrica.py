import sys
#obicna 2D matrica
#red i stupac su uvijek vrijednosti od 0 do length-1
class Matrica:

    def __init__(self, elementi_matrice=[]):

        self.matrica = []
        self.broj_redaka = len(elementi_matrice)
        if len(elementi_matrice)==0:
            self.broj_stupaca = 0
            return
            

        if type(elementi_matrice[0]) == str:
            for red in elementi_matrice:
                tmp_red = []
                for el in red.rstrip().split():
                    tmp_red.append(float(el))  #double je u pythonu float (64 bita)
                self.matrica.append(tmp_red)

        else:
            for red in elementi_matrice:
                tmp_red = []
                for el in red:
                    tmp_red.append(float(el))  #double je u pythonu float (64 bita)
                self.matrica.append(tmp_red)
            
        self.broj_stupaca = len(tmp_red)

    def __del__(self):
        return


    def Ispisi_matricu(self):

        if self.matrica is None:
            print("Nije moguće ispisati matricu.")
            return

        s = ""
        for red in range(self.broj_redaka):
            for stupac in range(self.broj_stupaca):
                s += str(self.matrica[red][stupac]) + "\t"
            s += "\n"
            
        print(s[:-1])
        return

    def Spremi_matricu(self, file_name):

        s = ""
        for red in range(self.broj_redaka):
            for stupac in range(self.broj_stupaca):
                s += str(self.matrica[red][stupac]) + "\t" +"\t"
            s += "\n"
            
        f = open(file_name, "w")
        f.write(s[:-1])
        f.close()
        return
            
    def Promijeni_element(self, red, stupac, novi_element):

        if red < self.broj_redaka and stupac < self.broj_stupaca:
            self.matrica[red][stupac] = float(novi_element)
        else:
            print("Neispravan unos elementa za promjenu.")
        return

    def Promijeni_dimenzije(self, novi_broj_redaka, novi_broj_stupaca):  #ako se dimenzija povecava onda popuniti s nulama taj red ili stupac

        #prvo radimo na stupcima
        if self.broj_stupaca>=novi_broj_stupaca:
            for red in range(self.broj_redaka):
                self.matrica[red] = self.matrica[red][:novi_broj_stupaca]
        else:
            tmp = [0] * (novi_broj_stupaca - self.broj_stupaca )
            for red in range(self.broj_redaka):
                self.matrica[red].extend(tmp)

        #zatim radimo na retcima
        if self.broj_redaka>=novi_broj_redaka:
            self.matrica = self.matrica[:novi_broj_redaka]
        else:
            for red in range(novi_broj_redaka - self.broj_redaka):
                self.matrica.append(self.matrica[0].copy())

        self.broj_redaka = novi_broj_redaka
        self.broj_stupaca = novi_broj_stupaca

        
        return

    def Dohvati_element(self, red, stupac):
        if red < self.broj_redaka and stupac < self.broj_stupaca:
            return self.matrica[red][stupac]
        print("Neispravan unos elementa za dohvat.")
        return

    def Pridruzivanje(self, matrica_B):  #A=B  kopiramo matricu B u matricu A

        self.broj_redaka = matrica_B.broj_redaka
        self.broj_stupaca = matrica_B.broj_stupaca
        self.matrica = [red.copy() for red in matrica_B.matrica]
        return


    def __add__(self, other):  # A+B = C

        if type(other) == int  or  type(other) == float:
            print("Ova operacija nije moguća.")
            sys.exit(0)
            return  None

        if self.broj_redaka == other.broj_redaka and self.broj_stupaca == other.broj_stupaca:
                
            elementi_matrice_C = []
            for red in range(self.broj_redaka):
                tmp_red = []
                for stupac in range(self.broj_stupaca):
                    tmp_red.append( float( self.matrica[red][stupac] + other.matrica[red][stupac] ) )
                elementi_matrice_C.append(tmp_red)
                
            C = Matrica(elementi_matrice_C)
            return  C

        else:
            print("Dimenzije se ne poklapaju! Nije moguće izvršiti operaciju zbrajanja.")
            sys.exit(0)
            return None

    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, other):  # A-B = C

        if type(other) == int  or  type(other) == float:
            print("Ova operacija nije moguća.")
            sys.exit(0)
            return  None

        if self.broj_redaka == other.broj_redaka and self.broj_stupaca == other.broj_stupaca:
                
            elementi_matrice_C = []
            for red in range(self.broj_redaka):
                tmp_red = []
                for stupac in range(self.broj_stupaca):
                    tmp_red.append( float( self.matrica[red][stupac] - other.matrica[red][stupac] ) )
                elementi_matrice_C.append(tmp_red)
                
            C = Matrica(elementi_matrice_C)
            return  C

        else:
            print("Dimenzije se ne poklapaju! Nije moguće izvršiti operaciju oduzimanja.")
            sys.exit(0)
            return None

    def __rsub__(self, other):
        return self.__asub__(other)


    def __mul__(self, other):

        #mnozenje skalarom C = A*5
        if type(other) == int  or  type(other) == float:
            elementi_matrice_C = []
            for red in range(self.broj_redaka):
                tmp_red = []
                for stupac in range(self.broj_stupaca):
                    tmp_red.append(float( float(self.matrica[red][stupac]) * other ) )
                elementi_matrice_C.append(tmp_red)

            C = Matrica(elementi_matrice_C)
            return  C

            #ili
            C = Matrica()
            C.Pridruzivanje(self)
            tmp= []
            for stupac in range(self.broj_stupaca):
                tmp.append(float( float(self.matrica[0][stupac]) * other ) )
                C.matrica[0] = tmp

            print(C.broj_redaka, C.broj_stupaca)
            return  C
    
        #mnozenje matrica C = A*B
        elementi_matrice_C = []
        if self.broj_stupaca == other.broj_redaka:
            elementi_matrice_C = []
            for red in range(self.broj_redaka):
                tmp_red = []
                for br_stupaca_u_drugoj in range(other.broj_stupaca):
                    suma = 0.0
                    for stupac in range(self.broj_stupaca):
                        suma += self.matrica[red][stupac] * other.matrica[stupac][br_stupaca_u_drugoj]
                    tmp_red.append(suma)
                
                elementi_matrice_C.append(tmp_red)
                
            C = Matrica(elementi_matrice_C)
            return  C

    __rmul__ = __mul__


    def __truediv__(self, other):

        #dijeljenje skalarom C = A/5
        if type(other) == int  or  type(other) == float:
            elementi_matrice_C = []
            for red in range(self.broj_redaka):
                tmp_red = []
                for stupac in range(self.broj_stupaca):
                    tmp_red.append(float( float(self.matrica[red][stupac]) / other ) )
                elementi_matrice_C.append(tmp_red)

            C = Matrica(elementi_matrice_C)
            return  C

    def __eq__(self, B): #za operator ==, tje za usporedbu martrica

        if self.broj_redaka != B.broj_redaka or self.broj_stupaca != B.broj_stupaca:
            return False

        for red in range(self.broj_redaka):
            if self.matrica[red] != B.matrica[red]:
                return False

        return True


    def __iadd__(self, other):
        self = self + other
        return self
    
    def __isub__(self, other):
        self = self - other
        return self


    def __invert__(self):   #operator ~, koristi se za transponiranje
        B = Matrica()
        B.Pridruzivanje( self )

        self.Promijeni_dimenzije(B.broj_stupaca, B.broj_redaka)

        for red in range(B.broj_redaka):
            for stupac in range(B.broj_stupaca):
                self.matrica[stupac][red] = B.matrica[red][stupac]

        return self





    def Zamijeni_retke(self,a,b):
        self.matrica[a], self.matrica[b] = self.matrica[b], self.matrica[a]
        return