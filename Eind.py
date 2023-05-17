import matplotlib.pyplot as plt
from sterkteleer import x,p,G,q,V,M,phi,v,tanklast,vb_cont,vb_last




#plots in een class runnen met plot.q() om bijv q te ploten
class plot():
    def p():
        plt.plot(x,p)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('Opwaartsekracht (p) [N/m]')
        plt.title('Opwaartsekracht uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def G():
        plt.plot(x,G)
        
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('Zwaartekracht als verdeelde belasting (G) [N/m]')
        plt.title('Zwaartekracht uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def q():
        plt.plot(x,q)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('Nettobelasting (q) [N/m]')
        plt.title('Nettobelasting uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def vb():
        figure = plt.figure(figsize=(10,15))
        ax = plt.subplot(111)
        plt.plot(x,-q,label="Totale belasting")
        plt.plot(x,-p,'--',label="Buoancy")
        plt.plot(x,-G,'--',label="Gewicht")
        plt.plot(x,-vb_cont,'--',label="Containers")
        plt.plot(x,-tanklast,'--',label="Balasttank")
        plt.plot(x,-vb_last,'--',label="Last")
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('Nettobelasting (q) [N/m]')
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
 
    def V():
        figure = plt.figure(figsize=(10,12))
        plt.plot(x,-V)
        plt.xlabel(r'$L_{oa} [m]$')
        plt.ylabel(r'$Dwarskracht (V) [N]$')
        plt.title(r'Dwarskracht uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def M():
        figure = plt.figure(figsize=(10,12))
        plt.plot(x,M)
        plt.xlabel(r'$L_{oa} [m]$')
        plt.ylabel(r'$Moment (M) [Nm]$')
        plt.title(r'Intern moment uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def phi():
        plt.plot(x,phi+C)
        plt.xlabel(r'$L_{oa} [m]$')
        plt.ylabel(r'$hoekverdraaing (phi) [radialen]$')
        plt.title(r'de hoekverdraaing')
        plt.grid()
        plt.show()
    def v():
        plt.plot(x,v)
        plt.xlabel(r'$L_{oa} [m]$')
        plt.ylabel(r'$doorbuiging (v) [m]$')
        plt.title(r'doorbuiging')
        plt.grid()
        plt.show()
    def alles():
        plt.figure(figsize=(16,9))
        plt.plot(x,q)
        plt.plot(x,G)
        plt.plot(x,p)
        plt.plot(x,phi)
        plt.plot(x,v)
        plt.plot(x,M)

plot.vb()
plot.V()
plot.M()
plot.phi()
plot.v()