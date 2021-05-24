print("\n+++ for i in range(5, 10): +++")
print("Usando la función range(), se itera sobre una secuencia que va desde 5 hasta 9 (no se incluye el 10).")
print("Al ejecutar el código obtenemos este resultado: 5 6 7 8 9\n")
for i in range(5, 10):
    print(f"iteracion {i-5}:",i)

print("\nUna forma de simplificar el uso de range() es usando sólo el valor máximo:\n")
print("La función range() devuelve valores que van desde 0 hasta 10, no fue necesario\nespecificar que comienza desde 0.")
print("\n+++ Al ejecutar el código obtenemos este resultado: 0 1 2 3 4 5 6 7 8 9 +++\n")
for i in range(10):
    print(f"iteracion {i}:", i)

print("\n+++ for i in range(0, 10, 2): +++")
print("El ciclo for con la función range(), también permite iterar sobre un rango no sólo haciendo incrementos en 1,\ntambién se puede hacer el incremento especificando un valor como se muestra a continuación:\n")
for i in range(0, 10, 2):
    print(f"iteracion {i}:",i)

print("\n+++ for i in range(0, -10, -2): +++")
print("El resultado son dos secuencias de valores donde en cada iteración el incremento es de 2 y -2.\n")
for i in range(0, -10, -2):
    print(f"iteracion {i}:",i)

