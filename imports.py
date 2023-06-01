import pandas as pd
import numpy as np

df = pd.read_excel(".\ik ben snelheid\ik ben snelheid.xlsx",'Last')
df = df.round(4)

df_varend = pd.read_excel(".\ik ben snelheid\ik ben snelheid.xlsx",'Varend')
df_varend = df_varend.round(4)

df_leeg = pd.read_excel(".\ik ben snelheid\ik ben snelheid.xlsx",'Leeg')
df_leeg = df_leeg.round(4)

tp_factor = 1