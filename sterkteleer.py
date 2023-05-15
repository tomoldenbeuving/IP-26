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

#Ballast tank
V_tank=df.iloc[32,1]
G_tank=V_tank*rho_water
arm_tank= df.iloc[34,1] 

tank = df.iloc[92:97,1]*rho_water*g*df.iloc[35,1]/100
x_tank = df.iloc[92:97,0]
tank_func=interpolate.interp1d(x_tank,tank)

tanklast=np.zeros(len(x))



for i in range(len(x)):
    if x[i] > min(x_tank) and x[i] < max(x_tank):
        tanklast[i]= tank_func(x[i])
    else:
        tanklast[i] = 0



#last op platfrom uitrekenen	
from container import G_cont
#som van de krachten
G_punt=sum(G)
P_punt=sum(p)
F_c=G_cont
F_tank=sum(tanklast)

F_last = -P_punt + -G_punt + -F_c + -F_tank

print(F_last/(P_punt+G_punt+F_c+F_tank))


#tijdelijke last
#F_last = 99399464.7


# som van momenten
x_tank = df.iloc[33,1]
x_last = 13.5
COB = df.iloc[20,1]
COV = df.iloc[21,1]

arm_c = (P_punt*COB-G_punt*COV-F_tank*x_tank-F_last*x_last)/F_c




x_platform=[11.8,16.2]
F_last_overlengte=F_last/(x_platform[1]-x_platform[0])

vb_last=np.zeros(len(x))

for i in range(len(x)):
    if x[i] > min(x_platform) and x[i] < max(x_platform):
        vb_last[i] = F_last_overlengte
    else:
        vb_last[i]= 0      



q= p+G+G_containerschip*g+tanklast+vb_last

# integratie lijnen
V = integrate.cumtrapz(q,x,initial=0) 
M = integrate.cumtrapz(V,x,initial=0)
phiEI=(integrate.cumtrapz(M,x,initial=0))
vEI=(integrate.cumtrapz(phiEI,x,initial=0))


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
        v[i]=vEI[i]/(E_staal*I[i])


# Maximaal toelaatbaar moment
sigma_max=190E6
I_midship=df.iloc[114, 7]
H=df.iloc[2,1]
KG_y=df.iloc[21,3]
y=H-KG_y

moment_max=(sigma_max*I_midship)/y



