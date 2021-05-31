##RÉSOLUTION DE L'ÉQUATION DE LA CHALEUR 2D



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation



#Initialisation des constantes et des variables

Lx = 80                 #Longueur de la plaque
Ly = 40                 #Largeur de la plaque
K = 15                  #Coefficient de diffusion thermique
dx = 1                  #Pas spatial
dt = (dx ** 2)/(4 * K)  #Pas temporel
nbi = 100               #Nombre d'itérations temporelles

Tci = 0     #Condition initiale (température initiale sur toute la plaque)
Tcl1 = 100  #Condition à la limite supérieure de la plaque
Tcl2 = 100    #Condition à la limite inférieure de la plaque
Tcl3 = 0  #Condition à la limite droite de la plaque
Tcl4 = 0    #Condition à la limite gauche de la plaque

T0 = np.zeros((nbi, Ly, Lx))    #Création du tableau de conditions initiales
T0[:, :, :] = Tci
T0[:, (Ly-1):, :] = Tcl1
T0[:, :1, :] = Tcl2
T0[:, :, (Lx-1):] = Tcl3
T0[:, :, :1] = Tcl4



#Création d'une fonction qui retourne le tableau des solutions en appliquant la méthode des différences finies

def mdf(y):
    for k in range(0, nbi-1):
        for i in range(1, Ly-1, dx):
            for j in range(1, Lx-1, dx):
                y[k + 1, i, j] = (K*dt/dx**2) * (y[k][i+1][j] + y[k][i-1][j] + y[k][i][j+1] + y[k][i][j-1] - 4*y[k][i][j]) + y[k][i][j]
    return y



#Création du tableau des solutions

T = mdf(T0)



#Plot (Image finale)

X, Y = np.meshgrid(np.arange(0, Lx), np.arange(0, Ly))
plt.contourf(X, Y, T[nbi-1, :, :], 50, cmap = plt.cm.inferno, vmin=0, vmax=100)
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Température à t = {(nbi-1)*dt:.1f} s")
plt.show()



#Plot (Animation)

fig = plt.figure()  #Création d'une nouvelle figure

def animate(k):     #Création d'une fonction qui permet de plot la température au temps k
    plt.clf()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Température à t = {k*dt:.1f} s")
    plt.pcolormesh(T[k, :, :], cmap = plt.cm.inferno, vmin=0, vmax=100)
    plt.colorbar()
    return plt

anim = animation.FuncAnimation(fig, animate, frames = nbi, interval = dt*1000, repeat = True) #Appel de la méthode qui permet d'afficher successivement chaque image créée par la fonction animate

#anim.save("Équation_de_la_chaleur.gif")

plt.show()
