import pandas as pd
import numpy as np
from scipy import integrate, interpolate
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
E_staal=210E9
rho_water = 1.025E3
g = 9.81
tp_factor=1
df = pd.read_excel("IP.xlsx",'VB schip van Goris')
df = df.round(4)
nul = np.zeros(1)
Loa= df.iloc[0,1]
eind = np.array([Loa])
onderwater= df.iloc[42:64,0]

#het gewicht van de containers punt belasting
G_cont=n*Cw*g

x=np.arange(0,Loa,0.05)

p=np.zeros(len(x))

p = -df.iloc[42:64,1]*rho_water*g
p = np.append(p,nul)
p = np.append(nul,p)
x_p = df.iloc[42:64,0]
x_p = np.append(0,x_p)
x_p = np.append(x_p,max(onderwater))
p_func = interpolate.interp1d(x_p,p)


G = df.iloc[101:123,2]*rho_staal*g*tp_factor
G=np.append(G,nul)
x_G = df.iloc[101:123,0]
x_G=np.append(x_G,eind)
G_func = interpolate.interp1d(x_G,G)


I = df.iloc[101:123,6]*tp_factor
I=np.append(I,nul)
x_I = df.iloc[101:123,0]
x_I=np.append(x_I,eind)
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
G_punt=integrate.quad(G_func,0,Loa)
P_punt=integrate.quad(p_func,min(onderwater),max(onderwater))
F_c=G_cont
F_tank=integrate.quad(tank_func,min(x_tank),max(x_tank))


F_last = -P_punt[0]  -G_punt[0]  -F_c  -F_tank[0]

#tijdelijke last

#F_last = 99399464.7


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

#Hoekverdraaiing zonder integratie constante
thetaEI=(integrate.cumtrapz(M,x,initial=0))
theta=np.zeros(len(x))

for i in range(len(x)):
    try:
        theta[i]=thetaEI[i]/(E_staal*I[i])
    except ZeroDivisionError:
        theta[i] = 0
         
#Waarde en locatie maximaal moment
Mmax_index = np.argmax(M)
M_max = M[Mmax_index] #Waarde maximaal moment
Loc_M_max = x[Mmax_index] #Locatie maximaal moment

#Integratie constante
theta_Mmax = theta[Mmax_index]
C=theta_Mmax

#Uiteindelijke verdraaiingslijn
theta= theta - C

#Waarde en locatie maximale hoekverdraaiing
thetamax_index = np.argmax(theta)
theta_max = theta[thetamax_index] #Waarde maximale Hoekverdraaiing
Loc_theta_max = x[thetamax_index] #Locatie maximale hoekverdraaiing

#Doorbuiging zonder integratie constante
v=integrate.cumtrapz(theta,x,initial=0)

#Integratie constante
v_thetamax = np.interp(Loc_theta_max, x, v)
D=v_thetamax

#Uiteindelijke doorbuigingslijn
v= v + D


# Maximaal toelaatbaar moment
sigma_max=190E6
I_midship=df.iloc[114, 7]
H=df.iloc[2,1]
KG_y=df.iloc[21,3]
y=H-KG_y

moment_max=(sigma_max*I_midship)/y

#Weerstandsmoment
W=I_midship/y

#Spanningsverdeling
sigma=M/W

