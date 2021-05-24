uizás el tipo de sentencia más conocido es la sentencia if. Aquí tenemos un ejemplo:

i = 0
if i < 5:
    print('i es menor que 5')
Al ejecutar el código obtenemos este resultado:



Esta es la forma más básica de la sentencia if en Python.

Sin embargo, existen otras variantes como el if-else.

i = 6
if i < 5:
    print('i es menor que 5')
else:
    print('i es mayor que 5')
El código debajo de else, se ejecutará si la condición resulta falsa.  Al ejecutar este código obtenemos lo siguiente:



Finalmente, podemos combinar if-else con otros ifs. Como en el ejemplo siguiente:

# decodigo.com
i = 5
if i < 5:
    print('i es menor que 5')
elif i == 5:
    print('i es igual a 5')
else:
    print('i es mayor que 5')
Al ejecutar el código, obtendrás lo siguiente:

