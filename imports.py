import pandas as pd
import numpy as np

df = pd.read_excel(".\chonker\chonker.xlsx",'last')
df = df.round(4)

df_varend = pd.read_excel(".\chonker\chonker.xlsx",'varend')
df_varend = df_varend.round(4)

df_leeg = pd.read_excel(".\chonker\chonker.xlsx",'leeg')
df_leeg = df_leeg.round(4)

tp_factor = 1