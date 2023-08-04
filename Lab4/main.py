from klasa_funkcije import Funkcija
from klasa_postupci import Postupak
from klasa_ogranicenja import Ogranicenje
import numpy as np


if __name__=="__main__":


    print("\n----ZADATAK 1-----")

    impl = [Ogranicenje(1).Provjeri_ogranicenje, Ogranicenje(2).Provjeri_ogranicenje]
    xd = [-100,-100]
    xg = [100,100]
    
    x0 = [-1.9, 2]
    f = Funkcija(1)
    postupak = Postupak(f)
    
    print("\n Postupak po Boxu")
    print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)
    postupak.Box(np.array(x0), xd, xg, f.Racunaj_vrijednost_fje, impl)  
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije u minimumu", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije:", f.broj_pozivanja)

    del f
    postupak.Resetiraj()

    x0 = [0.1, 0.3]
    f = Funkcija(2)
    postupak = Postupak(f)
    
    print("\n Postupak po Boxu")
    print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)
    postupak.Box(np.array(x0), xd, xg, f.Racunaj_vrijednost_fje, impl)  
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije u minimumu", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije:", f.broj_pozivanja)

    del f
    del postupak




    print("\n----ZADATAK 2-----")

    impl = [Ogranicenje(1).Provjeri_ogranicenje, Ogranicenje(2).Provjeri_ogranicenje]
    
    x0 = [-1.9, 2]
    f = Funkcija(1)
    postupak = Postupak(f)
    
    print("\n Transformacija u problem bez ograničenja na mješoviti način")
    print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)
    postupak.Transformacija_mjesoviti(np.array(x0), f.Racunaj_vrijednost_fje, impl)  
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije u minimumu", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije:", f.broj_pozivanja)

    del f
    postupak.Resetiraj()

    x0 = [1.9, 2]
    f = Funkcija(1)
    postupak = Postupak(f)
    
    print("\n Transformacija u problem bez ograničenja na mješoviti način")
    print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)
    postupak.Transformacija_mjesoviti(np.array(x0), f.Racunaj_vrijednost_fje, impl)  
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije u minimumu", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije:", f.broj_pozivanja)

    del f
    postupak.Resetiraj()

    x0 = [0.1, 0.3]
    f = Funkcija(2)
    postupak = Postupak(f)
    
    print("\n Transformacija u problem bez ograničenja na mješoviti način")
    print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)
    postupak.Transformacija_mjesoviti(np.array(x0), f.Racunaj_vrijednost_fje, impl)  
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije u minimumu", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije:", f.broj_pozivanja)

    del f
    del postupak




    print("\n----ZADATAK 3-----")

    nejedn = [Ogranicenje(3).Provjeri_ogranicenje, Ogranicenje(4).Provjeri_ogranicenje]
    jedn = [Ogranicenje(5).Provjeri_ogranicenje]
    
    x0 = [5.0, 5.0]
    f = Funkcija(4)
    postupak = Postupak(f)
    
    print("\n Transformacija u problem bez ograničenja na mješoviti način")
    print("Pocetna točka:",x0, "  Funkcija:", f.broj_fje)
    postupak.Transformacija_mjesoviti(np.array(x0), f.Racunaj_vrijednost_fje, nejedn, jedn)  
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije u minimumu", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije:", f.broj_pozivanja)

    del f
    del postupak