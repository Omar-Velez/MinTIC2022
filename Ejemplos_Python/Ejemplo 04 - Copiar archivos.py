# -*- encoding: utf-8 -*-
'''
Ejemplo que permite copiar un archivo de a ubicacion especifica.
****************************************************************
'''
# Importando librerias especificas "copyfile"
from shutil import copyfile

##############################################################################################
# "fuente" define la ruta del archivo a copiar                                               #
# "destino" define la ruta del nuevo archivo copiado                                         #
##############################################################################################

fuente = "Files/modificado_Crear_Archivo_de_Texto.txt"
destino = "Files/test_Crear_Archivo_de_Texto.txt"
copyfile(fuente, destino)
