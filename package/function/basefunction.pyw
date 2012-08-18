# -*-coding:Latin-1 -*
#-------------------------MODULE------------------------------
import math
import os
#------------------------FUNCTION-----------------------------
# 0 = airelargeur
# 1 = airelongeur
# 2 = airerayon
# 3 = aireapotheme
# 4 = airenombrecote
# 5 = volumelargeur
# 6 = volumelongeur
# 7 = volumehauteur
# 8 = volumerayon
# 9 = volumeapotheme
#10 = volumenombrecote
#11 = Cathète 1
#12 = Cathète 2
#13 = Hypoténuse
#14 = base
def baserectangle(arglist):
    vlargeur = arglist[5][1]
    vlongeur = arglist[6][1]
    return vlargeur * vlongeur

def basepolygone(arglist):
    vnombrecote = arglist[10][1]
    vlargeur    = arglist[5][1]
    vapotheme   = arglist[9][1]
    return vnombrecote * vlargeur * vapotheme / 2

def basecercle(arglist):
    vrayon = arglist[8][1]
    return math.pi * pow(vrayon,2)
#--------------------------MAIN-------------------------------
if __name__ == "__main__": 
    os.system("pause")