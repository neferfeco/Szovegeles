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
    # 'és'-ra végződő szavak kigyűjtésére szolgáló lista létrehozása
    es_lista = []

    szo_lista = feladat3()
    
    # 'és'-re végződő szavak kigyűjtése. Mivel írásmódtól függetlenül keressük ezeket a szavakat, ezért előtte egységesen kisbetűs írásmódúra változtatjuk őket
    for szo in szo_lista:
        if szo.lower().endswith("és") and szo not in es_lista:
            es_lista.append(szo)
    
    return es_lista


def feladat5():
    # Az 'a'-val kezdődő szavak kigyűjtésére szolgáló lista létrehozása
    a_lista = []

    szo_lista = feladat3()

    # 'a'-val kezdődő szavak kigyűjtése. Mivel írásmódtól függetlenül keressük ezeket a szavakat, ezért előtte egységesen kisbetűs írásmódúra változtatjuk őket, valamint kizárjuk a névelőket
    for szo in szo_lista:
        if szo.lower().startswith("a") and (szo.lower() not in ["a", "az"]):
            a_lista.append(szo)
    
    #print(a_lista)
    return a_lista


def feladat6():    
    return szoveg.find("jövőben")


def feladat7():
    # A legalább 10 karakter hosszú szavak kigyűjtésére szolgáló lista létrehozása
    hosszu_lista = []

    szo_lista = feladat3()

    for szo in szo_lista:
        # A szavak kisbetűssé alakítása, hogy elkerüljük a különböző írásmódú azonos szavak kigyűjtését és mert a rendezés csak így lesz helyes
        szo = szo.lower()
        
        # A 10 karakternél hosszabb és még nem kigyűjtött szó kigyűjtése
        if len(szo)>=10 and szo not in hosszu_lista:
            hosszu_lista.append(szo)

    # A kigyűjtött szavakat tartalmazó lista rendezése
    hosszu_lista.sort()
    
    return hosszu_lista



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
        fajl.write(f"4. feladat:\n")
        
        lista = feladat4()
                
        for es_szo in lista:
            fajl.write(f"\t{es_szo}\n")

        fajl.write(f"\n")

        # 5. feladat
        fajl.write(f"5. feladat:\n\t'a' betűvel kezdődő szavak száma: {len(feladat5())}\n\n")

        # 6. feladat
        fajl.write(f"6. feladat:\n\tA 'jövőben' szó a {feladat6()}. pozíciótól kezdve fordul elő először a szövegben.\n\n")

        # 7. feladat
        fajl.write(f"7. feladat:\n")
        
        lista = feladat7()
        
        for hosszu_szo in lista:
            fajl.write(f"\t{hosszu_szo}\n")
        
except IOError as ex:
    print(ex)



#################################################
###   PROGRAM VÉGE                            ###
#################################################


