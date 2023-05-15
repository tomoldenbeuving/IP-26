import pandas as pd
import numpy as np
from scipy import integrate, interpolate


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
F_container= Cw*atiers*arij*g                    # kracht van containers op hetzelfde zwaartepunt
aCL=np.int32(n/arij/atiers)                   #aantal container waarvan het zwaartepunt afstand nodig is
zwaartepuntafstandenL=np.zeros(aCL)
zwaartepuntafstandenL[0]=containerbegin+Cl/2



for i in range(aCL-1):
    zwaartepuntafstandenL[i+1]=zwaartepuntafstandenL[i]+Cl



Fcontainers=np.ones(aCL)*F_container
x_Fcontainer=zwaartepuntafstandenL
F_containerschip = np.zeros(len(x))
F_funccontainer = interpolate.interp1d(x_Fcontainer,Fcontainers)


for i in range(len(x)):
    if x[i] > zwaartepuntafstandenL[0] and x[i] < zwaartepuntafstandenL[aCL-1]:
        F_containerschip[i]= F_funccontainer(x[i])
    else:
        F_containerschip[i]= 0







G_container=Cw*atiers*arij/20*g # per 5 cm, dus delen door 20
Gcontainers=np.ones(aCL)*G_container
x_Gcontainer=zwaartepuntafstandenL
G_containerschip = np.zeros(len(x))
G_funccontainer = interpolate.interp1d(x_Gcontainer,Gcontainers)


for i in range(len(x)):
    if x[i] > zwaartepuntafstandenL[0] and x[i] < zwaartepuntafstandenL[aCL-1]:
        G_containerschip[i]= G_funccontainer(x[i])
    else:
        G_containerschip[i]= 0


