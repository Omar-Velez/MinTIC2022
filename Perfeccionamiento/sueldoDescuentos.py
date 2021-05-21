salarioBase=2355255
horasExtras=2 
bonificacion=True

"1000000 0 0"
"2355255 2 1"

"1000000.0 890000.0"
"2594747.2 2309325.0"

horaTrabajo=salarioBase/171
liqHorasExtras=(horaTrabajo*horasExtras)*.17
liqBonificacion=0
if bonificacion:
    liqBonificacion=salarioBase*1.088

salarioTotalsindescuentos=(salarioBase+liqHorasExtras+liqBonificacion)*.89
print(salarioTotalsindescuentos)

'''El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 171.
Las horas extras se liquidan con un recargo del 17% sobre el valor de una hora normal.
Debido a buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones de 8.8% del salario base.
El salario total antes de descuentos se calcula como la suma del salario base, más el valor de las horas extras, más las bonificaciones (si las hay).
Se descontará 5% del salario total antes de descuentos para el plan obligatorio de salud.
Se descontará 5% del salario total antes de descuentos para el aporte a pensión.
Se descontará 1% del salario total antes de descuentos para caja de compensación.'''