from klasa_funkcije import Funkcija
from klasa_postupci import Postupak
from klasa_sustavi import Sustav
import numpy as np


if __name__=="__main__":

    #ZAD1 - GRADIJENTNI SPUST NA f3
    print("\n----ZADATAK 1-----")   #odg: min u x=(2,-3)

    x0 = [0.0,0.0]
    f = Funkcija(3)
    postupak = Postupak(f)
    
    print("\n Postupak gradijentnog spusta uz određivanje optimalnog iznosa koraka (zlatni rez) za f3")
    postupak.Gradijentni_spust(np.array(x0), f.Racunaj_vrijednost_fje, f.Racunaj_Gradijent, koristi_zlatni_rez=True) 
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije cilja:", f.broj_pozivanja)
    print("Broj pozivanja gradijenta:", f.broj_pozivanja_gradijenta)

    f.Resetiraj()
    postupak.Resetiraj()

    print("\n Postupak gradijentnog spusta bez određivanje optimalnog iznosa koraka za f3")
    postupak.Gradijentni_spust(np.array(x0), f.Racunaj_vrijednost_fje, f.Racunaj_Gradijent, koristi_zlatni_rez=False)   
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije cilja:", f.broj_pozivanja)
    print("Broj pozivanja gradijenta:", f.broj_pozivanja_gradijenta)

    del f
    del postupak




    #ZAD2 - GRADIJENTNI SPUST I NEWTON-RAPHSON NA f1 i f2
    print("\n----ZADATAK 2-----")   #odg: min u x=(2,-3)

    x0 = [-1.9,2.0]
    f = Funkcija(1)
    postupak = Postupak(f)
    
    print("\n Postupak gradijentnog spusta uz određivanje optimalnog iznosa koraka (zlatni rez) za f1")
    postupak.Gradijentni_spust(np.array(x0), f.Racunaj_vrijednost_fje, f.Racunaj_Gradijent, koristi_zlatni_rez=True) 
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije cilja:", f.broj_pozivanja)
    print("Broj pozivanja gradijenta:", f.broj_pozivanja_gradijenta)

    f.Resetiraj()
    postupak.Resetiraj()

    print("\n Newton-Raphsonov postupak uz određivanje optimalnog iznosa koraka (zlatni rez) za f1")
    postupak.Newton_Raphson(np.array(x0), f.Racunaj_vrijednost_fje, f.Racunaj_Gradijent, f.Racunaj_Hesseovu_matricu, koristi_zlatni_rez=True)
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije cilja:", f.broj_pozivanja)
    print("Broj pozivanja gradijenta:", f.broj_pozivanja_gradijenta)
    print("Broj pozivanja Hesseove matrice:", f.broj_pozivanja_H)

    del f
    del postupak


    x0 = [0.1,0.3]
    f = Funkcija(2)
    postupak = Postupak(f)
    
    print("\n Postupak gradijentnog spusta uz određivanje optimalnog iznosa koraka (zlatni rez) za f2")
    postupak.Gradijentni_spust(np.array(x0), f.Racunaj_vrijednost_fje, f.Racunaj_Gradijent, koristi_zlatni_rez=True)  
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije cilja:", f.broj_pozivanja)
    print("Broj pozivanja gradijenta:", f.broj_pozivanja_gradijenta)

    f.Resetiraj()
    postupak.Resetiraj()

    print("\n Newton-Raphsonov postupak uz određivanje optimalnog iznosa koraka (zlatni rez) za f2")
    postupak.Newton_Raphson(np.array(x0), f.Racunaj_vrijednost_fje, f.Racunaj_Gradijent, f.Racunaj_Hesseovu_matricu, koristi_zlatni_rez=True)  
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije cilja:", f.broj_pozivanja)
    print("Broj pozivanja gradijenta:", f.broj_pozivanja_gradijenta)
    print("Broj pozivanja Hesseove matrice:", f.broj_pozivanja_H)

    del f
    del postupak



    #ZAD3 - NEWTON-RAPHSON NA f4 - bez i sa zlatnim rezom
    print("\n----ZADATAK 3-----")   #odg: min u x=(2,-3)

    x0 = [3.0,3.0]
    f = Funkcija(4)
    postupak = Postupak(f)

    print("\n Newton-Raphsonov postupak bez određivanje optimalnog iznosa koraka za f4")
    postupak.Newton_Raphson(np.array(x0), f.Racunaj_vrijednost_fje, f.Racunaj_Gradijent, f.Racunaj_Hesseovu_matricu, koristi_zlatni_rez=False)  
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije cilja:", f.broj_pozivanja)
    print("Broj pozivanja gradijenta:", f.broj_pozivanja_gradijenta)
    print("Broj pozivanja Hesseove matrice:", f.broj_pozivanja_H)

    f.Resetiraj()
    postupak.Resetiraj()

    x0 = [1.0,2.0]

    print("\n Newton-Raphsonov postupak bez određivanje optimalnog iznosa koraka za f4")
    postupak.Newton_Raphson(np.array(x0), f.Racunaj_vrijednost_fje, f.Racunaj_Gradijent, f.Racunaj_Hesseovu_matricu, koristi_zlatni_rez=False)  
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije cilja:", f.broj_pozivanja)
    print("Broj pozivanja gradijenta:", f.broj_pozivanja_gradijenta)
    print("Broj pozivanja Hesseove matrice:", f.broj_pozivanja_H)


    f.Resetiraj()
    postupak.Resetiraj()

    x0 = [3.0,3.0]

    print("\n Newton-Raphsonov postupak s određivanjem optimalnog iznosa koraka za f4")
    postupak.Newton_Raphson(np.array(x0), f.Racunaj_vrijednost_fje, f.Racunaj_Gradijent, f.Racunaj_Hesseovu_matricu, koristi_zlatni_rez=True)  
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije cilja:", f.broj_pozivanja)
    print("Broj pozivanja gradijenta:", f.broj_pozivanja_gradijenta)
    print("Broj pozivanja Hesseove matrice:", f.broj_pozivanja_H)

    f.Resetiraj()
    postupak.Resetiraj()

    x0 = [1.0,2.0]

    print("\n Newton-Raphsonov postupak s određivanjem optimalnog iznosa koraka za f4")
    postupak.Newton_Raphson(np.array(x0), f.Racunaj_vrijednost_fje, f.Racunaj_Gradijent, f.Racunaj_Hesseovu_matricu, koristi_zlatni_rez=True)  
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja funkcije cilja:", f.broj_pozivanja)
    print("Broj pozivanja gradijenta:", f.broj_pozivanja_gradijenta)
    print("Broj pozivanja Hesseove matrice:", f.broj_pozivanja_H)

    del f
    del postupak


    #ZAD4 - GAUSS NEWTON NA f1
    print("\n----ZADATAK 4-----")  

    x0 = [-1.9,2.0]
    #x0 = [-2.0,2.0]
    #x0 = [0.0,0.0]
    s = Sustav(1)
    postupak = Postupak()
    
    print("\n Gauss Newtonov postupak bez određivanje optimalnog iznosa koraka za f1")
    postupak.Gauss_Newton(np.array(x0), s.G, s.J, koristi_zlatni_rez=False) 
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja G i J:", s.broj_pozivanja_G, s.broj_pozivanja_J)

    s.Resetiraj()
    postupak.Resetiraj()

    print("\n Gauss Newtonov postupak s određivanjem optimalnog iznosa koraka za f1")
    postupak.Gauss_Newton(np.array(x0), s.G, s.J, koristi_zlatni_rez=True) 
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja G i J:", s.broj_pozivanja_G, s.broj_pozivanja_J)


    del s
    del postupak



    #ZAD5 - GAUSS NEWTON NA novi sustav
    print("\n----ZADATAK 5-----")  

    s = Sustav(2)
    postupak = Postupak()


    x0 = [-2.0,2.0]
    
    print("\n Gauss Newtonov postupak bez određivanje optimalnog iznosa koraka za s2")
    postupak.Gauss_Newton(np.array(x0), s.G, s.J, koristi_zlatni_rez=False) 
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja G i J:", s.broj_pozivanja_G, s.broj_pozivanja_J)

    s.Resetiraj()
    postupak.Resetiraj()

    print("\n Gauss Newtonov postupak s određivanjem optimalnog iznosa koraka za s2")
    postupak.Gauss_Newton(np.array(x0), s.G, s.J, koristi_zlatni_rez=True) 
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja G i J:", s.broj_pozivanja_G, s.broj_pozivanja_J)

    s.Resetiraj()
    postupak.Resetiraj()


    x0 = [2.0,2.0]
    
    print("\n Gauss Newtonov postupak bez određivanje optimalnog iznosa koraka za s2")
    postupak.Gauss_Newton(np.array(x0), s.G, s.J, koristi_zlatni_rez=False) 
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja G i J:", s.broj_pozivanja_G, s.broj_pozivanja_J)

    s.Resetiraj()
    postupak.Resetiraj()

    print("\n Gauss Newtonov postupak s određivanjem optimalnog iznosa koraka za s2")
    postupak.Gauss_Newton(np.array(x0), s.G, s.J, koristi_zlatni_rez=True) 
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja G i J:", s.broj_pozivanja_G, s.broj_pozivanja_J)

    s.Resetiraj()
    postupak.Resetiraj()


    x0 = [2.0,-2.0]
    
    print("\n Gauss Newtonov postupak bez određivanje optimalnog iznosa koraka za s2")
    postupak.Gauss_Newton(np.array(x0), s.G, s.J, koristi_zlatni_rez=False) 
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja G i J:", s.broj_pozivanja_G, s.broj_pozivanja_J)

    s.Resetiraj()
    postupak.Resetiraj()

    print("\n Gauss Newtonov postupak s određivanjem optimalnog iznosa koraka za s2")
    postupak.Gauss_Newton(np.array(x0), s.G, s.J, koristi_zlatni_rez=True) 
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja G i J:", s.broj_pozivanja_G, s.broj_pozivanja_J)


    del s
    del postupak



    #ZAD6 - GAUSS NEWTON NA novi sustav
    print("\n----ZADATAK 6-----")  

    parovi = [ [1,3], [2,4], [3,4], [5,5], [6,6], [7,8] ]  #(trenutak, promatrana vrijednost)
    #model = x1 * 1e(x2*t) + x3

    x0 = [1.0,1.0,1.0]
    
    s = Sustav(6, parovi)
    postupak = Postupak()
    
    # print("\n Gauss Newtonov postupak bez određivanje optimalnog iznosa koraka za zadani model")
    # postupak.Gauss_Newton(np.array(x0), s.G, s.J, koristi_zlatni_rez=False) 
    # print("Minimum:", postupak.minimum)
    # print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    # print("Broj pozivanja G i J:", s.broj_pozivanja_G, s.broj_pozivanja_J)

    # s.Resetiraj()
    # postupak.Resetiraj()

    print("\n Gauss Newtonov postupak s određivanjem optimalnog iznosa koraka za zadani model")
    postupak.Gauss_Newton(np.array(x0), s.G, s.J, koristi_zlatni_rez=True) 
    print("Minimum:", postupak.minimum)
    print("Vrijednost funkcije cilja u toj točki:", postupak.vrijednost_fje_u_min)
    print("Broj pozivanja G i J:", s.broj_pozivanja_G, s.broj_pozivanja_J)

    del s
    del postupak
