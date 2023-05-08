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

#containers
Cl=6.06   #container lengte
Cb=2.44  #container breedte
Ch=2.59   #container hoogte
Cw=30E3  #container weight


p = df.iloc[42:64,1]*rho_water*g
x_p = df.iloc[42:64,0]
p = np.append(nul,p)
p = np.append(p,nul)
p_func = interpolate.interp1d(x_p,p)


G = -df.iloc[97:119,2]*rho_staal*g
x_G = df.iloc[97:119,0]
G_func = interpolate.interp1d(x_G,G)


I = df.iloc[97:119,6]
x_I = df.iloc[97:119,0]
I_func = interpolate.interp1d(x_I,I)
G = G_func(x)
I= I_func(x)


#test

#index=[np.arange(0,1)]

#I=np.delete(I_func(x),index)

q= p+G

V = integrate.cumtrapz(x,q,initial=0)
M = integrate.cumtrapz(x,V,initial=0)
phiEI=(integrate.cumtrapz(x,M,initial=0))


phi=np.zeros(len(x))
for i in range(len(x)):
    if phiEI[i] == 0 or I[i] == 0:
        phi[i]= 0
    else:
        phi[i]=phiEI[i]/(E_staal*I[i])
   

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

    def alles():
        plt.figure(figsize=(16,9))
        plt.plot(x,q)
        plt.plot(x,G)
        plt.plot(x,p)

        
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



LCB = df.iloc[20,1]
LCF = df.iloc[26,1]
#GM dwarsrichting
It_x = df.iloc[27,1]
displacement = df.iloc[18,1]
BM_t = It_x/displacement
KB = df.iloc[20,3]
KG = df.iloc[26,3]

GM = KB + BM - KG 

#GM langsrichting
It_y = df.iloc[27,2]
BM_l = It_y/displacement
GM_l = KB +BM_l-KG

