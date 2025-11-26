szoveg = ""

try:
    with open("scifi_input_v2.txt",encoding = 'utf-8')as fajl:
        szoveg = fajl.read()
        #print(szoveg)
except IOError as ex:
    print(ex)

# -----------------------------------------------

def feladat1():
    kiir = ""
    lista = szoveg.strip().split('**')
    
    for i in range (len(lista)):
        lista[i]=lista[i].strip()

    db = 0
    for i in range (len(lista)):
        if (len(lista[i]) > 0):
            lista[db] = lista[i]
            db += 1
    for i in range(db,len(lista)):
        lista.pop()
    
    for sz in lista:
        kiir += sz + "\n"    
    
    return kiir


def feladat2():
    for i in range(len(lista)):
        lista[i]=lista[i].lower()

    #print(lista)    

    for i in range(0, len(lista), 2):
        lista2 = lista[i].split(' ')
        lista2[0] = lista2[0].upper()
        #lista[i] = lista2[0] + lista2[1]  
        szo = " "
        for j in range(len(lista2)):
            szo += lista2[j] + " "   
        lista[i] = szo.strip()    
    print(lista)

    try:
        with open("scifi_output.txt","w",encoding = 'utf-8')as fajl:
            for i in lista:
                fajl.write(i + "\n") 
            #print(szoveg)
    except IOError as ex:
        print(ex)










# -----------------------------------------------

try:
    with open("scifi_output.txt","a",encoding = 'utf-8')as fajl:
        fajl.write(feladat1() + "\n")    
        #fajl.write(feladat2())
        #fajl.write(feladat3())
        #fajl.write(feladat4())
        #fajl.write(feladat5())
        #fajl.write(feladat6())
        #fajl.write(feladat7())
except IOError as ex:
    print(ex)





























"""

    
#3. feladat
szoveg=szoveg.replace(".", "").replace(",", "").replace("*", "")
print(szoveg)

lista=szoveg.strip().split(' ')
print(lista)

try:
    with open("scifi_output.txt","a",encoding = 'utf-8')as fajl:
        fajl.write(str(len(lista)) + "\n") 
except IOError as ex:
    print(ex)

#4. feladat
aslista = []

for elem in lista:
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

for elem in lista:
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

for elem in lista:
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
