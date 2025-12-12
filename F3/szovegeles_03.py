#1. feladat
szoveg = ''

try:
    with open ("input.txt", "r", encoding="utf-8") as file:
        szoveg = file.read()
        
except IOError as hiba:
    print(hiba)

def feladat1():
    szoveg_szelet = szoveg.strip().split('\n')
    karakterek = 0
        
    for szoveg1 in szoveg_szelet:
        karakterek += len(szoveg1)
    
    return karakterek

def feladat1_2():
    szavak = szoveg.split(' ')
    
    return len(szavak)







# ****************************
#  A PROGRAM
# ****************************

try:
    with open ("output.txt", "w", encoding="utf-8") as file:
        file.write(f"1.feladat: {feladat1()}    \n")
        file.write(f"1_2. feladat: {feladat1_2()}    \n")
except IOError as hiba:
    print(hiba)
    







































