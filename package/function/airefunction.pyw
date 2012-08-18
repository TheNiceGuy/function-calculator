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
def triangle(arglist):
    alargeur  = arglist[0][1]
    aapotheme = arglist[3][1]
    return (alargeur * aapotheme) / 2

def rectangle(arglist):
    alargeur = arglist[0][1]
    alongeur = arglist[1][1]
    return alargeur * alongeur

def polygone(arglist):
    anombrecote = arglist[4][1]
    alargeur    = arglist[0][1]
    aapotheme   = arglist[3][1]
    return (anombrecote * alargeur * aapotheme) / 2

def cercle(arglist):
    arayon = arglist[2][1]
    return math.pi * pow(arayon, 2)
#--------------------------MAIN-------------------------------
if __name__ == "__main__": 
    os.system("pause")