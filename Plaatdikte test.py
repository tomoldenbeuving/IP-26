import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

p1 = pd.read_excel("IP.xlsx","Plaatdikte uitvogelen")
p2 = pd.read_excel("IP.xlsx","Plaatdikte 2")
p3 = pd.read_excel("IP.xlsx","Plaatdikte 3")

x = p1.iloc[101:123,0]

tp1 = p1.iloc[101:123,8].to_numpy()
tp2 = p2.iloc[101:123,8].to_numpy()
tp3 = p3.iloc[101:123,8].to_numpy()
it1 = p1.iloc[101:123,7].to_numpy()
it2 = p2.iloc[101:123,7].to_numpy()
it3 = p3.iloc[101:123,7].to_numpy()

plt.plot(x,tp1*10,"--")
plt.plot(x,tp2*2)
plt.plot(x,tp3,"--")
plt.grid()
plt.show()

plt.plot(x,it1*10,"--")
plt.plot(x,it2*2)
plt.plot(x,it3,"--")
plt.grid()
plt.show()
