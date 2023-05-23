import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import math as m
from sterkteleer import Cw, n, Ch,V_tank,atiers,F_last


rho_staal = 7.85E3
E_staal=210E9
rho_water = 1.025E3
g = 9.81
tp_factor=1
df = pd.read_excel("IP.xlsx",'VB schip van Goris')
H=df.iloc[2,1]
df = df.round(4)
nul = np.zeros(1)
Loa= df.iloc[0,1]
eind = np.array([Loa])
onderwater= df.iloc[42:64,0]
Lwl=df.iloc[4,1]

LCB = df.iloc[20,1]
LCF = df.iloc[26,1]



#GM dwarsrichting
It_x = df.iloc[27,1]
displacement = df.iloc[18,1]

KB = df.iloc[20,3]
KG = df.iloc[21,3]

#berekening displacement nieuw nadat containers erop zijn
gewichtschip=displacement*rho_water
displacement1=(gewichtschip+Cw*n)/rho_water
BM_t = It_x/displacement1
KGcont=H+(Ch*atiers/2)
KGtank=df.iloc[33,3]
KGlast=H+2.7

KG_nieuw= (KG*gewichtschip+KGcont*n*Cw+KGlast*F_last/g)/(gewichtschip+n*Cw+F_last/g)

GM_t = KB + BM_t - KG_nieuw 

#GM langsrichting
It_y = df.iloc[27,2]
BM_l = It_y/displacement
GM_l = KB +BM_l-KG

#momentstelling stabiliteit
trim_max = 7/180*np.pi   #of negatieve trimhoek
theta = trim_max/Lwl

Msl=rho_water*g*displacement*GM_l*(theta)
#Msl=rho_water*g*displacement*GM_l*theta
BB1=It_y/displacement*np.tan(theta)
