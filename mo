1.
lista = szoveg.split('**')

i = 0
for sor in lista:
    if len(sor) > 0:
        lista[i] = sor.strip()
        i += 1

if i < len(lista):
    for j in range(i, len(lista)):
        lista.pop()

for sor in lista:
    print(f"--{sor}--")






