import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import matplotlib.pyplot as plt

x = np.arange(0,11,0.05)

def f(x):
    y = -4/10*x +104/10
    return y

def g(x):
    y = 4/10*(x-1) +6
    return y

def plot():
    figure = plt.figure(figsize=(10,6))
    plt.plot(x,f(x),"--")
    plt.plot(x,g(x),"--")
    plt.plot(x,(g(x)+f(x))/2)
    plt.ylim(0,11)
    plt.show()