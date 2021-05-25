lista_datos = [int(d) for d in input().split()]

salarioBase=lista_datos[0]
horasExtras=lista_datos[1]
bonificacion=lista_datos[2]

# El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 171.
horaTrabajo=salarioBase/171

# Las horas extras se liquidan con un recargo del 17% sobre el valor de una hora normal.
liqHorasExtras=horaTrabajo*0.17

# Debido a buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones de 8.8% del salario base.
liqBonificacion=0
if bonificacion==1:
    liqBonificacion=salarioBase*.088

# El salario total antes de descuentos se calcula como la suma del salario base, más el valor de las horas extras,
# más las bonificaciones (si las hay).
salarioTotal=round((salarioBase+(liqHorasExtras*horasExtras)+liqBonificacion),1)

print(salarioTotal,salarioTotal*0.89)