# -*- encoding: utf-8 -*-
'''
La función match() devuelve None si no encuentra ninguna coincidencia.
**********************************************************************
'''
# Importando librerias
import re

##############################################################################################
# Si tienen éxito, se devuelve una instancia de objeto de coincidencia, que contiene         #
# información sobre la coincidencia: dónde comienza y finaliza, la subcadena que coincidió   #
# y más.                                                                                     #
##############################################################################################
# El siguiente ejemplo verifica si en una cadena se encuentra una dirección de correo válida #
##############################################################################################

validacion = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
email = "correo.prueba@dominio.com"

if re.match(validacion, email) is None:
    print("No es dirección de correo válida")
else:
    print("Es dirección de correo válida")