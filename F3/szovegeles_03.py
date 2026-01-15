#1. feladat
import string
szoveg = ''

try:
    with open ("F3//input.txt", "r", encoding="utf-8") as file:
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

def feladat2():
    kisbetus = szoveg.lower()
    
    for i in kisbetus:
        if i in string.punctuation:
            kisbetus = kisbetus.replace(i,"")
    
    return kisbetus

def feladat3():
    pass

def feladat4():
    kulcsszo = []
    
    szavak = feladat2().strip()
    szavak2 = szavak.split(' ')
    
    for szo in szavak2:
        if len(szo) >= 7 and szavak.count(szo) >= 2:
            if szo not in kulcsszo:
                kulcsszo.append(szo)

    return kulcsszo

def feladat5():
    global szoveg
    
    db = szoveg.count("MI")
    
    szoveg = szoveg.replace("MI", "Mesterséges Intelligencia")
    
    return db    


def leghosszabb_mondat():
    mondatok = []
    
    # Üres sorok eltávolítása
    szoveg2 = szoveg.strip().replace("\n", " ")
    
    
    j = 0    
    for i in range(0, len(szoveg2)):
        if szoveg2[i] == "." or szoveg2[i] == "?" or szoveg2[i] == "!":            
            mondatok.append(szoveg2[j:i+1])
            j = i + 2
    
    # MAXIMUM KIVÁLASZTÁS
    max_i = 0
    
    for i in range(1, len(mondatok)):
        if len(mondatok[i]) > len(mondatok[max_i]):
            max_i = i
    
    return mondatok[max_i]







# ****************************
#  A PROGRAM
# ****************************

try:
    with open ("output.txt", "w", encoding="utf-8") as file:
        file.write(f"1.feladat: {feladat1()}\n")
        file.write(f"1_2. feladat: {feladat1_2()}\n")
        file.write(f"4 feladat: {sorted(feladat4())}\n")
        file.write(f"{feladat5()}* fordul elő a szövegben az MI szó.\n")
        file.write(f"A leghosszabb mondat:\n\t{leghosszabb_mondat()}")
except IOError as hiba:
    print(hiba)
    
#print(feladat2())


    





































