import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import matplotlib.pyplot as plt
from imports import df_varend, tp_factor,n,Cw,Ch,a,atiers_varend


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
G = df_varend.iloc[101+a:123+a,2]*rho_staal*g*tp_factor
#G=np.append(G,nul)
x_G = df_varend.iloc[101+a:123+a,0]
#x_G=np.append(x_G,eind)
G_func = interpolate.interp1d(x_G,G)

#traagheidsmoment over de lengte
I = df_varend.iloc[101+a:123+a,6]*tp_factor
#I=np.append(I,nul)
x_I = df_varend.iloc[101+a:123+a,0]
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

G_punt=integrate.simpson(G,x)
P_punt=integrate.simpson(p,x)


#som krachten 6 staat voor de 6 meter diepgang
Fc=Cw*n*g

Ftank = -1*(G_punt + P_punt +Fc)
xtank=df_varend.iloc[33,1]
volumetank=Ftank/rho_water/g

volumetankmax=df_varend.iloc[32,1]/df_varend.iloc[35,1]*100


Fillheight=volumetank/volumetankmax

#som momenten
LCG_c= -1*(P_punt*COB +G_punt*COV +Ftank*xtank)/Fc

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
KGcont_v=H+(Ch*atiers_varend/2)
KGtank_v=df_varend.iloc[33,3]

KG_nieuw= (KG*G_punt/g+KGcont_v*n*Cw+KGtank_v*volumetank*rho_water)/(G_punt/g+n*Cw+volumetank*rho_water)
I_water=df_varend.iloc[38,1]

gg1=I_water/displacement
GM_t_v = KB + BM_t - KG_nieuw-gg1



#LCG
LCF = df_varend.iloc[26,1]
LCGNieuw=(LCF*G_punt/g+LCG_c*n*Cw+xtank*volumetank*rho_water)/(G_punt/g+n*Cw+volumetank*rho_water)
#GM langsrichting
It_y = df_varend.iloc[27,2]
BM_l = It_y/displacement
GM_l = KB +BM_l-KG

#KG1=(KG*gewichtschip+F_tank1/g*tankx+F_cont*VCG_c/g)/(F_cont/g+gewichtschip+F_tank1)



V_s = df_varend.iloc[152+a:165+a,1]
R_tot = df_varend.iloc[152+a:165+a,3]

R_tot_max = df_varend.iloc[151+a,3]