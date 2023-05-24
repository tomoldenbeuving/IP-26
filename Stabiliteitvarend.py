import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import matplotlib.pyplot as plt
from Sterkteleerbeladen import Ch, atiers


rho_staal = 7.85E3
E_staal=210E9
rho_water = 1.025E3
g = 9.81
tp_factor=1
df = pd.read_excel("IP.xlsx",'VB varend')
df = df.round(4)
nul = np.zeros(1)
Loa= df.iloc[0,1] +df.iloc[67,0]
eind = np.array([Loa])
onderwater= df.iloc[42:64,0]
Cw=30E3  #container weight
n=234 #aantal containers
COB=df.iloc[20,1]
COV=df.iloc[21,1]
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

G_punt=integrate.quad(G_func,0,Loa)
P_punt=integrate.quad(p_func,min(onderwater),max(onderwater))


#som krachten 6 staat voor de 6 meter diepgang
Fc=Cw*n*g

Ftank = -1*(G_punt[0] + P_punt[0] +Fc)
xtank=df.iloc[33,1]
volumetank=Ftank/rho_water/g

volumetankmax=df.iloc[32,1]/df.iloc[35,1]*100


Fillheight=volumetank/volumetankmax

#som momenten
LCG_c= -1*(P_punt[0]*COB +G_punt[0]*COV +Ftank*xtank)/Fc

displacement = df.iloc[18,1]
gewichtschip=displacement*rho_water
H=df.iloc[2,1]




#GM dwarsrichting
It_x = df.iloc[27,1]
displacement = df.iloc[18,1]

KB = df.iloc[20,3]
KG = df.iloc[21,3]

#berekening displacement nieuw nadat containers erop zijn
gewichtschip=displacement*rho_water
displacement1=(gewichtschip+Cw*n)/rho_water
BM_t = It_x/displacement1
KGcont_v=H+(Ch*atiers/2)
KGtank_v=df.iloc[33,3]

KG_nieuw= (KG*G_punt[0]+KGcont*n*Cw+KGtank*volumetank*rho_water)/(G_punt[0]+n*Cw+volumetank*rho_water)

GM_t_v = KB + BM_t - KG_nieuw 



#LCG
LCF = df.iloc[26,1]
LCGNieuw=(LCF*gewichtschip+LCG_c*n*Cw+xtank*volumetank*rho_water)/(gewichtschip+n*Cw+volumetank*rho_water)
#GM langsrichting
It_y = df.iloc[27,2]
BM_l = It_y/displacement
GM_l = KB +BM_l-KG

#KG1=(KG*gewichtschip+F_tank1/g*tankx+F_cont*VCG_c/g)/(F_cont/g+gewichtschip+F_tank1)



V_s = df.iloc[152:165,1]
R_tot = df.iloc[152:165,3]

R_tot_max = df.iloc[165,3]