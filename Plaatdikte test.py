import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

p1 = pd.read_excel("IP.xlsx","TP1")
p2 = pd.read_excel("IP.xlsx","TP20")
p3 = pd.read_excel("IP.xlsx","TP53")

x = p1.iloc[101:123,0]

A1 = p1.iloc[101:123,2].to_numpy()
A2 = p2.iloc[101:123,2].to_numpy()
A3 = p3.iloc[101:123,2].to_numpy()
it1 = p1.iloc[101:123,6].to_numpy()
it2 = p2.iloc[101:123,6].to_numpy()
it3 = p3.iloc[101:123,6].to_numpy()

plt.plot(x,A1*53,"--")
plt.plot(x,A2*53/20)
plt.plot(x,A3,"--")
plt.grid()
plt.show()

plt.plot(x,it1*53,"--")
plt.plot(x,it2*53/20)
plt.plot(x,it3,"--")
plt.grid()
plt.show()
