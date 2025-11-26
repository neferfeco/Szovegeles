szoveg = ""
try:
    with open("scifi_input_v2.txt",encoding = 'utf-8')as fajl:
        szoveg = fajl.read()
        #print(szoveg)
except IOError as ex:
    print(ex)

    
# 1. feladat
lista=szoveg.strip().split('**')
for i in range (len(lista)):
    lista[i]=lista[i].strip()
"""for sor in lista:
    if (len(sor)==0):
        lista.remove(sor)
"""
db = 0
for i in range (len(lista)):
    if (len(lista[i]) > 0):
        lista[db] = lista[i]
        db += 1
for i in range(db,len(lista)):
    lista.pop()
#print(lista)

# 2. feladat
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

'''
szoveg_kis = szoveg.lower()

for i in range(len(szoveg_kis)):
    if ():
'''















