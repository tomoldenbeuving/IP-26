import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
from openpyxl import load_workbook
from scipy import integrate, interpolate

import warnings
warnings.filterwarnings("ignore")


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

tp_factor = 1


def beladen(df):
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
    G_punt=integrate.quad(G_func,0,Loa)
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
    sigma_max=190E6
    I_midship=df.iloc[114, 7]*tp_factor
    H=df.iloc[2,1]
    KG_y=df.iloc[21,3]
    y=H-KG_y

    moment_max=(sigma_max*I_midship)/y

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


    rho_staal = 7.85E3
    E_staal=210E9
    rho_water = 1.025E3
    g = 9.81
    H=df.iloc[2,1]
    nul = np.zeros(1)
    Loa= df.iloc[0,1] +df.iloc[67,0]
    eind = np.array([Loa])
    onderwater= df.iloc[42:64,0]
    Lwl=df.iloc[4,1]

    LCB = df.iloc[20,1]




    #GM dwarsrichting
    It_x = df.iloc[27,1]
    displacement = df.iloc[18,1]

    KB = df.iloc[20,3]
    KG = df.iloc[21,3]

    #berekening displacement nieuw nadat containers erop zijn
    gewichtschip=displacement*rho_water
    displacement1=(gewichtschip+Cw*n)/rho_water
    BM_t = It_x/displacement1
    KGcont=H+(Ch*atiers/2)
    KGtank=df.iloc[33,3]
    KGlast=H+2.7

    KG_nieuw= (KG*G_punt[0]/g+KGcont*n*Cw+KGlast*F_last/g+V_tank*rho_water*KGtank)/(G_punt[0]/g+n*Cw+F_last/g+V_tank*rho_water)

    GM_t = KB + BM_t - KG_nieuw 



    #LCG
    LCF = df.iloc[26,1]
    LCGNieuw=(LCF*gewichtschip+arm_c*n*Cw+x_last*F_last/g+x_tank*V_tank*rho_water)/(gewichtschip+n*Cw+F_last/g+V_tank*rho_water)
    #GM langsrichting
    It_y = df.iloc[27,2]
    BM_l = It_y/displacement1
    GM_l = KB +BM_l-KG

    #momentstelling stabiliteit
    trim_max = 7/180*np.pi   #of negatieve trimhoek
    theta = trim_max/Lwl

    Msl=rho_water*g*displacement*GM_l*(theta)
    #Msl=rho_water*g*displacement*GM_l*theta
    BB1=It_y/displacement*np.tan(theta)
    return [F_last,GM_t,arm_c,v_max,]
    
