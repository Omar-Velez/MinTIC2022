# -*- encoding: utf-8 -*-
'''
Ejemplo que permite borrar un archivo en una ubicacion especifica
*****************************************************************
'''
# Importando librerias especificas
from os import remove
from os import path

##############################################################################################
# Opcion 1: Se define la ubicacion del archivo a borrar, ubicado en la carpeta "Files"       #
# Opcion 2: Se comprueba que exista el archivo y se procede a borrrar                        #
##############################################################################################

# Opcion 1
# Se ejecuta el codigo para borrar un archivo en la ruta especificada
remove('Files/test_Crear_Archivo_de_Texto.txt')

# Opcion 2:
# Se valida que el archivo exista en la ubicacion definida
if path.exists("Files/test_Crear_Archivo_de_Texto.txt"):
    remove('Files/test_Crear_Archivo_de_Texto.txt')
else:
    print("Archivo no existe en ubicacion especificada")