distancia,velocidadPermitida,tiempo = [int(valor) for valor in input().split()]
velocidadMedia=(distancia/1000)/(tiempo/3600)
if distancia >= 0 and velocidadPermitida >= 0 and tiempo >= 0:
    if velocidadMedia <= velocidadPermitida:
        print("OK")
    elif velocidadMedia > velocidadPermitida and velocidadMedia <= velocidadPermitida*1.25:
        print("MULTA")
    elif velocidadMedia > velocidadPermitida*1.25:
        print("CURSO SENSIBILIZACION")
else:     
    print("VALORES NEGATIVOS")