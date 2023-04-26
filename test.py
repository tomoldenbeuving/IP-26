import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import matplotlib.pyplot as plt

rho_staal = 7.85E3
rho_water = 1.025E3
g = 9.811

df = pd.read_excel("IP.xlsx")
df = df.round(4)

p = df.iloc[42:64,1]*rho_water*g
x_p = df.iloc[42:64,0]
p_func = interpolate.interp1d(x_p,p,fill_value=0)



G = -df.iloc[97:119,2]*rho_staal*g
x_G = df.iloc[97:119,0]
G_func = interpolate.interp1d(x_G,G)

x = np.arange(0.0,147.0,0.05)


p = p_func(x)
G = G_func(x)

q= p+G

V = integrate.cumtrapz(x,q,initial=0)

def plot(x,y):
    plt.plot(x,y)
    plt.grid()
    plt.show()


