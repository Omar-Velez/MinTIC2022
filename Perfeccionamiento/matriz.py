matriz=[]

for f in range(3):
    matriz.append([])
    for c in range(3):
        matriz[f].append(input("digite un valor: "))
#print(matriz)
for fila in matriz:
    for valor in fila:
            print("\t", valor, end="")
    print()