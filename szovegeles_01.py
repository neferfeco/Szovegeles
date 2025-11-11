szoveg = ""
try:
    with open("scifi_input_v2.txt",encoding = 'utf-8')as fajl:
        szoveg = fajl.read()
        #print(szoveg)
except IOError as ex:
    print(ex)

    
#1. feladat
lista = []
szoveg.strip().split('**')
print(szoveg.strip().split('** '))




















