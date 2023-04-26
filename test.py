import pandas as pd
import numpy as np

rho_staal = 7.85E3
rho_water = 1.025E3
g = 9.811

df = pd.read_excel("https://tud365-my.sharepoint.com/personal/toldenbeuving_tudelft_nl/Documents/IP.xlsx")

p = df.iloc[42:64,1]*rho_water*g

G = -df.iloc[97:119,2]*rho_staal*g

q = p+G

