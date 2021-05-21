## Ejercicio

#Definir la clase `saludo` con un método `saludar` que reciba un <nombre> y muestre por pantalla `hola <nombre>`.

# Definición de la clase saludo
class saludo:
    # Definición del método saludar
    def saludar(self, nombre):
        print('Hola', nombre)

nombre = input('Introduce tu nombre: ')
s = saludo()
s.saludar(nombre)