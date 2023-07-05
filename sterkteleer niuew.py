# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:22:11 2023

@author: timme
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 13:36:03 2023

@author: timme
"""

import numpy as np
import math
import scipy as sp
from math import sqrt
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.interpolate import interp1d
import numpy as np
import math
import scipy as sp
import matplotlib.pyplot as plt
from scipy import integrate
import pandas as pd

#"C:\Users\timme\Downloads\MT1458 - Excel 5.xlsx"

"Gegevens uit excel halen"
#excel file lezen
#dataframe = pd.read_excel(r"C:\Users\timme\Downloads\poging9.xlsx")
dataframe = pd.read_excel("./experimenten jiswi/eind ontwerp theone.xlsx",'Last')

data = np.array(dataframe) 

#Totale afstand en spant omtrek
T_afstand = data[101:123,0].astype(np.float64)
T_area = data[101:123,1].astype(np.float64)

#Bouyant afstand en cross section area
B_afstand = data[42:64,0].astype(np.float64)
B_area = data[42:64,1].astype(np.float64)

#Ballast afstand en cross section area
Ballast_afstand = data[92:97,0].astype(np.float64)
Ballast_area = data[92:97,1].astype(np.float64)


# =============================================================================
# 
# =============================================================================

"waardedes en constanten"
#constantes
rho_water = 1025
rho_staal = 7850
g = 9.81
x1_platform = 10.8
x2_platform = 16.2

#for loop om waardes uit excel te halen
for x in range(0, len(dataframe.iloc[:,0:1].values)):
    if dataframe.iloc[x,0:1].values == "COV Total [m]": 
        cov = dataframe.iloc[x,1]
    if dataframe.iloc[x,0:1].values == "COB [m]":
        cob = dataframe.iloc[x,1]
    if dataframe.iloc[x,0:1].values == "COV WB [m]":
        cov_bal = dataframe.iloc[x,1]
    if dataframe.iloc[x,0:1].values == "B [m]":
        B = dataframe.iloc[x,1]
    if dataframe.iloc[x,0:1].values == "Loa  [m]":
        loa = dataframe.iloc[x,1]
    if dataframe.iloc[x,0:1].values == "H [m]":
        H = dataframe.iloc[x,1]
    
    
stapgrote = 0.001
x_schip = np.arange(T_afstand[0], T_afstand[-1], stapgrote)
col= ((x_schip[0]+x1_platform)+(x_schip[0]+x2_platform))/2

# =============================================================================
# 
# =============================================================================
"containerwaardes"
l_con = 6.06
b_con = 2.44
n_rows = math.floor(B/b_con)
n_bays = 5
m_con = 30000
h_con = 2.59
lcg_con = loa - ((l_con*n_bays)/2)
# =============================================================================
# 
# =============================================================================
"Neerwaartse belasting"
#Verdeelde belasting van de huid van het schip
#handmatig
huiddikte = 0.066
w_g = -1*T_area*rho_staal*huiddikte*g

fit_g = sp.interpolate.interp1d(T_afstand, w_g, kind = "linear")
y_romp = fit_g(x_schip)

schaal = huiddikte/0.001
# =============================================================================
# 
# =============================================================================
'verdeelde belasting ballast'

w_ball = -1*Ballast_area*rho_water*g

fit_ball = sp.interpolate.interp1d(Ballast_afstand, w_ball, kind = "linear")
x_ball = np.arange(Ballast_afstand[0], Ballast_afstand[-1], 0.001)
x_ball[-1] = Ballast_afstand[-1]
y_ball = fit_ball(x_ball)
y_ball_totaal = np.zeros(len(x_schip))

for z in range(0,len(x_schip)):
    if x_schip[z] >= x_ball[0]:
        n_ball = z -1
        break

for z in range(0,len(x_schip)):
    if x_schip[z] >= x_ball[-1]:
        n_ball_eind = z -1
        break

y_ball_totaal[n_ball:n_ball_eind] = y_ball  
# =============================================================================
# 
# =============================================================================
"opwaartse belasting"

w_bouyancy = B_area*rho_water*g

fit_bouy = sp.interpolate.interp1d(B_afstand, w_bouyancy, kind = "linear")
x_bouy = np.arange(B_afstand[0], B_afstand[-1], 0.001)
y_bouy = fit_bouy(x_bouy)
y_bouy_final = np.zeros(len(x_schip))

n_bouy=0
n_bouy1=0

for w in range(0,len(x_schip)):
    if x_schip[w] >= x_bouy[0]:
        n_bouy = w
        break
        
for w in range(0,len(x_schip)):
    if x_schip[w] >= x_bouy[-1]:
        n_bouy1 = w + 1
        break

y_bouy_final [n_bouy :n_bouy1] = y_bouy
# =============================================================================
# 
# =============================================================================
"krachten balans"
#krachten vinden
F_huid =  (-1)*integrate.simpson(y_romp, x_schip)
F_bouyancy =  integrate.simpson(y_bouy_final, x_schip)
F_ballast = (-1)*integrate.simpson(y_ball_totaal, x_schip)




for x in range(1,1000):
    F_con = m_con*x*g
    F_last = F_bouyancy - F_ballast - F_huid - F_con
    x_con = (F_bouyancy*cob - F_last*col - F_huid*cov - F_ballast*cov_bal)/ F_con
    if x_con < lcg_con:
        n_con = x - 1
        #print(n_con)
        break
    
F_con = m_con*n_con*g
Ftot = F_bouyancy-F_ballast-F_con-F_huid-F_last

n_tiers = n_con/(n_bays* n_rows)

#print(Ftot)
# =============================================================================
# 
# =============================================================================
"verdeelde belasting"
w_pl = (-1)*F_last/5.4
w_con = (-1)*F_con/(n_bays*l_con)

count1 = 0
count2 = 0

for z in range(len(x_schip)):
    if x_schip[z] <= x_schip[0] + x1_platform:
        count1 = count1 + 1
    if x_schip[z] <= x_schip[0]+x2_platform:
        count2 = count2 + 1  

y_pl = np.zeros(len(x_schip))
y_pl[count1:count2] = w_pl

count3 = 0
count4 = 0

for z in range(len(x_schip)):
    if x_schip[z] <= x_con-((l_con*n_bays)/2):
        count3 = count3 + 1
    if x_schip[z] <= x_con +((l_con*n_bays)/2):
        count4 = count4 + 1   
y_con = np.zeros(len(x_schip))
y_con[count3:count4-1] = w_con
# =============================================================================
# 
# =============================================================================
"netto belasting"

neerwaarts_totaal = y_romp + y_pl + y_con + y_ball_totaal
netto_belasting = neerwaarts_totaal + y_bouy_final


plt.figure()
plt.plot(x_schip, y_romp, label = "huid")
plt.plot(x_schip, y_pl, label = "platform")
plt.plot(x_schip, y_con, label = "containers")
plt.plot(x_schip,y_ball_totaal, label = "ballast")
plt.plot(x_schip, y_bouy_final, label = "bouyancy")
plt.plot(x_schip, neerwaarts_totaal, label = "neerwaarts")
plt.plot(x_schip, netto_belasting, label = "netto belasting")
plt.xlabel("x afstand")
plt.ylabel("N")
plt.legend()
plt.grid()

# =============================================================================
# 
# =============================================================================
"dwarskrachtenlijn"
dwarskracht = integrate.cumtrapz(netto_belasting, x_schip)
nul_l = np.zeros(1)  #voegt een nul toe aan het begin van de dwarskrachten lijst zodat de x_schip en dwarskrachtenlijn even lang worden
dwarskracht_final = np.concatenate((nul_l, dwarskracht))


plt.figure()
plt.plot(x_schip, dwarskracht_final)
plt.xlabel("x afstand")
plt.ylabel("N")
plt.grid()
plt.title("dwarskrachtenlijn")
# =============================================================================
# 
# =============================================================================
"momentenlijn"
moment = integrate.cumtrapz(dwarskracht_final, x_schip)
moment_final = np.concatenate((nul_l, moment))

max_moment = min(moment_final)

teller = 0
for j in range(0,len(moment_final)-1):
    teller = teller + 1
    if moment_final[j] == max_moment:
        x_maxmoment = teller


plt.figure()
plt.plot(x_schip, moment_final)
plt.xlabel("x afstand")
plt.ylabel("moment (Nm)")
plt.grid()
plt.title("momentenlijn")

# =============================================================================
# 
# =============================================================================
"Weerstandsmoment bepalen"

I_y = data[101:123,7].astype(np.float64)*schaal
z_spant = data[101:123,5].astype(np.float64)
z_keel = data[101:123,9].astype(np.float64)
cross_section = data[101:123,2].astype(np.float64)

weerstandsmoment = (I_y)/(z_spant-z_keel)  #+cross_section*(z_spant**2)

myfit_weer = sp.interpolate.interp1d(T_afstand, weerstandsmoment, kind = "linear")
y_weerstand = myfit_weer(x_schip)

# =============================================================================
# 
# =============================================================================
"Doorbuiging grafiek"

fit_iy = sp.interpolate.interp1d(T_afstand, I_y, kind = "linear")
y_iy = fit_iy(x_schip)
E = 210 * 10**9


#hoekverdraaiing
hoekverdraaing = integrate.cumtrapz((moment_final/(y_iy*E)), x_schip) 
hoekverdraaing_final = np.concatenate((nul_l, hoekverdraaing))

#doorbuiging
doorbuiging = integrate.cumtrapz(hoekverdraaing_final, x_schip)
doorbuiging_final = np.concatenate((nul_l, doorbuiging))

# =============================================================================
# plt.figure()
# plt.plot(doorbuiging_final)
# =============================================================================

C = np.max(np.abs(doorbuiging_final))/loa
laatstehoekverdraaing = hoekverdraaing_final + C

# =============================================================================
# plt.figure()
# plt.plot(x_schip, laatstehoekverdraaing)
# =============================================================================

v_tussen = integrate.cumtrapz(laatstehoekverdraaing, x_schip)

v_final = np.concatenate((nul_l,v_tussen))

counter = 0
for h in range(0, len(v_final)):
    counter = counter + 1
    if v_final[h] == np.max(v_final):
        number = counter
        
 
plt.figure()
plt.plot(x_schip[:], v_final[:])
plt.grid()
plt.xlabel("x afstand")
plt.ylabel("doorbuiging")
plt.title("doorbuiging")
# =============================================================================
# 
# =============================================================================

"spanningsverdeling"

spanning = []
for g in range(len(y_weerstand)):
    spanning.append((moment_final[g]/y_weerstand[g])) #/9.81)
    
spanning_array = np.array(spanning)

print("max spanning", max(np.abs(spanning_array[:-10000])))
print("maximale last", F_last)
print("aantal containers", n_con)
print("Lcg ballast containers", x_con)
print("Vcg ballast containers", H+((h_con*n_tiers)/2))
print("aantal bays", n_bays)
print("aantal rows", n_rows)
print("aantal tiers", n_tiers)
print("")
print("")
print("maximaal moment", np.max(np.abs(moment_final)))
print("afstand maximaal moment", x_schip[x_maxmoment])
print("plaatdikte", huiddikte)
print("maximale doorbuiging", np.max(np.abs(v_final)))
print("locatie maximale doorbuiging", x_schip[number])


plt.figure()
plt.plot(x_schip[:-10000], (-1)*spanning_array[:-10000])
plt.xlabel("x afstand")
plt.ylabel("spanning")
plt.grid()
