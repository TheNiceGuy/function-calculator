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
def cathete(arglist):
    cathete     = arglist[11][1]
    hypothenuse = arglist[13][1]
    if cathete <= hypothenuse:
        return math.sqrt(pow(hypothenuse, 2) - pow(cathete, 2))
    return "Error: Cathète > Hypothénuse"

def hypothenuse(arglist):
    cathete1     = arglist[11][1]
    cathete2     = arglist[12][1]
    return math.sqrt(pow(cathete1, 2) + pow(cathete2, 2))

#--------------------------MAIN-------------------------------
if __name__ == "__main__": 
    os.system("pause")