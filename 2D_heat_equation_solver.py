#!/usr/bin/env python3
# coding: utf-8

'''
Programme pour résoudre l'équation de la chaleur par la méthodes des différences finies
'''

__author__ = 'Nathan Zimniak'


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import time
start_time = time.time()



#Initialisation des constantes
Lx = 81                 #Longueur spatiale
Ly = 41                 #Largeur spatiale
Nbi = 100               #Nombre d'itérations temporelles
dx = 1                  #Pas spatial suivant x
dy = 1                  #Pas spatial suivant y
dt = 0.01               #Pas temporel
K = 15                  #Coefficient de diffusion thermique



#Création du tableau des solutions
T0 = np.zeros((Nbi, Ly, Lx))
Tci = 0                     #Condition initiale (température initiale sur toute la plaque)
Tcl1 = 100                  #Condition à la limite supérieure de la plaque
Tcl2 = 100                  #Condition à la limite inférieure de la plaque
Tcl3 = 100                  #Condition à la limite droite de la plaque
Tcl4 = 100                  #Condition à la limite gauche de la plaque
T0[:, :, :] = Tci
T0[:, :1, :] = Tcl1
T0[:, (Ly-1):, :] = Tcl2
T0[:, :, (Lx-1):] = Tcl3
T0[:, :, :1] = Tcl4



def finite_difference_method(Z):
    ''' Calcule la fonction d'onde pour chaque itération temporelle
        ----------
        :param Z: 3D array, tableau des solutions vide
        :return: Z, tableau des solutions
        ----------
    '''
    for k in range(0, Nbi-1):
        for i in range(1, Ly-1):
            for j in range(0, Lx-1):
                Z[k + 1, i, j] = Z[k][i][j] + K * dt * ((Z[k][i+1][j] + Z[k][i-1][j] - 2*Z[k][i][j])/dx**2  + (Z[k][i][j+1] + Z[k][i][j-1] - 2*Z[k][i][j])/dy**2)
    return Z



T = finite_difference_method(T0)



#Affiche le résultat

#Plot (Image 2D)

##plt.style.use('dark_background')
##plt.figure()
##X, Y = np.meshgrid(np.arange(0, Lx), np.arange(0, Ly))
##imageNbi = Nbi-1
##plt.contourf(X, Y, T[imageNbi, :, :], 100, cmap = plt.cm.inferno)
##plt.colorbar()
##plt.xlabel("x")
##plt.ylabel("y")
##plt.title("Température à t = " + str(round(imageNbi*dt,2)) + " s")
##plt.savefig('2D_Heat_Equation.png')



#Plot (Animation 2D)

##plt.style.use('dark_background')
##fig = plt.figure()
##
##def animate(k):
##    plt.clf()
##    plt.pcolormesh(T[k, :, :], cmap = plt.cm.inferno)
##    plt.colorbar()
##    plt.xlabel("x")
##    plt.ylabel("y")
##    plt.title(f"Température à t = {k*dt:.2f} s")
##    return
##
##anim = animation.FuncAnimation(fig, animate, frames = int(Nbi), interval = 50, repeat = True)
##
###plt.rcParams['animation.ffmpeg_path'] = 'C:\\ffmpeg\\bin\\ffmpeg.exe'
###Writer = animation.writers['ffmpeg']
###writermp4 = Writer(fps=30, bitrate=1800)
###anim.save("2D_Heat_Equation.mp4", writer=writermp4)
##writergif = animation.PillowWriter(fps=30)
##writergif.setup(fig, "2D_Heat_Equation.gif")
##anim.save("2D_Heat_Equation.gif", writer=writergif)



###Plot (Image 3D)
##    
##plt.style.use('dark_background')
##fig = plt.figure()
##ax = plt.axes(projection = '3d')
##X, Y = np.meshgrid(np.arange(0, Lx), np.arange(0, Ly))
##imageNbi = Nbi-1
##surf = ax.plot_surface(X, Y, T[imageNbi, :, :], cmap=plt.cm.inferno)
##ax.set_xlabel("x")
##ax.set_ylabel("y")
##ax.set_zlabel("T (K)")
##ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
##ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
##ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
##ax.grid(False)
##plt.title("Température à t = " + str(round(imageNbi*dt,2)) + " s")
##plt.savefig('3D_Heat_Equation.png')



#Plot (Animation 3D)

plt.style.use('dark_background')
fig = plt.figure()
ax = plt.axes(projection = '3d')
X, Y = np.meshgrid(np.arange(0, Lx), np.arange(0, Ly))

def Animate3D(k):
    ax.clear()
    ax.set_zlim3d(0, np.max(T))
    ax.plot_surface(X, Y, T[k, :, :], cmap=plt.cm.inferno)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("T (K)")
    #fig.set_facecolor('black')
    #ax.set_facecolor('black')
    ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.grid(False)
    plt.title(f"Température à t = {k*dt:.2f} s")
    ax.view_init(azim=k)
    return

anim3D = animation.FuncAnimation(fig, Animate3D, frames = int(Nbi), interval = 50, blit = False, repeat = True)

##plt.rcParams['animation.ffmpeg_path'] = 'C:\\ffmpeg\\bin\\ffmpeg.exe'
##Writer = animation.writers['ffmpeg']
##writermp4 = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)
##anim3D.save("3D_Schrodinger_Equation.mp4", writer=writermp4)
writergif = animation.PillowWriter(fps=30)
anim3D.save("3D_Heat_Equation.gif", writer=writergif)



print("%s secondes" % (time.time() - start_time))
plt.show()
