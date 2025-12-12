#################################################
###   FÜGGVÉNYEK                              ###
#################################################

def adat_beolvasas_fajlbol():
    # A szoveg név globális változóként történő használatának lehetővé tétele (tartalmának módosíthatóságához)
    global szoveg
    
    # Szövegfájl beolvasása kivétel- és erőforrás-kezeléssel.
    try:
        with open("F1\\scifi_input_v2.txt", encoding = 'utf-8')as fajl:
            szoveg = fajl.read()

    except IOError as ex:
        print(ex)


def feladat1():
    # A sorok_lista név globális változóként történő használatának lehetővé tétele (tartalmának módosíthatóságához)
    global sorok_lista
    kiirando = ""
    
    # A beolvasott szöveg végéről az Enter eltávolítása (strip), majd a szöveg feldarabolása '**' karakterpáros mentén
    sorok_lista = szoveg.strip().split('**')
    
    # A feldarabolt szövegrészek elejéről és végéről a szóközök eltávolítása
    for i in range (len(sorok_lista)):
        sorok_lista[i] = sorok_lista[i].strip()

    db = 0
    
    # A lista elejére másoljuk a nem üres elemeket
    for i in range (len(sorok_lista)):
        if (len(sorok_lista[i]) > 0):
            sorok_lista[db] = sorok_lista[i]
            db += 1
    
    # A lista végéről eltávolítjuk a felesleges elemeket
    for i in range(db,len(sorok_lista)):
        sorok_lista.pop()
    
    # A fájlba írandó sor a 4. listaelem
    kiirando = sorok_lista[3]

    return kiirando


def feladat2():
    # A sorok_lista név globális változóként történő használatának lehetővé tétele (tartalmának módosíthatóságához)
    global sorok_lista

    # Minden listaelem kisbetűssé alakítása
    for i in range(len(sorok_lista)):
        sorok_lista[i] = sorok_lista[i].lower()

    # Minden cím (minden páratlan indexű listaelem) első szavának nagybetűssé alakítása
    for i in range(0, len(sorok_lista), 2):
        
        # A sor feldarabolása szóközöknél, hogy megkaphassuk a címben lévő szavakat
        szavak = sorok_lista[i].split(' ')
        
        # Az első szó nagybetűssé alakítása
        szavak[0] = szavak[0].upper()
        
        # A cím összefűzése már az új formátumú első szóval
        uj_cim = ""
        
        for j in range(len(szavak) - 1):
            uj_cim += szavak[j] + " "
        
        uj_cim += szavak[-1]
        
        sorok_lista[i] = uj_cim

    
def feladat3():    
    # A szoveg változóból eltávolítjuk először a '.'-okat, majd a ','-ket, végül a '*'-okat
    szoveg2 = szoveg.replace(".", "").replace(",", "").replace(":", "").replace("*", "")
    
    # A szöveget alkotó szavak listáját a szöveg szóközök mentén történő feldarabolásával kapjuk meg. A darabolás előtt eltávolítjuk a szöveg végéről az Entert (strip).
    szo_lista = szoveg2.strip().split(' ')
        
    return szo_lista


def feladat4():
    pass


def feladat5():
    pass


def feladat6():
    pass


def feladat7():
    pass



#################################################
###   A PROGRAM                               ###
#################################################

### GLOBÁLIS VÁLTOZÓK ###

# Változó létrehozása a beolvasott szöveg tárolásához.
szoveg = ""

# A szekciókra tördelt szöveget tároló lista létrehozása a további feladatok megkönnyítésére.
# Minden listaelem egy sornyi szöveget tárol majd.
sorok_lista = []



### VÉGREHAJTÁS ###

adat_beolvasas_fajlbol()

# Feladatok végrehajtása és az eredmények fájlba írása
try:
    with open("F1\\scifi_output.txt","w",encoding = 'utf-8')as fajl:
        # 1. feladat
        fajl.write(f"1. feladat:\n\t{feladat1()}\n\n")
        
        # 2. feladat               
        feladat2()
 
        sz = ""
        for le in sorok_lista:
            sz += le + " "
                     
        fajl.write(f"2. feladat:\n\t{sz.strip()}\n\n")

        # 3. feladat
        fajl.write(f"3. feladat:\n\tA szöveg {len(feladat3())} szóból áll.\n\n")
        
        # 4. feladat

        # 5. feladat

        # 6. feladat

        # 7. feladat
        
except IOError as ex:
    print(ex)



#################################################
###   PROGRAM VÉGE                            ###
#################################################



"""
#4. feladat
aslista = []

for elem in sorok_lista:
    if elem.lower().endswith("és") and elem not in aslista:
        aslista.append(elem)
print(aslista)

try:
    with open("scifi_output.txt","a",encoding = 'utf-8')as fajl:
        
        for elem in aslista:
            fajl.write(elem+"\n")
        
except IOError as ex:
    print(ex)


#5. feladat
alista = []

for elem in sorok_lista:
    if elem.lower().startswith("a") and (elem.lower() not in ["a","az"]):
        alista.append(elem)
print(len(alista))


#6. feladat
try:
    with open("scifi_output.txt","a",encoding = 'utf-8')as fajl:
        fajl.write(str(szoveg.find("jövőben")) + "\n")
except IOError as ex:
    print(ex)
    
    
#7.feladat
hosszulista = []

for elem in sorok_lista:
    elem=elem.lower()
    if len(elem)>=10 and elem not in hosszulista:
        hosszulista.append(elem)
hosszulista.sort()
print(hosszulista)

try:
    with open("output.txt","w",encoding = 'utf-8')as fajl:
        
        for elem in hosszulista:
            fajl.write(elem+"\n")
        
except IOError as ex:
    print(ex)
"""
