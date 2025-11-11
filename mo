1.
print("---MO---")
lista2 =  []
lista = szoveg.split('**')

for sor in lista:
    if len(sor) > 0:
        lista2.append(sor.strip('**').strip())

for sor in lista2:
    print(f"--{sor}--")






