#%%
import pandas as pd
import numpy as np

from sterkteleer import G, p,tanklast
from container import F_containerschip

df = pd.read_excel("IP.xlsx",'VB schip van Goris')
g=9.81
rho_water=1025


#som van de krachten
G=sum(G)
P=sum(p)
F_c=sum(F_containerschip)
F_tank=sum(tanklast)

F_last = P - G - F_c - F_tank 


# som van momenten
x_tank = df.iloc[33,1]
x_last = 13.5
COB = df.iloc[20,1]
COV = df.iloc[21,1]

arm_c = (P*COB-G*COV-F_tank*x_tank-F_last*x_last)/F_c


