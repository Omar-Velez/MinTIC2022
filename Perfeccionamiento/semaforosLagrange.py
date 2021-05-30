while True:
    distancia,velocidadPermitida,tiempo = [int(valor) for valor in input().split()]
    velocidadMedia=(distancia/1000)/(tiempo/3600)
    if velocidadMedia > velocidadPermitida:
        print(f"se paso del miite {round(velocidadMedia)} > {velocidadPermitida}")
    
    

# Salida 
#########
# El programa imprimirá una línea indicando si el conductor debe ser multado o no. 
# Se debe considerar lo siguiente:
# Imprimirá OK si el conductor no superó la velocidad máxima.
# Imprimirá MULTA si se superó la velocidad máxima en menos de un 25% de la velocidad permitida.
# Imprimirá CURSO SENSIBILIZACION si la velocidad fue superada en un 25% o más de la velocidad permitida. 
# En este caso además de la multa deberá realizar un curso de sensibilización.
# Debido a que los sistemas pueden fallar y registrar valores errados (por ejemplo, indicando que el tiempo que ha tardado el  conductor es negativo). En esos casos, se deberá imprimir únicamente VALORES NEGATIVOS.
'''
9165 110 300
9165 110 299
-1000 -50 -100
12000 80 359
'''