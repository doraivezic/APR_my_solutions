from klasa_matrica import Matrica 
from klasa_metode import Metode




def Rijesi_sustav(file_A, file_b, koristi_LUP = False, epsilon = None):

    o = open(file_A, "r")
    lines = o.readlines()
    o.close()
    A= Matrica(lines)
    #A.Ispisi_matricu()

    o = open(file_b, "r")
    lines = o.readlines()
    o.close()
    b = Matrica(lines)
    #b.Ispisi_matricu()
    b_copy = Matrica(lines)

    m = Metode(A, epsilon)
    
    
    
    LU = m.LU_dekompozicija()
    try:
        LU.Ispisi_matricu()
        print("Uspješna LU dekompozicija.")
        #b ce nam ostati isti
    except:
        print("LU dekompozicija nije uspjela.")   
        #probati cemo i sa LUP 

    if LU is not None:
        b = m.Supstitucija_unaprijed(b,False)
        try:
            b.Ispisi_matricu()
            print("Uspješna supstitucija unaprijed uz LU dekompoziciju.")
        except:
            print("Neuspješna supstitucija unaprijed uz LU dekompoziciju.")

        b = m.Supstitucija_unatrag(b,False)
        try:
            b.Ispisi_matricu()
            print("Uspješna supstitucija unatrag uz LU dekompoziciju.")
        except:
            print("Neuspješna supstitucija unatrag uz LU dekompoziciju.")

    
    if LU is None or koristi_LUP or b is None:

        LUP, P = m.LUP_dekompozicija()
        try:
            LUP.Ispisi_matricu()
            print("Uspješna LUP dekompozicija.")
        except:
            print("LUP dekompozicija nije uspjela.")

        if LUP is not None:

            # P*b šaljemo u supstituciju unatrag i unaprijed
            b = Matrica()
            b = P*b_copy
            b = m.Supstitucija_unaprijed(b)
            try:
                b.Ispisi_matricu()
                print("Uspješna supstitucija unaprijed uz LUP dekompoziciju.")
            except:
                print("Neuspješna supstitucija unaprijed uz LUP dekompoziciju.")

            b = m.Supstitucija_unatrag(b)
            try:
                b.Ispisi_matricu()
                print("Uspješna supstitucija unatrag uz LUP dekompoziciju.")
            except:
                print("Neuspješna supstitucija unatrag uz LUP dekompoziciju.")


    if b is not None:
        b.Spremi_matricu(file_A[:5]+"output.txt")
    else:
        b = Matrica()
        b.Spremi_matricu(file_A[:5]+"output.txt")

    return






def Izracunaj_inverz(file_A):

    o = open(file_A, "r")
    lines = o.readlines()
    o.close()
    A= Matrica(lines)
    #A.Ispisi_matricu()

    m = Metode(A)
    A_inverz = m.Inverz()

    try:
        A_inverz.Ispisi_matricu()
    except:
        print("Ne postoji inverz matrice A.")

    if A_inverz is not None:
        A_inverz.Spremi_matricu(file_A[:5]+"output.txt")
    else:
        b = Matrica()
        b.Spremi_matricu(file_A[:5]+"output.txt")

    return

def Izracunaj_determinantu(file_A):

    o = open(file_A, "r")
    lines = o.readlines()
    o.close()
    A= Matrica(lines)
    #A.Ispisi_matricu()

    m = Metode(A)
    det_A = m.Determinanta()

    print("Determinanta matrice A iznosi",det_A)

    f = open(file_A[:6]+"output.txt", "w")
    f.write(str(det_A))
    f.close()

    return






if __name__=="__main__":


    #zad1
    #pomnoziti i podijeliti M sa realnim brojem i usporediti s početnim M
    print("\n----ZADATAK 1-----")

    o = open("zad1_input_A.txt", "r")
    lines = o.readlines()
    o.close()
    M = Matrica(lines)  #upisujem elemete iz tesktovne datoteke u matricu
    #M.Ispisi_matricu()

    C = M * 0.2 / 0.2
    C.Ispisi_matricu()
    C.Spremi_matricu("zad1_output.txt")

    if C == M:
        print("isti su")
    else:
        print("nisu isti")

    del C
    del M



    #zad2
    #sustav Ax = b, trazi se x
    print("\n----ZADATAK 2-----")
    Rijesi_sustav("zad2_input_A.txt", "zad2_input_b.txt")
    
    #zad3
    print("\n----ZADATAK 3-----")
    Rijesi_sustav("zad3_input_A.txt", "zad3_input_b.txt")
    
    #zad4
    print("\n----ZADATAK 4-----")
    Rijesi_sustav("zad4_input_A.txt", "zad4_input_b.txt", True)
    
    #zad5
    print("\n----ZADATAK 5-----")
    Rijesi_sustav("zad5_input_A.txt", "zad5_input_b.txt")

    #zad6
    print("\n----ZADATAK 6-----")
    Rijesi_sustav("zad6_input_A.txt", "zad6_input_b.txt", epsilon=-6)




    #zad7
    print("\n----ZADATAK 7-----")
    Izracunaj_inverz("zad7_input_A.txt")

    #zad8
    print("\n----ZADATAK 8-----")
    Izracunaj_inverz("zad8_input_A.txt")
    



    #zad9
    print("\n----ZADATAK 9-----")
    Izracunaj_determinantu("zad9_input_A.txt")

    #zad10
    print("\n----ZADATAK 10-----")
    Izracunaj_determinantu("zad10_input_A.txt")
