
class Ogranicenje:

    def __init__(self, broj_ogr):

        self.broj_ogr = broj_ogr
        
    def Provjeri_ogranicenje(self, x=[]):

        if self.broj_ogr == 1:
            x1= x[0]
            x2 = x[1]
            return x2-x1

        elif self.broj_ogr == 2:
            x1= x[0]
            x2 = x[1]
            return 2-x1



        elif self.broj_ogr == 3:
            x1= x[0]
            x2 = x[1]
            return 3-x1-x2

        elif self.broj_ogr == 4:
            x1= x[0]
            x2 = x[1]
            return 3+1.5*x1-x2

        #ogranicenje jednakosti
        elif self.broj_ogr == 5:
            x1= x[0]
            x2 = x[1]
            return x2-1


    def __del__(self):
        return
