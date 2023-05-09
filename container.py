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


#containers
Cl=6.06   #container lengte
Cb=2.44  #container breedte
Ch=2.59   #container hoogte
Cw=30E3  #container weight

#aantal containers
n=234
#aantal rijen in de hoogte
atiers=3
#aantal containers in breedte
arij=13
#aantal containers in lengte
abay= 6

# waar de verdeelde belasting van de container begint in de lengte-as dus y-as
containerbegin = 180.363
containereind  = 216.711
#het gewicht van de containers punt belasting
G_cont=n*Cw*g
sigma_max=190E6
F_container= Cw*n*g 
print(Loa)


