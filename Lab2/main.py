from klasa_funkcije import Funkcija
from klasa_postupci import Postupak
import numpy as np
import random


if __name__=="__main__":

    zad1, zad2, zad3, zad4, zad5 = False, True, False, False, False

    if zad1:
        print("\n----ZADATAK 1-----")   #f3, odg: min u x=3

        x0 = 10.0
        f = Funkcija(31)
        postupak = Postupak(f)
        print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)
        
        print("\n Postupak zlatnog reza")
        postupak.Zlatni_rez(np.array([x0]), f.Racunaj_vrijednost_fje)    #file za postavljanje intervala: "zlatni_rez_zad.txt"
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        f.Resetiraj()
        postupak.Resetiraj()

        print("\n Pretraživanje po koordinatnim osima")
        postupak.Trazenje_po_koord_osima(np.array([x0]), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        f.Resetiraj()
        postupak.Resetiraj()

        print("\n Postupak Hooke-Jevees")
        postupak.Hooke_Jevees(np.array([x0]), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        f.Resetiraj()
        postupak.Resetiraj()

        print("\n Simpleks postupak po Nelderu i Meadu")
        postupak.Simpleks(np.array([x0]), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        del postupak
        del f

        
        
    if zad2:
        print("\n----ZADATAK 2-----")

        print("\n--PODZADATAK 1--")

        x0 = [-1.9, 2.0]
        f = Funkcija(1)
        postupak = Postupak(f)
        print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)

        print("\n Pretraživanje po koordinatnim osima")
        postupak.Trazenje_po_koord_osima(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        f.Resetiraj()
        postupak.Resetiraj()

        print("\n Postupak Hooke-Jevees")
        postupak.Hooke_Jevees(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        f.Resetiraj()
        postupak.Resetiraj()

        print("\n Simpleks postupak po Nelderu i Meadu")
        postupak.Simpleks(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        del postupak
        del f

        #------------------------------

        print("\n--PODZADATAK 2--")

        x0 = [0.1, 0.3]
        f = Funkcija(2)
        postupak = Postupak(f)
        print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)

        print("\n Pretraživanje po koordinatnim osima")
        postupak.Trazenje_po_koord_osima(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        f.Resetiraj()
        postupak.Resetiraj()

        print("\n Postupak Hooke-Jevees")
        postupak.Hooke_Jevees(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        f.Resetiraj()
        postupak.Resetiraj()

        print("\n Simpleks postupak po Nelderu i Meadu")
        postupak.Simpleks(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        del postupak
        del f

        #------------------------------

        print("\n--PODZADATAK 3--")

        x0 = [0.0, 0.0, 0.0, 0.0, 0.0]
        f = Funkcija(3)
        postupak = Postupak(f)
        print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)

        print("\n Pretraživanje po koordinatnim osima")
        postupak.Trazenje_po_koord_osima(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum.tolist())
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        f.Resetiraj()
        postupak.Resetiraj()

        print("\n Postupak Hooke-Jevees")
        postupak.Hooke_Jevees(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        f.Resetiraj()
        postupak.Resetiraj()

        print("\n Simpleks postupak po Nelderu i Meadu")
        postupak.Simpleks(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        del postupak
        del f

        #------------------------------

        print("\n--PODZADATAK 4--")

        x0 = [5.1, 1.1]
        f = Funkcija(4)
        postupak = Postupak(f)
        print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)

        print("\n Pretraživanje po koordinatnim osima")
        postupak.Trazenje_po_koord_osima(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        f.Resetiraj()
        postupak.Resetiraj()

        print("\n Postupak Hooke-Jevees")
        postupak.Hooke_Jevees(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        f.Resetiraj()
        postupak.Resetiraj()

        print("\n Simpleks postupak po Nelderu i Meadu")
        postupak.Simpleks(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        del postupak
        del f



        
    if zad3:
        print("\n----ZADATAK 3-----")

        x0 = [5.0,5.0]
        f = Funkcija(4)
        postupak = Postupak(f)
        print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)

        print("\n Postupak Hooke-Jevees")
        postupak.Hooke_Jevees(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        f.Resetiraj()
        postupak.Resetiraj()

        print("\n Simpleks postupak po Nelderu i Meadu")
        postupak.Simpleks(np.array(x0), f.Racunaj_vrijednost_fje)
        print("Minimum:", postupak.minimum)
        print("Broj pozivanja funkcije:", f.broj_pozivanja)

        del postupak
        del f




    if zad4:
        print("\n----ZADATAK 4-----") 

        x0 = [0.5, 0.5]
        f = Funkcija(1)
        postupak = Postupak(f)
        print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)

        for i in range(1,20+1):
            print("\n Simpleks postupak po Nelderu i Meadu uz pomak", i)
            postupak.Simpleks(np.array(x0), f.Racunaj_vrijednost_fje, pomak=i)
            print("Minimum:", postupak.minimum)
            print("Broj pozivanja funkcije:", f.broj_pozivanja)
            f.Resetiraj()
            postupak.Resetiraj()

        x0 = [20.0,20.0]
        print("\nPocetna točka:",x0, "  Funkcija:", f.broj_fje)
        for i in range(1,20+1):
            print("\n Simpleks postupak po Nelderu i Meadu uz pomak", i)
            postupak.Simpleks(np.array(x0), f.Racunaj_vrijednost_fje, pomak=i)
            print("Minimum:", postupak.minimum)
            print("Broj pozivanja funkcije:", f.broj_pozivanja)
            f.Resetiraj()
            postupak.Resetiraj()

        del postupak
        del f

        



    if zad5:
        print("\n----ZADATAK 5-----")

        f = Funkcija(6)
        postupak = Postupak(f)
        print("Pocetne točke su slučajno odabrane.", "  Funkcija:", f.broj_fje)

        s = 0
        for i in range(2000):

            x0 = [random.uniform(-50, 50), random.uniform(-50, 50)]
            postupak.Simpleks(np.array(x0), f.Racunaj_vrijednost_fje)

            #print(f.Racunaj_vrijednost_fje(postupak.minimum))
            if (f.Racunaj_vrijednost_fje(postupak.minimum)).max() < 10**(-4):
                s += 1
            
            postupak.Resetiraj()
            f.Resetiraj()

        print("Vjerojatnost pronalaska globalnog optimuma: ", s/2000*100, "%")

        del postupak
        del f
