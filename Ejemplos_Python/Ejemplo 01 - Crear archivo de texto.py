# -*- encoding: utf-8 -*-
'''
Ejemplo que permite crear un archivo de texto con un salto de linea.
********************************************************************
'''
# Importando librerias
import os
import codecs

##############################################################################################
# Se define la ubicacion del archivo a crear, se guarda en la carpeta "Files"                #
# se crea una variable "archivo" y se asigna un objeto del tipo codecs (libreria importada)  #
# codecs.open crea el documento en la ruta especificada y se envia el parametro de           #
# codificacion en utf-8 para que nos acepte tildes y caracter ñ entre otros                  #
##############################################################################################

archivo = codecs.open("Files/test_Crear_Archivo_de_Texto.txt", "w", "utf-8-sig") # ,w (Write ~ Escribir) ,"utf-8-sig" (Codificacion en español).
archivo.write("Primera línea" + os.linesep) # Se manda la primera linea que se escribe en el texto + os.linesep (separador de linea).
archivo.write("Segunda línea") #  Se escribe la segunda frase que ira en el salto de linea.
archivo.close() # se cierra la orden de escritura.