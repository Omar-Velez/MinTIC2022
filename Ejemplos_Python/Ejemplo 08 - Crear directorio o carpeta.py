# -*- encoding: utf-8 -*-
'''
Ejemplo que permite crear un directorio o carpeta en una ubicacion especifica.
******************************************************************************
'''
# Importando librerias especificas "copyfile"
import os

##############################################################################################
# Se puede crear directorios con 2 funciones mkdir o makedirs                                #
# mkdir -> crea un directorio, seo genera error al crear en cascada mas direcorios: mkdir -p #
# makedirs -> crea directorios en cascada: mkdir -p                                          #
##############################################################################################

# Se define el nombre de la carpeta o directorio a crear
directorio = "Files/mintic"

# se hace un try con el comando mkdir para crear un directorio
try:
    os.makedirs(directorio)
# si se genera error se atrapa y se imprime el fallo
except OSError:
    print("La creación del directorio %s falló" % directorio)
# si es correcto indica la creacion del directorio
else:
    print("Se ha creado el directorio: %s " % directorio)