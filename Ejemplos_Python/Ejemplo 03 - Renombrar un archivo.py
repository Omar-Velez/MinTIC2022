# -*- encoding: utf-8 -*-
'''
Ejemplo que permite renombrar un archivo en una ubicacion especifica.
*********************************************************************
'''
# Importando librerias especificas "rename"
from os import rename

##############################################################################################
# "archivo" define la ruta del archivo a modificar el nombre                                 #
# por medio de un "for" de imprime cada linea del archivo                                    #
##############################################################################################

archivo = "Files/test_Crear_Archivo_de_Texto.txt" # Definimos la ubicacion del archivo
nuevoNombre = "Files/modificado_Crear_Archivo_de_Texto.txt" # Definimos el nuevo nombre del archivo

# Se llama la funcion importada de la libreria os
rename(archivo, nuevoNombre)