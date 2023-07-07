import pandas as pd
import numpy as np

df = pd.read_excel("./Inleveren herkansing/NIET INLEVEREN J 1.7 excel file.xlsx",'Last')
df = df.round(4)

df_varend = pd.read_excel("./Inleveren herkansing/NIET INLEVEREN J 1.7 excel file.xlsx",'Varend')
df_varend = df_varend.round(4)

df_leeg = pd.read_excel("./Inleveren herkansing/NIET INLEVEREN J 1.7 excel file.xlsx",'Leeg')
df_leeg = df_leeg.round(4)

tp_factor = 68

a=0

#containers
Cl=6.06   #container lengte
Cb=2.44  #container breedte
Ch=2.59   #container hoogte
Cw=30E3  #container weight
B=df.iloc[1,1]
#aantal containers
n=266
#aantal rijen in de hoogte

#aantal containers in breedte
arij=np.int64(B/Cb)
#aantal containers in lengte
abay= 5
atiers=n/abay/arij


arij_varend=14
abay_varend=14
atiers_varend=n/abay_varend/arij_varend
