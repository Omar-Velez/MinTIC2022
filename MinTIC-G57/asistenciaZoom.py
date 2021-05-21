# importamos la libreria os
from itertools import chain

# declaramos una variable para almacenar datos principales (nombre en zoom, hora del mensaje)
# declaramos una variable para almacenar las respuestas
datos=[]
respuestas=[]

# Abrimos el documento de asistencia
asistencia = open("asistencia.txt", "r")
# preparamos el documento csv
csvDocument = open("asistencia.csv", "w")

# leemos la el listado de asistencia
cadena=asistencia.readlines()

# guardamos en la variable datos las lineas impares, 
# en la variable respuestas las lineas pares
lineas=0
for linea in cadena:
    if lineas%2==0:
        datos.append(linea.split())
    else:
        respuestas.append(linea.split())
    lineas+=1

# hacemos una limpieza en cada lista
# ['De', 'Ana', 'Meliza', 'Alvarez', 'Reyes', 'para', 'todos:', '09:15', 'PM']
#   0      1        2         3         4        5        6        7       8    -> Indice positivo
#  -9     -8       -7        -6        -5       -4       -3       -2      -1    -> Indice negativo
recorrido=0 # el primer indice es 0
# validamos el largo de la lista (numero de lineas par o impar) con len(lista)
while recorrido < len(datos): # len(datos) -> 29 
    # Borra el indice -3 'todos:'
    datos[recorrido].pop(-3)
    # la lista pierde un item ahora 'para' es el indice -3
    datos[recorrido].pop(-3)
    # borra el indice 0 'De'
    datos[recorrido].pop(0)
    # insertamos en la posicion -2 (antes de '09:15' un ';' para usarlo de separador en el CSV)
    datos[recorrido].insert(-2, ";")
    # insertamos al final de la lista un ';' para usarlo de separador en el CSV
    datos[recorrido].append(";")
    recorrido+=1

# hasta este punto, solo falta concatenar todo en un listado y guardarlo como CSV
lista=""
recorrido=0 # el primer indice es 0
while recorrido < len(datos): # len(datos) -> 29 
    lista=datos[recorrido]+respuestas[recorrido]
    csvDocument.write("".join(lista))
    csvDocument.write("\n")
    recorrido+=1
