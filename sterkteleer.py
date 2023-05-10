#%%
import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import matplotlib.pyplot as plt
from container import G_containerschip

rho_staal = 7.85E3
E_staal=210E9
rho_water = 1.025E3
g = 9.81
tp_factor=1
df = pd.read_excel("IP.xlsx",'VB schip van Goris')
df = df.round(4)
nul = np.zeros(1)
Loa= df.iloc[0,1]
eind = np.array([Loa])
onderwater= df.iloc[42:64,0]

x=np.arange(0,Loa,0.5)

p=np.zeros(len(x))

p = -df.iloc[42:64,1]*rho_water*g
p = np.append(p,nul)
p = np.append(nul,p)
x_p = df.iloc[42:64,0]
x_p = np.append(0,x_p)
x_p = np.append(x_p,max(onderwater))


p_func = interpolate.interp1d(x_p,p)


G = df.iloc[101:123,2]*rho_staal*g*tp_factor
G=np.append(G,nul)
x_G = df.iloc[101:123,0]
x_G=np.append(x_G,eind)
G_func = interpolate.interp1d(x_G,G)


I = df.iloc[101:123,6]*tp_factor
I=np.append(I,nul)

x_I = df.iloc[101:123,0]
x_I=np.append(x_I,eind)
I_func = interpolate.interp1d(x_I,I)


G = G_func(x)
I= I_func(x)
p= np.zeros(len(x))

# for loop zodat nadat het onderwater stopt p altijd 0
for i in range(len(x)):
    if x[i] < min(onderwater):
        p[i] = 0
    elif x[i] > max(onderwater):
        p[i]=0
    else:
        p[i]=p_func(x[i])

#index=[np.arange(0,1)]

#I=np.delete(I_func(x),index)

q= p+G+G_containerschip
# integratie lijnen
V = integrate.cumtrapz(x,q,initial=0) 
M = integrate.cumtrapz(x,V,initial=0)
phiEI=(integrate.cumtrapz(x,M,initial=0))
vEI=(integrate.cumtrapz(x,phiEI,initial=0))

plt.plot(x,V)
phi=np.zeros(len(x))
# for loop zodat elke de waardes van het traagheidsmoment die nul zijn niet worden gebruikt om door te delen

for i in range(len(x)):
    if I[i] == 0:
        phi[i]= 0
    else:
        phi[i]=phiEI[i]/(E_staal*I[i])

v=np.zeros(len(x))
for i in range(len(x)):
    if I[i] == 0:
        v[i]= 0
    else:
        v[i]=phiEI[i]/(E_staal*I[i])


# Maximaal toelaatbaar moment
sigma_max=190E6
I_midship=df.iloc[114, 7]
H=df.iloc[2,1]
KG_y=df.iloc[21,3]
y=H-KG_y

moment_max=(sigma_max*I_midship)/y

#Ballast tank
V_tank=df.iloc[32,1]
G_tank=V_tank*rho_water
arm_tank=  


