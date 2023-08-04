from klasa_postupci import Postupak
from klasa_matrica import Matrica
from klasa_graf import Graf
import numpy as np


def Rijesi_sve_postupke(broj_zadatka, T, t_max, r=None, ispis=None, racunaj_greske=False, crtaj = True):

    if broj_zadatka not in range(1,5):
        return

    file_A = "zad" + str(broj_zadatka) + "_matrica_A.txt"
    file_B = "zad" + str(broj_zadatka) + "_matrica_B.txt"
    file_x0 = "zad" + str(broj_zadatka) + "_matrica_x0.txt"

    o = open(file_A, "r")
    lines = o.readlines()
    o.close()
    A = Matrica(lines)
    #A.Ispisi_matricu()

    o = open(file_x0, "r")
    lines = o.readlines()
    o.close()
    x0 = Matrica(lines)
    #x0.Ispisi_matricu()

    try:
        o = open(file_B, "r")
        lines = o.readlines()
        o.close()
        B = Matrica(lines)
    except:
        B = None

    try:
        o = open("ucestalost_ispisa.txt", "r")
        lines = o.readlines()
        o.close()
        ispis = int(lines[0])
    except:
        if ispis is None:
            ispis = 10

    postupak = Postupak(T, t_max, A, B, x0, r, ispis)

    l1 = np.array(postupak.Runge_Kutta())
    l2 = np.array(postupak.Trapez())
    l3 = np.array(postupak.Euler())
    l4 = np.array(postupak.Obrnuti_Euler())
    l5 = np.array(postupak.Prediktorsko_korektorski( prediktor = postupak.Euler, korektor=postupak.Obrnuti_Euler, S=2))
    postupak.x0 = x0
    postupak.ispis = ispis
    l6 = np.array(postupak.Prediktorsko_korektorski( prediktor = postupak.Euler, korektor=postupak.Trapez, S=1))

    if racunaj_greske:

        #racunaj stvarno rijesenje u svakoj tocki integracije
        l = []
        for i in range( int(t_max / T) + 1 ):
            x1 = np.cos(T*i) + np.sin(T*i)
            x2 = np.cos(T*i) - np.sin(T*i)
            l.append( [[x1], [x2]] )


        #racunaj apsolutnu razliku izmedu l i l_i
        l = np.array(l)

        print("\nKumulativna apsolutna razlika za svaki postupak")

        print("Runge_Kutta: ", np.sum( np.abs(l - l1) ))
        print("Trapez: ", np.sum( np.abs(l - l2) ))
        print("Euler: ", np.sum( np.abs(l - l3) ))
        print("Obrnuti euler: ", np.sum( np.abs(l - l4) ))
        print("Prediktorsko_korektorski Euler, obrnuti Euler, S=2: ", np.sum( np.abs(l - l5) ))
        print("Prediktorsko_korektorski Euler, trapez, S=1: ", np.sum( np.abs(l - l6) ))


    if crtaj:
        g = Graf(T, t_max)
        g.Nacrtaj( [l1, l2, l3, l4, l5, l6], ["Runge-Kutta", "Trapez", "Euler", "Obrnuti Euler", "PE(CE)^2", "PECE"], broj_zadatka=broj_zadatka)
        

    return




if __name__=="__main__":

    zadatak1 = True
    zadatak2 = False
    zadatak3 = False
    zadatak4 = False

    if zadatak1:
        print("\n----ZADATAK 1-----")

        T = 0.01
        t_max = 10

        Rijesi_sve_postupke( 1, T, t_max, racunaj_greske=True, crtaj=True, ispis=100 )



    if zadatak2:
        print("\n\n----ZADATAK 2-----")

        # T = 0.1
        # t_max = 1

        # Rijesi_sve_postupke( 2, T, t_max, ispis=10 )


        #prikladni korak integracije
        T = 0.02
        t_max = 1

        Rijesi_sve_postupke( 2, T, t_max, ispis=10)


    if zadatak3:
        print("\n----ZADATAK 3-----")

        T = 0.01
        t_max = 10

        Rijesi_sve_postupke( 3, T, t_max, lambda t : Matrica([[1],[1]]), ispis=100)



    if zadatak4:
        print("\n----ZADATAK 4-----")

        T = 0.01
        t_max = 1

        Rijesi_sve_postupke( 4, T, t_max, lambda t : Matrica([[t],[t]]), ispis=10)