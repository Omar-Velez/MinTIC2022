numeros=[]
suma=0
numero=1

while numero != 0:
    try:
        numero=float(input("Digite un numero: "))
        numeros.append(numero)
        suma += numero
    except ValueError as err:
        print("Se ha producido el siguiente error: {0}".format(err))

numeros.pop(-1)

print(f"numeros ingresados: {numeros}")
print(f"la suma de todos los numeros es igual a {0}".format(suma))