import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import math as m
from container import Ch,atiers, G_cont

rho_staal = 7.85E3
E_staal=210E9
rho_water = 1.025E3
g = 9.81
tp_factor= 1
df = pd.read_excel("IP.xlsx",'VB schip van Goris')
df = df.round(4)
nul = np.zeros(1)
Loa= df.iloc[0,1]
eind = np.array([Loa])
onderwater= df.iloc[42:64,0]
Lwl=df.iloc[4,1]

LCB = df.iloc[20,1]
LCF = df.iloc[26,1]

D=df.iloc[2,1]

#GM dwarsrichting
It_x = df.iloc[27,1]
It_z=df.iloc[27,3]
displacement = df.iloc[18,1]
BM_t = It_x/displacement
KB = df.iloc[20,3]
KG = df.iloc[21,3]
Z_cont= Ch*atiers/2+D
KGnieuw=(KG*displacement*g*rho_water+ Z_cont*G_cont)/(displacement*g*rho_water+G_cont)

GM_t = KB + BM_t - KGnieuw

#GM langsrichting
It_y = df.iloc[27,2]
BM_l = It_y/displacement
GM_l = KB +BM_l-KGnieuw

#momentstelling stabiliteit
trim_max = 7/180*np.pi   #of negatieve trimhoek
theta = trim_max/Lwl

Msl=rho_water*g*displacement*GM_l*(theta)
#Msl=rho_water*g*displacement*GM_l*theta
BB1=It_y/displacement*np.tan(theta)
