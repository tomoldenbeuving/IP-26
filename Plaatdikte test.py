import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

p1 = pd.read_excel("IP.xlsx","Plaatdikte uitvogelen")
p2 = pd.read_excel("IP.xlsx","Plaatdikte 2")
p3 = pd.read_excel("IP.xlsx","Plaatdikte 3")

x = p1.iloc[101:123,0]

tp1 = p1.iloc[101:123,3].to_numpy()
tp2 = p2.iloc[101:123,3].to_numpy()
tp3 = p3.iloc[101:123,3].to_numpy()

plt.plot(x,tp1)
plt.plot(x,(tp2/5))
plt.plot(x,(tp3/10))
plt.grid()
plt.show()