def varend(df_varend):   
    rho_staal = 7.85E3
    E_staal=210E9
    rho_water = 1.025E3
    g = 9.81
    nul = np.zeros(1)
    Loa= df_varend.iloc[0,1] +df_varend.iloc[67,0]
    eind = np.array([Loa])
    onderwater= df_varend.iloc[42:64,0]
    COB=df_varend.iloc[20,1]
    COV=df_varend.iloc[21,1]
    x=np.arange(0,Loa,0.05)


    #containers
    Cl=6.06   #container lengte
    Cb=2.44  #container breedte
    Ch=2.59   #container hoogte
    Cw=30E3  #container weight

    #aantal containers
    n=234
    #aantal rijen in de hoogte
    atiers=1
    #aantal containers in breedte
    arij=13
    #aantal containers in lengte
    abay= n/arij


    #opwaartsekracht verdeelde belasting
    p=np.zeros(len(x))

    p = -df_varend.iloc[42:64,1]*rho_water*g
    p = np.append(p,nul)
    p = np.append(nul,p)
    x_p = df_varend.iloc[42:64,0]
    x_p = np.append(0,x_p)
    x_p = np.append(x_p,max(onderwater))
    p_func = interpolate.interp1d(x_p,p)

    #gewicht verdeelde belasting
    G = df_varend.iloc[101:123,2]*rho_staal*g*tp_factor
    #G=np.append(G,nul)
    x_G = df_varend.iloc[101:123,0]
    #x_G=np.append(x_G,eind)
    G_func = interpolate.interp1d(x_G,G)

    #traagheidsmoment over de lengte
    I = df_varend.iloc[101:123,6]*tp_factor
    #I=np.append(I,nul)
    x_I = df_varend.iloc[101:123,0]
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

    G_punt=integrate.quad(G_func,0,Loa)
    P_punt=integrate.quad(p_func,min(onderwater),max(onderwater))


    #som krachten 6 staat voor de 6 meter diepgang
    Fc=Cw*n*g

    Ftank = -1*(G_punt[0] + P_punt[0] +Fc)
    xtank=df_varend.iloc[33,1]
    volumetank=Ftank/rho_water/g

    volumetankmax=df_varend.iloc[32,1]/df_varend.iloc[35,1]*100


    Fillheight=volumetank/volumetankmax

    #som momenten
    LCG_c= -1*(P_punt[0]*COB +G_punt[0]*COV +Ftank*xtank)/Fc

    displacement = df_varend.iloc[18,1]
    gewichtschip=displacement*rho_water
    H=df_varend.iloc[2,1]




    #GM dwarsrichting
    It_x = df_varend.iloc[27,1]
    displacement = df_varend.iloc[18,1]

    KB = df_varend.iloc[20,3]
    KG = df_varend.iloc[21,3]

    #berekening displacement nieuw nadat containers erop zijn
    gewichtschip=displacement*rho_water
    displacement1=(gewichtschip+Cw*n)/rho_water
    BM_t = It_x/displacement1
    KGcont_v=H+(Ch*atiers/2)
    KGtank_v=df_varend.iloc[33,3]

    KG_nieuw= (KG*G_punt[0]/g+KGcont_v*n*Cw+KGtank_v*volumetank*rho_water)/(G_punt[0]/g+n*Cw+volumetank*rho_water)

    GM_t_v = KB + BM_t - KG_nieuw 



    #LCG
    LCF = df_varend.iloc[26,1]
    LCGNieuw=(LCF*G_punt[0]/g+LCG_c*n*Cw+xtank*volumetank*rho_water)/(G_punt[0]/g+n*Cw+volumetank*rho_water)
    #GM langsrichting
    It_y = df_varend.iloc[27,2]
    BM_l = It_y/displacement
    GM_l = KB +BM_l-KG

    #KG1=(KG*gewichtschip+F_tank1/g*tankx+F_cont*VCG_c/g)/(F_cont/g+gewichtschip+F_tank1)



    V_s = df_varend.iloc[152:165,1]
    R_tot = df_varend.iloc[152:165,3]

    R_tot_max = df_varend.iloc[150,3]
    return [GM_t_v, Fillheight*100]


def trendplotinelkeaar(filepath):
    data = ["Last","GM dwars,","arm van de containers"]
    wb = load_workbook(filepath, read_only=True, keep_links=False)
    variable= wb.sheetnames

    for i in variable:
        df = pd.read_excel(filepath,i)
        data = np.vstack((data,beladen(df)))

    variable = [int(numeric_string) for numeric_string in variable]
    figure = plt.figure(figsize=(10,15))
    ax = plt.subplot(111)
#    for i in range(np.shape(data)[1]):
 #       plt.plot(variable,data[1:,i],label=data[0,i])
    plt.plot(variable,data[1:,0],label=data[0,0])
    plt.plot(variable,data[1:,1],label=data[0,1])
    plt.plot(variable,data[1:,2],label=data[0,2])
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


def trendplot(filepath):
    datalabel = [r"Last", r"GM dwars", r"LCG containers",r"$v_{max}$"]
    wb = load_workbook(filepath, read_only=True, keep_links=False)
    variable = wb.sheetnames
    data = [0,0,0,0]
    for i in variable:
        df = pd.read_excel(filepath, i)
        data = np.vstack((data, beladen(df)))

    data = data[1:,]

    variable = [int(numeric_string) for numeric_string in variable]
    
    figure, axes = plt.subplots(np.shape(data)[1], 1, figsize=(8, 12))

    for i, ax in enumerate(axes):
        ax.plot(variable, data[:,i], label=datalabel[i])
#        ax.set_xlabel('[m]')
#        ax.set_ylabel('[N/m]')
        ax.set_title(datalabel[i])
        ax.grid()
        ax.legend()

    # Adjust spacing between subplots
    plt.tight_layout()
    plt.show()

trendplot("breedte verandering.xlsx")