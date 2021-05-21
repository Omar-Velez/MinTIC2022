'''
Para la solución de este problema, se requiere que el usuario escriba un script y defina una función llamada separar().
Como parámetro de entrada recibe una lista de numero de enteros. La lista debe crearla como lista=[1,2,3,4].
La función devuelve dos listas de la forma: lista1=[Numeros pares], lista2=[numeros impares]
'''
# declaramos la lista de numeros y las listas que recibiran el listado de enteros e impares
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista1,lista2=[],[]

# funcion que recibe una lista y regresa dos listas
def separar(listado):
    lista1=[]
    lista2=[]
    for numero in range(0, len(listado)):
        if listado[numero] % 2 == 0:
            lista1.append(listado[numero])
        else:
            lista2.append(listado[numero])
    return lista1,lista2

# llamamos la funcion que retorna 2 listas
lista1,lista2=separar(lista)

# Imprimimos el resultado
print(f"Del listado {lista}, separamos en numeros Pares e Impares:")
print(f"Numeros Pares: {lista1}")
print(f"Numeros Impares: {lista2}")
