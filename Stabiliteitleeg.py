import pandas as pd
import numpy as np
from scipy import integrate, interpolate

rho_staal = 7.85E3
E_staal=210E9
rho_water = 1.025E3
g = 9.81
tp_factor=1
df = pd.read_excel("IP.xlsx",'VB schip van Goris')
df = df.round(4)
nul = np.zeros(1)
Loa= df.iloc[0,1] +df.iloc[67,0]
eind = np.array([Loa])
onderwater= df.iloc[42:64,0]

x=np.arange(0,Loa,0.05)

#opwaartsekracht verdeelde belasting
p=np.zeros(len(x))

p = -df.iloc[42:64,1]*rho_water*g
p = np.append(p,nul)
p = np.append(nul,p)
x_p = df.iloc[42:64,0]
x_p = np.append(0,x_p)
x_p = np.append(x_p,max(onderwater))
p_func = interpolate.interp1d(x_p,p)

#gewicht verdeelde belasting
G = df.iloc[101:123,2]*rho_staal*g*tp_factor
#G=np.append(G,nul)
x_G = df.iloc[101:123,0]
#x_G=np.append(x_G,eind)
G_func = interpolate.interp1d(x_G,G)

#traagheidsmoment over de lengte
I = df.iloc[101:123,6]*tp_factor
#I=np.append(I,nul)
x_I = df.iloc[101:123,0]
#x_I=np.append(x_I,eind)
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

#Som van de krachten
G_punt=integrate.quad(G_func,0,Loa)
P_punt=integrate.quad(p_func,min(onderwater),max(onderwater))
print(G_punt[0]+P_punt[0])