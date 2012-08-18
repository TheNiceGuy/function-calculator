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
def prisme(arglist):
    base     = arglist[14][1]
    vhauteur = arglist[7][1]
    return base * vhauteur

def pyramide(arglist):
    base     = arglist[14][1]
    vhauteur = arglist[7][1]
    return (base * vhauteur) / 3

def sphere(arglist):
    vrayon    = arglist[8][1]
    return (4 * math.pi * pow(vrayon, 3)) / 3
#--------------------------MAIN-------------------------------
if __name__ == "__main__": 
    os.system("pause")