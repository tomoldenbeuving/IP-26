import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import math as m
from sterkteleer import Cw, n, Ch,V_tank,atiers


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
BM_t = It_x/displacement
KB = df.iloc[20,3]
KG = df.iloc[26,3]
gewichtschip=displacement*rho_water*g
KGcont=H+Ch*atiers/2
KGtank=df.iloc[33,3]

KG_nieuw= KG*gewichtschip+KGcont*n*Cw+KGtank*V_tank*rho_water/(gewichtschip+n*Cw+V_tank*rho_water)

GM_t = KB + BM_t - KG 

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
