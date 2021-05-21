# -*- encoding: utf-8 -*-
'''
Ejemplo que permite crear un archivo PDF  desde Python con la libreria reporlab.
********************************************************************************
'''
# Importando librerias 
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

##############################################################################################
# para la ejecucion de este script se necesita descargar la libreria de reportlab            #
# https://www.reportlab.com/dev/install/version_3_and_up/ se debe tener instalado pip para   #
# poder proceder con la descarga de esta libreria.                                           #
##############################################################################################

documentoPDF = SimpleDocTemplate("Files/PDF_Reportlab.pdf",
                        pagesize=letter,
                        rightMargin=72,
                        leftMargin=72,
                        topMargin=72,
                        bottomMargin=18)
Story = []
logotipo = "Files/logo-mision.png"

nombreRevista = "Programación Avanzada"
numero = 4
precio = "10.00"
fechaLimite = "18/5/2021"
obsequio = "Taller de Python"

formatoFecha = time.ctime()
nombreCompleto = "Nombre Apellido"
partesDeDireccion = ["Cra. 8 ## 7 - 26", " Bogotá - Cundinamarca, Código Postal 12345"]

imagen = Image(logotipo, 1 * inch, 1 * inch)
Story.append(imagen)

estilos = getSampleStyleSheet()
estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
texto = '%s' % formatoFecha

Story.append(Paragraph(texto, estilos["Normal"]))
Story.append(Spacer(1, 12))

# Se construye la dirección
texto = '%s' % nombreCompleto
Story.append(Paragraph(texto, estilos["Normal"]))
for part in partesDeDireccion:
  texto = '%s' % part.strip()
  Story.append(Paragraph(texto, estilos["Normal"]))

Story.append(Spacer(1, 12))
texto = 'Estimado %s:' % nombreCompleto.split()[0].strip()
Story.append(Paragraph(texto, estilos["Normal"]))
Story.append(Spacer(1, 12))

texto = 'Nos gustaría darle la bienvenida como suscriptor a nuestra revista %s ! \
        Recibirá %s números con un precio introductorio de $%s. Por favor responda antes de \
        %s para comenzar a recibir su suscripción y obtenga además su obsequio: %s.' % (nombreRevista,
                                                                                        numero,
                                                                                        precio,
                                                                                        fechaLimite,
                                                                                        obsequio)
Story.append(Paragraph(texto, estilos["Justify"]))
Story.append(Spacer(1, 12))

texto = 'Gracias y esperamos haberle servido.'
Story.append(Paragraph(texto, estilos["Justify"]))
Story.append(Spacer(1, 12))
texto = 'Sinceramente,'
Story.append(Paragraph(texto, estilos["Normal"]))
Story.append(Spacer(1, 48))
texto = 'Daniel López'
Story.append(Paragraph(texto, estilos["Normal"]))
Story.append(Spacer(1, 12))
documentoPDF.build(Story)