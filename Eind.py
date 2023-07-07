import matplotlib.pyplot as plt
from Sterkteleerbeladen import x,p,G,q,V,M,theta,v,sigma,tanklast,vb_cont,vb_last
from Stabiliteitvarend import V_s, R_tot
import numpy as np

class plot():

    def vb():
        figure = plt.figure(figsize=(10,15))
        ax = plt.subplot(111)
        plt.plot(x,-q,label="Totale belasting")
        plt.plot(x,-p,'--',label="Buoancy")
        plt.plot(x,-G,'--',label="Gewicht")
        plt.plot(x,-vb_cont,'--',label="Containers")
        plt.plot(x,-tanklast,'--',label="Balasttank")
        plt.plot(x,-vb_last,'--',label="Last")
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('Nettobelasting (q) [N/m]')
        plt.title('Belasting uitgezet tegen de totale lengte')
        plt.grid()
        plt.legend()
        # Shrink current axis's height by 10% on the bottom
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1,
                        box.width, box.height * 0.9])

        # Put a legend below current axis
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
                fancybox=True, shadow=True, ncol=3)
        plt.show()
 
    def V():
        figure = plt.figure(figsize=(10,12))
        plt.plot(x,-V)
        plt.xlabel(r'$L_{oa} [m]$')
        plt.ylabel(r'$Dwarskracht \;(V) [N]$')
        plt.title(r'Dwarskracht uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def M():
        figure = plt.figure(figsize=(10,12))
        plt.plot(x,M)
        plt.xlabel(r'$L_{oa} [m]$')
        plt.ylabel(r'$Moment\; (M) [Nm]$')
        plt.title(r'Intern moment uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def theta():
        figure = plt.figure(figsize=(10,12))
        plt.plot(x,theta)
        plt.xlabel(r'$L_{oa} [m]$')
        plt.ylabel(r'$Hoekverdraaiing\; (\theta)[rad]$')
        plt.title(r'Hoekverdraaiing uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()
    def v():
        figure = plt.figure(figsize=(10,12))
        plt.plot(x,v)
        plt.xlabel(r'$L_{oa} [m]$')
        plt.ylabel(r'$Doorbuiging \; (v) [m]$')
        plt.title(r'Doorbuiging uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()
  
    def sigma():
        figure = plt.figure(figsize=(10,12))
        plt.plot(x,sigma)
        plt.xlabel(r'$L_{oa} [m]$')
        plt.ylabel(r'$Spanningsverdeling \; (\sigma) [m]$')
        plt.title(r'Spanningsverdeling uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()
    def R_tot():
        figure = plt.figure(figsize=(10,12))
        plt.plot(V_s,R_tot)
        plt.xlabel(r'$v_{s} [ms^{-1}]$')
        plt.ylabel(r'$R_{tot}[N]$')
        plt.title(r'Totale scheepsweerstand uitgezet over de snelheid')
        plt.grid()
        plt.show()        

plot.vb()
