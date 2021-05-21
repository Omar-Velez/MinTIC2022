
# Una expresión regular, es una secuencia de caracteres que forma un patrón de búsqueda y se
# puede usar para verificar si una cadena contiene este patrón.

# Python tiene un paquete incorporado llamado re, que se puede usar para trabajar con expresiones
# regulares. Puedes comenzar a usar expresiones regulares usando el módulo re.
'''
+-------------------------------------------------------------------------------------------------+
| Función	   |        Descripción                                                               |
+-------------------------------------------------------------------------------------------------+
| findall	   | Devuelve una lista que contiene todas las coincidencias                          |
| search	   | Devuelve un objeto Match si hay una coincidencia en cualquier parte de la cadena |
| split	       | Devuelve una lista donde la cadena se ha dividido en cada coincidencia           |
| sub	       | Reemplaza una o varias coincidencias con una cadena                              |
| match	       | Determina si la expresión coincide al principio de la cadena                     |
+-------------------------------------------------------------------------------------------------+
'''
# Metacaracteres
# Existen metacaracteres, que no son otra cosa que caracteres con significado especial.

'''
+-----------------------------------------------------------------------------------------------------+
| Caracrter	  | Descripción	                                                               | Ejemplo  |
+-----------------------------------------------------------------------------------------------------+
| []	      | Representa un conjunto de caracteres	                                   |  [a-c]   |
| \		      | Señala una secuencia especial (también puede usarse para escapar de        |   \n     |
|             | caracteres especiales)	                                                   |          |
| .		      | Cualquier carácter (excepto el carácter de salto de línea)	               |  ho..a   |
| ^		      | Comienza con	                                                           |  ^hola   |
| $		      | Termina con	                                                               |   fin$   |
| *		      | Cero o más ocurrencias	                                                   |   cad*   |
| +	          |	Una o más ocurrencias	                                                   |   cad+   |
| {}	      |	Exactamente el número especificado de ocurrencias	                       |  cad{3}  |
| |		      | Cualquiera o	                                                           | uno|otro |
| () 	      |	Captura y grupo	                                                           |          |
+-----------------------------------------------------------------------------------------------------+
'''

# Caracteres Especiales
# Una secuencia especial se especifica con el caracter \ seguido por uno de los caracteres en
# la lista a continuación:

'''
+-----------------------------------------------------------------------------------------------------------------------------+
| Caracter | Descripción                                                                                      |    Ejemplo    |
+-----------------------------------------------------------------------------------------------------------------------------+
| \A	   | Devuelve una coincidencia si los caracteres especificados están al principio de la cadena	      | \AInicio      |
| \b	   | Devuelve una coincidencia donde los caracteres especificados están al principio 	              | r»\bpalabr»   |
|          | o al final de una palabra                                                                        | r»labra\b»    |
| \B	   | Devuelve una coincidencia donde están presentes los caracteres especificados, pero NO al  	      | r»\Bain»      |
|          | principio (o al final) de una palabra                                                            | r»ain\B»      |
| \d	   | Devuelve una coincidencia donde la cadena contiene dígitos (números del 0 al 9)                  |	\d            |
| \D	   | Devuelve una coincidencia donde la cadena NO contiene dígitos	                                  | \D            |
| \s	   | Devuelve una coincidencia donde la cadena contiene un carácter de espacio en blanco              |	\s            |
| \S	   | Devuelve una coincidencia donde la cadena NO contiene un carácter de espacio en blanco	          | \S            |
| \w	   | Devuelve una coincidencia donde la cadena contiene cualquier carácter de palabra                 | \w            |
|          | (caracteres de la A a la Z, dígitos del 0-9 y el carácter de subrayado _)	                      |               |
| \W	   | Devuelve una coincidencia donde la cadena NO contiene ningún carácter de palabra       	      | \W            |
| \Z	   | Devuelve una coincidencia si los caracteres especificados están al final de la cadena	          | Cadena\Z      |
+-----------------------------------------------------------------------------------------------------------------------------+
'''

# Conjuntos
# Un conjunto es un conjunto de caracteres dentro de un par de corchetes [] con un significado especial

'''
+-----------------------------------------------------------------------------------------------------------------------------+
| Conjunto   | Descripción                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------+
|   [asd]    | Devuelve una coincidencia donde está presente uno de los caracteres especificados (a, s, o d)                  |
|   [a-d]    | Devuelve una coincidencia para cualquier carácter en minúscula, alfabéticamente entre a y d                    |
|   [^asd]   | Devuelve una coincidencia para cualquier carácter excepto los caracteres a, s y d                              |
|   [0123]   | Devuelve una coincidencia donde cualquiera de los dígitos especificados (0, 1, 2 o 3) están presentes          |
|   [0-9]    | Devuelve una coincidencia para cualquier dígito entre 0 y 9                                                    |
| [0-5][0-9] | Devuelve una coincidencia para cualquier número de dos dígitos de 00 y 59                                      |
| [a-zA-Z]	 | Devuelve una coincidencia para cualquier carácter alfabéticamente entre a y z, minúsculas o mayúsculas         |
|    [+]	 | En los conjuntos, +, *,., |, (), $, {} no tiene un significado especial, por lo que [+] significa:             |
|            | devolver una coincidencia para cualquier carácter + en la cadena                                               |
+-----------------------------------------------------------------------------------------------------------------------------+
'''
# Tomando en cuenta los conjutos de caracteres anteriormente descritos es posible formar expresiones regulares. 
# Comencemos por ver como funcionan las distintas opciones que tiene python para evaluar expresiones.