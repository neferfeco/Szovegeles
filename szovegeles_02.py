import string

#1. feladat
betu = ""

try:
    with open("string_input.txt",encoding = 'utf-8')as fajl:
        betu = fajl.read()
except IOError as ex:
    print(ex)

betu = betu.strip()

#2. feladat
db_szam = 0
db_betu = 0

for i in  betu:
    if i in string.digits:
        db_szam += 1

for i in  betu:
    if i in string.ascii_letters:
        db_betu += 1



print (db_szam)

print (db_betu)