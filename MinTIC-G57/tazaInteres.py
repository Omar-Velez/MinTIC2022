'''
Suponga que un individuo desea invertir
inverision=?
1 mes = 
15% / 12
'''
inversion = float(input("Digite el monto de la inversion: "))
cantidadMeses = int((input("Digite el numero de meses a evaluar el interes: ")))
interes = 0.15/12

print(f"Para su inversion de {inversion}, el interes por {cantidadMeses} mes/meses es igual a: {inversion*cantidadMeses*interes}")