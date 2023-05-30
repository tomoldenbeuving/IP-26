import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

def get_sheetnames_xlsx(filepath):
    wb = load_workbook(filepath, read_only=True, keep_links=False)
    return wb.sheetnames

radii= get_sheetnames_xlsx("bilge radius.xlsx")

for i in radii:
    data = pd.read_excel("bilge radius.xlsx", i)



def trendplot(x,y):
    figure = plt.figure(figsize=(10,15))
    ax = plt.subplot(111)

    for i in range(np.shape(y)[0]):
        plt.plot(x,y[i,])
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
