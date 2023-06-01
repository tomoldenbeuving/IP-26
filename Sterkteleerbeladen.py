import pandas as pd
import numpy as np
from scipy import integrate, interpolate
from imports import df, tp_factor
import matplotlib.pyplot as plt


#containers
Cl=6.06   #container lengte
Cb=2.44  #container breedte
Ch=2.59   #container hoogte
Cw=30E3  #container weight

#aantal containers
n=234
#aantal rijen in de hoogte
atiers=3
#aantal containers in breedte
arij=13
#aantal containers in lengte
abay= 6



rho_staal = 7.85E3
E_staal=210000*(10**6)
rho_water = 1.025E3
g = 9.81
nul = np.zeros(1)
Loa= df.iloc[0,1] +df.iloc[67,0]
eind = np.array([Loa])
onderwater= df.iloc[42:64,0]

#het gewicht van de containers punt belasting
G_cont=n*Cw*g

x=np.arange(0,Loa,0.05)


#opwaartsekracht verdeelde belasting
p=np.zeros(len(x))

p = -df.iloc[42:64,1]*rho_water*g
p = np.append(p,nul)
p = np.append(nul,p)
x_p = df.iloc[42:64,0]
x_p = np.append(0,x_p)
x_p = np.append(x_p,max(onderwater))
p_func = interpolate.interp1d(x_p,p)

#gewicht verdeelde belasting
G = df.iloc[101:123,2]*rho_staal*g*tp_factor
#G=np.append(G,nul)
x_G = df.iloc[101:123,0]
#x_G=np.append(x_G,eind)
G_func = interpolate.interp1d(x_G,G)

#traagheidsmoment over de lengte
I = df.iloc[101:123,7]*tp_factor
#I=np.append(I,nul)
x_I = df.iloc[101:123,0]
#x_I=np.append(x_I,eind)
I_func = interpolate.interp1d(x_I,I)


G = G_func(x)
I= I_func(x)
p= np.zeros(len(x))
# for loop zodat nadat het onderwater stopt p altijd 0
for i in range(len(x)):
    if x[i] < min(onderwater):
        p[i] = 0
    elif x[i] > max(onderwater):
        p[i]=0
    else:
        p[i]=p_func(x[i])

#index=[np.arange(0,1)]

#I=np.delete(I_func(x),index)

#Ballast tank
V_tank=df.iloc[32,1]
G_tank=V_tank*rho_water*g
arm_tank= df.iloc[34,1] 

tank = df.iloc[92:97,1]*rho_water*g#*(df.iloc[35,1]/100)
x_tank = df.iloc[92:97,0]
tank_func=interpolate.interp1d(x_tank,tank)

tanklast=np.zeros(len(x))

for i in range(len(x)):
    if x[i] > min(x_tank) and x[i] < max(x_tank):
        tanklast[i]= tank_func(x[i])
    else:
        tanklast[i] = 0




#last op platfrom uitrekenen	

#som van de krachten
G_punt=integrate.quad(G_func,0,Loa,epsabs=8E-6,epsrel=8E-6)
P_punt=integrate.quad(p_func,min(onderwater),max(onderwater))
F_c=G_cont
F_tank=integrate.quad(tank_func,min(x_tank),max(x_tank))


F_last = -P_punt[0]  -G_punt[0]  -F_c  -F_tank[0]


# som van momenten
x_tank = df.iloc[33,1]
x_last = 13.5
COB = df.iloc[20,1]
COV = df.iloc[21,1]
#tijdelijke arm
#arm_c=216
arm_c = -1*(P_punt[0]*COB +G_punt[0]*COV +F_tank[0]*x_tank +F_last*x_last)/F_c


#verdeeldebelasting container

start_cont=arm_c-(0.5*abay*Cl)
eind_cont=arm_c+(0.5*abay*Cl)

x_vd=np.arange(start_cont,eind_cont,0.5)
G_cont_overlengte=G_cont/(eind_cont-start_cont)

vb_cont=np.zeros(len(x))

for i in range(len(x)):
    if x[i] > (start_cont) and x[i] < (eind_cont):
        vb_cont[i] = G_cont_overlengte
    else:
        vb_cont[i]= 0 


#verdeeldebelasting last op platform
x_platform=[11.8,16.2]
F_last_overlengte=F_last/(x_platform[1]-x_platform[0])

vb_last=np.zeros(len(x))

for i in range(len(x)):
    if x[i] > min(x_platform) and x[i] < max(x_platform):
        vb_last[i] = F_last_overlengte
    else:
        vb_last[i]= 0      



#verdeelde belasting
q= p+G+vb_cont+tanklast+vb_last

# integratie lijnen
V = integrate.cumtrapz(q,x,initial=0) 
M = integrate.cumtrapz(V,x,initial=0)

#Waarde en locatie maximaal moment
Mmax_index = np.argmax(M)
M_max = M[Mmax_index] #Waarde maximaal moment
Loc_M_max = x[Mmax_index] #Locatie maximaal moment

#Hoekverdraaiing zonder integratie constante
thetaEI=integrate.cumtrapz(M/(E_staal*I),x,initial=0)

#Integratie constante
vEI=integrate.cumtrapz(thetaEI,x,initial=0)
theta_Mmax = thetaEI[Mmax_index]
C=(np.max(vEI))/Loa

#Uiteindelijke verdraaiingslijn
theta= thetaEI - C

#Doorbuiging met integratie constante
v=integrate.cumtrapz(theta,x,initial=0)

#Waarde en locatie maximale doorbuiging
vmax_index = np.argmin(v)
v_max = v[vmax_index] #Waarde maximale doorbuiging
Loc_v_max = x[vmax_index] #Locatie maximale doorbuiging

# Maximaal toelaatbaar moment
sigma_maxtoelaatbaar=190E6
I_midship=df.iloc[114, 7]*tp_factor
H=df.iloc[2,1]
KG_y=df.iloc[21,3]
y=H-KG_y+(tp_factor*0.001)

moment_max=(sigma_maxtoelaatbaar*I_midship)/y

#Weerstandsmoment
y_boven=df.iloc[101:123,10]-df.iloc[101:123,5]
y_onder=df.iloc[101:123,5]-df.iloc[101:123,9]
W=df.iloc[101:123,7]/y_boven

W=np.append(W,nul)
x_W = df.iloc[101:123,0]
x_W=np.append(x_W,eind)
W_func = interpolate.interp1d(x_W,W)
W = W_func(x)


#Spanningsverdeling
sigma=np.zeros(len(x))

for i in range(len(x)):
    try:
        sigma[i]=M[i]/(W[i])
    except ZeroDivisionError:
        sigma[i] = 0

sigma_max=np.max(sigma)
'''
    return sigma_max


#plaatdikte uitrekenen
sigma_maxtoelaatbaar=190E6
#\sigma_max = sterkteleer_berekeningen(tp_factor)
def plaatdikte_rekenen():
    while sigma_max > sigma_maxtoelaatbaar:
        if sigma_max < sigma_maxtoelaatbaar:
            print("tp_factor waarbij sigma_max gelijk is aan sigma_toelaatbaar:", tp_factor)
            break
        sigma_max = sterkteleer_berekeningen(tp_factor)
        print(r"sigma_max",sigma_max,r"t_p",tp_factor) 
        tp_factor += 5  # Verhoog tp_factor met 1'''

