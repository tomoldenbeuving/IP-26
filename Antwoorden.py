import pandas as pd
from imports import df,atiers,n,arij,abay,Ch
from Sterkteleerbeladen import F_last,arm_c,F_tank,x_tank,M_max,Loc_M_max,tp_factor,v_max,Loc_v_max,eind_cont,Loa,F_c,G_punt,P_punt,g,rho_water
from Stabiliteitbeladen import KGtank,KGcont,KG_nieuw,LCGNieuw,GM_t
from Stabiliteitvarend import displacement, LCG_c, KGcont_v, GM_t_v, R_tot_max,Fillheight,Ftank,KGtank_v,xtank
from Stabiliteitleeg import dp_leeg,Gschip_leeg,COB_leeg,KB_leeg,KG_romp_leeg,BM_leeg_t,BM_leeg_l,GM_leeg_l,GM_leeg_t,theta,Foutmarge


F=F_last+F_tank+G_punt+P_punt+F_c
dp=P_punt/rho_water/g
print("\n \n")
print("Foutmarge, leegscheepse conditie",Foutmarge,'%')
print('Blokcoeëficiënt',df.iloc[19,1]/(df.iloc[0,1]*df.iloc[1,1]*df.iloc[2,1]))
print('Last=',F_last)
print('Vulhoogte tank varend=',Fillheight*100,'%')
print('GM dwarsscheeps varend=', GM_t_v)
print('GM dwarsscheeps beladen=',GM_t)
print('LCG containers beladen=',arm_c)
print("uitstekende containers",eind_cont-df.iloc[0,1])
print('Weerstand bij 19kts=', R_tot_max)
print("\n \n")


def tabel():
    print('LOA=',df.iloc[0,1])
    print('Breedte=',df.iloc[1,1])
    print('MidshipLength=',df.iloc[6,1]-df.iloc[5,1])
    print('Last=',F_last)
    print('Aantal containers=',n)
    print('Aantal tiers=',atiers)
    print('Aantal rows=',arij)
    print('Aantal bays=',abay)
    print('LCG containers beladen=',arm_c)
    print('VCG containers beladen=',KGcont)
    print('Vulhoogte tank beladen=',df.iloc[35,1])
    print('Ballast tank gewicht=',F_tank)
    print('KG ballast tank beladen=',KGtank)
    print('LCG ballast tank=',x_tank)
    print('KG totaal beladen=',KG_nieuw)
    print('LCG totaal beladen=',LCGNieuw)
    print('GM dwarsscheeps beladen=',GM_t)
    print('Maximaal moment=',M_max)
    print('Locatie maximaal moment=',Loc_M_max)
    print('Plaatdikte=',tp_factor)
    print('Maximale doorbuiging=',v_max)
    print('Locatie maximale doorbuiging=',Loc_v_max)
    print('Deplacement gesleept=',displacement)
    print('LCG ballast containers gesleept=',LCG_c)
    print('VCG ballast containers gesleept=',KGcont_v)
    print('GM dwarsscheeps varend=', GM_t_v)
    print('Weerstand bij 19kts=', R_tot_max)
    print('Cstern=',df.iloc[7,2])
    print('Vulhoogte tank varend=',Fillheight*100,'%')
    print('Ballast tank gewicht varend=',Ftank)
    print('KG ballast tank varend=',KGtank_v)
    print('LCG ballast tank varend=',xtank)
    print('Deplacement leeg=',dp_leeg)
    print('LSW=',Gschip_leeg[0])
    print('Longitudonaal COB zonder trim leeg=',COB_leeg)
    print('Berekende trim (graden)',theta)
    print('KB leeg=',KB_leeg)
    print('KG staal=',KG_romp_leeg)
    print('BM leeg dwarsscheeps=',BM_leeg_t)
    print('BM leeg langsscheeps=', BM_leeg_l)
    print('GM leeg dwarsscheeps=',GM_leeg_t)
    print('GM leeg langsscheeps=', GM_leeg_l)

tabel()