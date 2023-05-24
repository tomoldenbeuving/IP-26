import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import matplotlib.pyplot as plt
from imports import df_varend, tp_factor


rho_staal = 7.85E3
E_staal=210E9
rho_water = 1.025E3
g = 9.81
nul = np.zeros(1)
Loa= df_varend.iloc[0,1] +df_varend.iloc[67,0]
eind = np.array([Loa])
onderwater= df_varend.iloc[42:64,0]
COB=df_varend.iloc[20,1]
COV=df_varend.iloc[21,1]
x=np.arange(0,Loa,0.05)


#containers
Cl=6.06   #container lengte
Cb=2.44  #container breedte
Ch=2.59   #container hoogte
Cw=30E3  #container weight

#aantal containers
n=234
#aantal rijen in de hoogte
atiers=1
#aantal containers in breedte
arij=13
#aantal containers in lengte
abay= n/arij


#opwaartsekracht verdeelde belasting
p=np.zeros(len(x))

p = -df_varend.iloc[42:64,1]*rho_water*g
p = np.append(p,nul)
p = np.append(nul,p)
x_p = df_varend.iloc[42:64,0]
x_p = np.append(0,x_p)
x_p = np.append(x_p,max(onderwater))
p_func = interpolate.interp1d(x_p,p)

#gewicht verdeelde belasting
G = df_varend.iloc[101:123,2]*rho_staal*g*tp_factor
#G=np.append(G,nul)
x_G = df_varend.iloc[101:123,0]
#x_G=np.append(x_G,eind)
G_func = interpolate.interp1d(x_G,G)

#traagheidsmoment over de lengte
I = df_varend.iloc[101:123,6]*tp_factor
#I=np.append(I,nul)
x_I = df_varend.iloc[101:123,0]
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

G_punt=integrate.quad(G_func,0,Loa)
P_punt=integrate.quad(p_func,min(onderwater),max(onderwater))


#som krachten 6 staat voor de 6 meter diepgang
Fc=Cw*n*g

Ftank = -1*(G_punt[0] + P_punt[0] +Fc)
xtank=df_varend.iloc[33,1]
volumetank=Ftank/rho_water/g

volumetankmax=df_varend.iloc[32,1]/df_varend.iloc[35,1]*100


Fillheight=volumetank/volumetankmax

#som momenten
LCG_c= -1*(P_punt[0]*COB +G_punt[0]*COV +Ftank*xtank)/Fc

displacement = df_varend.iloc[18,1]
gewichtschip=displacement*rho_water
H=df_varend.iloc[2,1]




#GM dwarsrichting
It_x = df_varend.iloc[27,1]
displacement = df_varend.iloc[18,1]

KB = df_varend.iloc[20,3]
KG = df_varend.iloc[21,3]

#berekening displacement nieuw nadat containers erop zijn
gewichtschip=displacement*rho_water
displacement1=(gewichtschip+Cw*n)/rho_water
BM_t = It_x/displacement1
KGcont_v=H+(Ch*atiers/2)
KGtank_v=df_varend.iloc[33,3]

KG_nieuw= (KG*G_punt[0]/g+KGcont_v*n*Cw+KGtank_v*volumetank*rho_water)/(G_punt[0]/g+n*Cw+volumetank*rho_water)

GM_t_v = KB + BM_t - KG_nieuw 



#LCG
LCF = df_varend.iloc[26,1]
LCGNieuw=(LCF*G_punt[0]/g+LCG_c*n*Cw+xtank*volumetank*rho_water)/(G_punt[0]/g+n*Cw+volumetank*rho_water)
#GM langsrichting
It_y = df_varend.iloc[27,2]
BM_l = It_y/displacement
GM_l = KB +BM_l-KG

#KG1=(KG*gewichtschip+F_tank1/g*tankx+F_cont*VCG_c/g)/(F_cont/g+gewichtschip+F_tank1)



V_s = df_varend.iloc[152:165,1]
R_tot = df_varend.iloc[152:165,3]

R_tot_max = df_varend.iloc[166,3]