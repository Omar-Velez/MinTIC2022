# -*- encoding: utf-8 -*-
'''
Ejemplo que permite leer un archivo XML de una ubicacion especifica.
********************************************************************
'''
# Importando librerias
from xml.dom import minidom

##############################################################################################
# Primero se lee el documento xml y se selecciona el TagName para seleccionar datos a leer   #
##############################################################################################

doc = minidom.parse("Files/datos.xml")
nombre = doc.getElementsByTagName("nombre")[0]
print(nombre.firstChild.data)
empleados = doc.getElementsByTagName("empleado")
for empleado in empleados:
    sid = empleado.getAttribute("id")
    username = empleado.getElementsByTagName("username")[0]
    password = empleado.getElementsByTagName("password")[0]
    print("id: %s " % sid)
    print("username: %s" % username.firstChild.data)
    print("password: %s" % password.firstChild.data)