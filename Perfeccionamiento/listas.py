lista=[0,1,2,3,4,5,6,7,8,9,10]

# Ejemplo 1
print("\n # Recorrido normal #")
for recorrido in range (len(lista)): # Recorre desde el indice 0 (primero)
    print (recorrido)

# Ejemplo 2
print("\n # Recorrido Inverso #")
inverso=-1
for recorrido in range (len(lista)): # Recorre desde el indice -1 (ultimo)
    print (lista[inverso])
    inverso-=1

# Ejemplo 3
print("\n # Eliminando el ultimo item de la lista #")    
print(f"lista al iniciar: {lista}\n")
while lista:
    print(f"Eliminando el item {lista[-1]}")
    lista.pop(-1)
print(f"\nlista al finalizar: {lista}")