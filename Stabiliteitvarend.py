from Sterkteleerbeladen import Cw, n, F_c, P_punt, COB, G_punt, COV, F_tank, x_tank

LCG_c= -1*(P_punt[0]*COB +G_punt[0]*COV +F_tank[0]*x_tank)/F_c

print(COB, COV)
