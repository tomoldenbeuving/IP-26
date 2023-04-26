import pandas as pd
import numpy as np

rho_staal = 7.85E3
rho_water = 1.025E3
g = 9.811

df = pd.read_excel("IP.xlsx")

p = df.iloc[42:64,1]*rho_water*g
