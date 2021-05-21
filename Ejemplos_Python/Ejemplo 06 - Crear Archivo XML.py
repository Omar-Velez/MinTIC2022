# -*- encoding: utf-8 -*-
'''
Ejemplo que permite crear un archivo XML ubicacion especifica.
**************************************************************
'''
# Importando librerias a un objeto "ET" -> ElementTree
import xml.etree.ElementTree as ET
import codecs

##############################################################################################
# Primero se creara la estructura de un archivo xml y luego se procede a crear el archivo    #
##############################################################################################

# Creacion de la estructura del archivo XML
# Definicion del elemento root/principal
data = ET.Element('results')

# creacion del arbol de documentos xml
doc = ET.ElementTree(data)

# creando sub-elementos
dataElement = ET.SubElement(data, 'pais',
                            nombre='Colombia',
                            clima = 'Tropical',
                            capital = 'Bogota',
                            codigo='CO',
                            capacidad='Basico')
dataElement = ET.SubElement(data, 'ciudad',
                            nombre='Medellín',
                            departamento='Antioquia',
                            capacidad='Basic',
                            producto = 'Cafe')

# creaando un archivo XML con los resultados
ET.ElementTree(data).write('Files/ciudad.xml',encoding="UTF-8",xml_declaration=True)
