import pandas as pd
import numpy as np

df = pd.read_excel("IP_1mm.xlsx",'Last')
df = df.round(4)

df_varend = pd.read_excel("IP_1mm.xlsx",'Varend')
df_varend = df_varend.round(4)

df_leeg = pd.read_excel("IP_1mm.xlsx",'Leeg')
df_leeg = df_leeg.round(4)

tp_factor = 1
