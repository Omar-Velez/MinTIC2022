# -*- encoding: utf-8 -*-
'''
Ejemplo que permite leer un archivo de texto en una ubicacion especifica.
*************************************************************************
'''
# Importando librerias
import codecs

##############################################################################################
# Se define la ubicacion del archivo a abrir, se guarda en una variable temporal "archivo"   #
# por medio de un "for" de imprime cada linea del archivo                                    #
##############################################################################################

with codecs.open("Files/test_Crear_Archivo_de_Texto.txt","r","utf-8-sig") as archivo:  # ,r (read ~ leer) ,"utf-8-sig" (Codificacion en español).
    for linea in archivo: # recorre el archivo segun su numero de lineas
        print(linea) # Imprime la linea