import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import matplotlib.pyplot as plt

rho_staal = 7.85E3
E_staal=210000E6
rho_water = 1.025E3
g = 9.811
df = pd.read_excel("IP.xlsx")
df = df.round(4)
nul = np.zeros(1)
Loa= df.iloc[0,1]
eind = np.array([Loa])

p = df.iloc[42:64,1]*rho_water*g
p = np.append(nul,p)
p = np.append(p,nul)
x_p = df.iloc[42:64,0]
x_p = np.append(nul,x_p)
x_p = np.append(x_p,eind)
p_func = interpolate.interp1d(x_p,p,fill_value=0)



G = -df.iloc[97:119,2]*rho_staal*g
G = np.append(nul,G)
G = np.append(G,nul)
x_G = df.iloc[97:119,0]
x_G = np.append(nul,x_G)
x_G = np.append(x_G,eind)
G_func = interpolate.interp1d(x_G,G)

I = df.iloc[97:119,6]
I = np.append(nul,I)
I = np.append(I,nul)
x_I = df.iloc[97:119,0]
x_I = np.append(nul,x_I)
x_I = np.append(x_I,eind)
I_func = interpolate.interp1d(x_I,I)


x = np.arange(0.0,Loa,0.5)


p = p_func(x)
G = G_func(x)
I= I_func(x)




#index=[np.arange(0,1)]

#I=np.delete(I_func(x),index)

q= p+G

V = integrate.cumtrapz(x,q,initial=0)
M = integrate.cumtrapz(x,V,initial=0)
phiEI=(integrate.cumtrapz(x,M,initial=0))


#plt.plot(x,phi)
phi=np.zeros(len(x))
for i in range(len(x)):
    if phiEI[i] == 0 or I[i] == 0:
        phi[i]= 0
    else:
        phi[i]=phiEI[i]/(E_staal*I[i])
   

plt.plot(x,phi)
def plotp():
    plt.plot(x,p)
    plt.xlabel('L.O.A. [m]')
    plt.ylabel('Opwaartsekracht (p) [N]')
    plt.title('Opwaartsekracht uitgezet tegen de totale lengte')
    plt.grid()
    plt.show()
    return plotp

def plotG():
    plt.plot(x,G)
    plt.xlabel('L.O.A. [m]')
    plt.ylabel('Zwaartekracht (G) [N]')
    plt.title('Zwaartekracht uitgezet tegen de totale lengte')
    plt.grid()
    plt.show()
    return plotG

def plotq():
    plt.plot(x,q)
    plt.xlabel('L.O.A. [m]')
    plt.ylabel('Nettobelasting (q) [N]')
    plt.title('Nettobelasting uitgezet tegen de totale lengte')
    plt.grid()
    plt.show()
    return plotq
    
def dwarskrachtlijn():
    plt.plot(x,V)
    plt.xlabel('L.O.A. [m]')
    plt.ylabel('Dwarskracht (V) [N]')
    plt.title('Dwarskracht uitgezet tegen de totale lengte')
    plt.grid()
    plt.show()
    return dwarskrachtlijn

def momentlijn():
    plt.plot(x,M)
    plt.xlabel('L.O.A. [m]')
    plt.ylabel('Moment (M) [Nm]')
    plt.title('Intern moment uitgezet tegen de totale lengte')
    plt.grid()
    plt.show()
    return momentlijn



