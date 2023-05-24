import pandas as pd
from Sterkteleerbeladen import F_last,n,atiers,arij,abay,arm_c,F_tank,x_tank,M_max,Loc_M_max,tp_factor,v_max,Loc_v_max
from Stabiliteitbeladen import KGtank,KGcont,KG_nieuw,LCGNieuw,GM_t
from Stabiliteitvarend import displacement, LCG_c

df = pd.read_excel("IP.xlsx",'VB schip van Goris')

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
print('Vulhoogte tank=',df.iloc[35,1])
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
print('VCG ballast containers gesleept=',)