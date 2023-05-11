
import matplotlib.pyplot as plt
from sterkteleer import x,p,G,q,V,M,phi,v




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

    

        
    def V():
        plt.plot(x,V)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('Dwarskracht (V) [N]')
        plt.title('Dwarskracht uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def M():
        plt.plot(x,M)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('Moment (M) [Nm]')
        plt.title('Intern moment uitgezet tegen de totale lengte')
        plt.grid()
        plt.show()

    def phi():
        plt.plot(x,phi)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('hoekverdraaing (phi) [radialen]')
        plt.title('de hoekverdraaing')
        plt.grid()
        plt.show()
    def v():
        plt.plot(x,v)
        plt.xlabel('L.O.A. [m]')
        plt.ylabel('doorbuiging (v) [m]')
        plt.title('doorbuiging')
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

