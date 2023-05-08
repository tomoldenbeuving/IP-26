#%%
import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import matplotlib.pyplot as plt

rho_staal = 7.85E3
E_staal=210E9
rho_water = 1.025E3
g = 9.81
tp=0.008
df = pd.read_excel("IP.xlsx",'VB schip van Goris')
df = df.round(4)
nul = np.zeros(1)
Loa= df.iloc[0,1]
eind = np.array([Loa])
onderwater= df.iloc[42:64,0]

x=np.arange(0,Loa,0.5)



#plots in een class runnen met plot.q() om bijv q te ploten
class plot():
    def p():
        plt.plot(x,p)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('Opwaartsekracht (p) [N/m]')
        plt.title('Opwaartsekracht uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def G():
        plt.plot(x,G)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('Zwaartekracht als verdeelde belasting (G) [N/m]')
        plt.title('Zwaartekracht uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def q():
        plt.plot(x,q)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('Nettobelasting (q) [N/m]')
        plt.title('Nettobelasting uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    

        
    def V():
        plt.plot(x,V)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('Dwarskracht (V) [N]')
        plt.title('Dwarskracht uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def M():
        plt.plot(x,M)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('Moment (M) [Nm]')
        plt.title('Intern moment uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def phi():
        plt.plot(x,phi)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('hoekverdraaing (phi) [radialen]')
        plt.title('de hoekverdraaing')
        plt.grid()
        plt.show()
    def v():
        plt.plot(x,v)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('doorbuiging (v) [m]')
        plt.title('doorbuiging')
        plt.grid()
        plt.show()
    def alles():
        plt.figure(figsize=(16,9))
        plt.plot(x,q)
        plt.plot(x,G)
        plt.plot(x,p)
        plt.plot(x,phi)
        plt.plot(x,v)
        plt.plot(x,M)

#momentstelling stabiliteit


LCB = df.iloc[20,1]
LCF = df.iloc[26,1]
#GM dwarsrichting
It_x = df.iloc[27,1]
displacement = df.iloc[18,1]
BM_t = It_x/displacement
KB = df.iloc[20,3]
KG = df.iloc[26,3]

GM = KB + BM_t - KG 

#GM langsrichting
It_y = df.iloc[27,2]
BM_l = It_y/displacement
GM_l = KB +BM_l-KG

#Kritische belasting moment
n=234
G_cont=n*Cw*g
sigma_max=190E6
M_cont=
