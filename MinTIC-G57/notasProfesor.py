# Declaracion del diccionario
'''
Dentro del diccionario se puede decir que hay "objetos" del tipo se define dentro del diccionario
'''
notas={
    "talleres":[0,0,0], # se declara una lista de 3 espacios
    "evaluaciones":[0,0], # se declara una lista de 2 espacios
    "trabajoFinal":0.0, # se declara como valor 0 sin especificar int / float
    "sustentacionFinal":0.0 # se declara como valor 0 sin especificar int / float
    }

# Funcion para validar las notas ingresadas
def validadorNota(nota): # funcion que recibe un numero "nota" cuando es llamado
    if nota.isdigit(): # valida si solo tiene numeros el numero ingresado
        nota=float(nota) # convierte a flotante el numero ingresado
        if nota >= 0 and nota <= 5: # valida si esta en el rango entre 0 y 5
            return [nota] # retorna el valor de la nota como un numero flotante entre 0 y 5
        else:
            print("\nel numero no esta en el rango de 0 y 5\n") # si no esta en el rango entre 1 y 9 envia advertencia
            return False # retorna falso para que vuelva a pedir que ingrese la nota
    else:
        print("Digitaste un caracter!!") # indica si ingresaste un caracter o espacio en la nota ingresada

# funcion para ingresar la nota validada
'''
esta funcion recibe un "objeto" que puede ser una lista, una variable, otro diccionario, etc
'''
def ingresoNota(tipoNota, cantidad): # recibe un objeto tipo Lista/variable y la cantidad de notas que pedira por ese objeto
    ingreso=0 # esta no puede superar la "cantidad" de preguntas 
    while ingreso < cantidad: # valida que el numero de ingreso de notas en el objeto no sea superior a la cantidad de notas a pedir
        notaIngresada=input(f"Inserte la nota del taller {ingreso+1}: ") # se solicita la nota
        if validadorNota(notaIngresada): # valida y devuelve un numero flotante entre "0 y 5" o False si es mayor o un caracter
            tipoNota.append(notaIngresada) # del objeto que recibe en el index "ingreso" le asigna la nota validada 
            ingreso+=1 # aumenta el numero de ingresos que a su vez es el index del listado

#ingresoNota(notas["talleres"], 3)
#ingresoNota(notas["evaluaciones"], 2)
#ingresoNota(notas["trabajoFinal"], 1)
#ingresoNota(notas["sustentacionFinal"], 1)

# impresion de verificacion
print(type(notas["talleres"]))
print(type(notas["evaluaciones"]))
print(type(notas["trabajoFinal"]))
print(type(notas["sustentacionFinal"]))
