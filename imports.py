import pandas as pd
import numpy as np

df = pd.read_excel("IP.xlsx",'VB schip van Goris')
df = df.round(4)

df_varend = pd.read_excel("IP.xlsx",'VB varend')
df_varend = df.round(4)