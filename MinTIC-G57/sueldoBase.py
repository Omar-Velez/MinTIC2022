'''
un vendedor recibe un sueldo base
sueldoBase=1000000
comision=10% extra por comision de ventas
quiere saber cuanto dinero obtendra por concepto de comisiones por las 3 ventas en el mes 
total que recibira en el mes tomando en cuenta su sueldo base y comisiones
'''
sueldoBase = float(input("Digite el monto del salario base: "))
comisionesVentas = int((input("Digite el numero de ventas en el mes: ")))
comision = 0.10

print(f"Para su inversion de {sueldoBase}, el interes por {comisionesVentas} mes/meses es igual a: {sueldoBase*comisionesVentas*comision}")