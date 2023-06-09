import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import math as m
from Sterkteleerbeladen import V_tank,F_last,arm_c,x_tank,x_last,G_punt,P_punt
from imports import df, tp_factor,Cw,n,Ch,atiers

rho_staal = 7.85E3
E_staal=210E9
rho_water = 1.025E3
g = 9.81
H=df.iloc[2,1]
nul = np.zeros(1)
Loa= df.iloc[0,1] +df.iloc[67,0]
eind = np.array([Loa])
onderwater= df.iloc[42:64,0]
Lwl=df.iloc[4,1]

LCB = df.iloc[20,1]
dp_leeg=P_punt/(rho_water*g)*-1



#GM dwarsrichting
It_x = df.iloc[27,1]
displacement = df.iloc[18,1]

KB = df.iloc[20,3]
KG = df.iloc[21,3]

#berekening displacement nieuw nadat containers erop zijn
gewichtschip=displacement*rho_water


BM_t = It_x/displacement
KGcont=H+(Ch*atiers/2)
KGtank=df.iloc[33,3]
KGlast=H+2.7

KG_nieuw= (KG*G_punt/g+KGcont*n*Cw+KGlast*F_last/g+V_tank*rho_water*KGtank)/(G_punt/g+n*Cw+F_last/g+V_tank*rho_water)

#vloeistof reductie
I_water=df.iloc[38,1]
gg1=I_water/displacement
GM_t = KB + BM_t - KG_nieuw-gg1

#LCG
LCF = df.iloc[26,1]
LCGNieuw=(LCF*G_punt/g+arm_c*n*Cw+x_last*F_last/g+x_tank*V_tank*rho_water)/(G_punt/g+n*Cw+F_last/g+V_tank*rho_water)

#GM langsrichting
It_y = df.iloc[27,2]
BM_l = It_y/displacement
GM_l = KB +BM_l-KG_nieuw-gg1

#momentstelling stabiliteit
trim_max = 7/180*np.pi   #of negatieve trimhoek
theta = trim_max/Lwl

Msl=rho_water*g*displacement*GM_l*(theta)
#Msl=rho_water*g*displacement*GM_l*theta
BB1=It_y/displacement*np.tan(theta)
