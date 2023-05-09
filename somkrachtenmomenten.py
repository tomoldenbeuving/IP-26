#%%
import pandas as pd
import numpy as np

df = pd.read_excel("IP.xlsx",'VB schip van Goris')

g=9.81
rho_water=1025

#som van de krachten
from sterkteleer import G

G=sum(G)

from sterkteleer import p

P=sum(p)

from container import F_containerschip

F_c=sum(F_containerschip)

from sterkteleer import F_tank

F_tank=F_tank

som_F=G+P+F_c+F_tank

