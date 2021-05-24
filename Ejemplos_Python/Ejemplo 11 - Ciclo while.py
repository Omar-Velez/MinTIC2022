El bucle o ciclo while es muy sencillo en Python. Con el bucle while podemos ejecutar un conjunto de sentencias siempre que una condición sea verdadera.


i = 1
while i < 10:
    print(i)
    i += 1
A diferencia de la sentenecia for, la variable con la que controlamos el número de iteraciones normalmente se inicializa antes y fuera del while, pero esto depende mucho de la forma en la que uses la sentencia en tu código.

El ejemplo que te mostramos, sólo imprime una secuencia del 1 al 9.


Desde luego, el ciclo o bucle while soporta el uso de las sentencias break y continue.



while y break

i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
Este ejemplo imprime una secuencia desde 1 hasta 5, la sentencia break interrumpe las iteraciones restantes.


while y continue

i = 1
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
En este ejemplo se omite la impresión del número 5, la sentencia continue interrumpe la iteración en curso y no se imprime nada hasta la siguiente iteración.


Esperamos que estos ejemplos te dejen claro el funcionamiento de while.