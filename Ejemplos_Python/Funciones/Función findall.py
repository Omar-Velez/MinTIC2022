# -*- encoding: utf-8 -*-
'''
La función findall() devuelve una lista que contiene todas las coincidencias.
*****************************************************************************
'''
# Importando librerias
import re

##############################################################################################
# El siguiente ejemplo verifica si existen números en la cadena y devuelve una lista.        #
##############################################################################################

variable = re.compile(r'\d+')
lista = variable.findall('11 es un número y 12 también')
print(lista)
if lista:
    print("Si, hay al menos una coincidencia!")
else:
    print("No hay coincidencias")