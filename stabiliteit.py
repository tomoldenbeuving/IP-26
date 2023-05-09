import pandas as pd
import numpy as np
from scipy import integrate, interpolate

rho_staal = 7.85E3
E_staal=210E9
rho_water = 1.025E3
g = 9.81
tp=0.008
df = pd.read_excel("IP.xlsx",'VB schip van Goris')
df = df.round(4)
nul = np.zeros(1)
Loa= df.iloc[0,1]
eind = np.array([Loa])
onderwater= df.iloc[42:64,0]

LCB = df.iloc[20,1]
LCF = df.iloc[26,1]
#GM dwarsrichting
It_x = df.iloc[27,1]
displacement = df.iloc[18,1]
BM_t = It_x/displacement
KB = df.iloc[20,3]
KG = df.iloc[26,3]

GM = KB + BM_t - KG 

#GM langsrichting
It_y = df.iloc[27,2]
BM_l = It_y/displacement
GM_l = KB +BM_l-KG
me