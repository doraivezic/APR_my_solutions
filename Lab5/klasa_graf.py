import matplotlib.pyplot as plt
import numpy as np

class Graf:

    def __init__(self, T, t_max):
        self.T = T
        self.t_max = t_max


    def Nacrtaj(self, liste, imena, broj_zadatka):

        fig, axs = plt.subplots(3,2)
        fig.suptitle('Zadatak'+str(broj_zadatka))
        fig.set_size_inches(16, 12)
        fig.tight_layout(pad=5.0)

        for i in range(len(liste)):

            lista_rez = np.array(liste[i])
            column1 = lista_rez[:,0]
            column2 = lista_rez[:,1]

            # plotting the points 
            axs[i%3,i%2].plot(np.arange(0, self.t_max + self.T, self.T), column1, label="x1", color="red")
            axs[i%3,i%2].plot(np.arange(0, self.t_max + self.T, self.T), column2, label="x2", color='yellow')
        
            # naming the x axis
            axs[i%3,i%2].set(xlabel='vrijeme', ylabel='vr. var. stanja')
            
            # giving a title to my graph
            axs[i%3,i%2].set_title(imena[i])
            axs[i%3,i%2].legend(loc="best")
        
        # function to show the plot
        #plt.show()
        plt.savefig('grafovi_zadatak'+str(broj_zadatka)+'.png')

        return