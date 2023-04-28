import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import matplotlib.pyplot as plt

rho_staal = 7.85E3
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

x = np.arange(0.0,Loa,0.05)


p = p_func(x)
G = G_func(x)

q= p+G

V = integrate.cumtrapz(x,q,initial=0)

def plot(x,y):
    plt.plot(x,y)
    plt.grid()
    plt.show()


