import pandas as pd
import numpy as np

df = pd.read_excel("IP_1mm.xlsx",'Last')
df = df.round(4)

df_varend = pd.read_excel("IP_1mm.xlsx",'Varend')
df_varend = df_varend.round(4)

df_leeg = pd.read_excel("IP_1mm.xlsx",'Leeg')
df_leeg = df_leeg.round(4)

tp_factor = 53


#containers
Cl=6.06   #container lengte
Cb=2.44  #container breedte
Ch=2.59   #container hoogte
Cw=30E3  #container weight
B=df.iloc[1,1]
#aantal containers
n=220
#aantal rijen in de hoogte
atiers=3
#aantal containers in breedte
arij=np.int64(B/Cb)
#aantal containers in lengte
abay= n/atiers/arij
