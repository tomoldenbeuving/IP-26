import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

x= np.array([[1,2,3,4],
            [1.5,2.5,3.5,4.5]])
y = np.array([1,2,3,4])

def trendplot(x,y):
    figure = plt.figure(figsize=(10,15))
    ax = plt.subplot(111)

    for i in range(np.shape(y)[0]):
        plt.plot(x[i:],y)
    plt.xlabel('[m]')
    plt.ylabel('[N/m]')
    plt.title('Belasting uitgezet tegen de totale lengte')
    plt.grid()
    plt.legend()
    # Shrink current axis's height by 10% on the bottom
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                    box.width, box.height * 0.9])
    # Put a legend below current axis
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
            fancybox=True, shadow=True, ncol=3)
    plt.show()

    trendplot(x,y)
