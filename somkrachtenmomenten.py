#%%
import pandas as pd
import numpy as np
from scipy import integrate, interpolate

df = pd.read_excel("IP.xlsx",'VB schip van Goris')

g=9.81
rho_water=1025

#som van de krachten
from sterkteleer import G

G=sum(G)

from sterkteleer import p

P=sum(p)


