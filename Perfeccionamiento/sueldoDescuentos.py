lista_datos = [float(valor) for valor in input().split()]

salarioBase=lista_datos[0]
horasExtras=lista_datos[1]
bonificacion=lista_datos[2]

# El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 171.
horaTrabajo=salarioBase/171

# Las horas extras se liquidan con un recargo del 17% sobre el valor de una hora normal.
liqHorasExtras=(horasExtras*horaTrabajo)*1.17

# Debido a buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones de 8.8% del salario base.
liqBonificacion=0
if bonificacion==1:
    liqBonificacion=salarioBase*0.088

# El salario total antes de descuentos se calcula como la suma del salario base, más el valor de las horas extras,
# más las bonificaciones (si las hay).
salarioTotal=salarioBase+liqBonificacion+liqHorasExtras
salarioDescuento=salarioTotal*0.89
print(round(salarioTotal,1),round(salarioDescuento,1))