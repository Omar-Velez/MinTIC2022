import random
baraja = ("As",2,3,4,5,6,7,8,9,10,"J","Q","K")
figura = ("Picas", "Diamante", "Corazon", "Trebol")

# enviamos una carta aleatorea
def poker(baraja,figura):
    return baraja[random.randint(0,1)],figura[random.randint(0,3)]

# llenamos la mano con 5 cartas no repetidas
cartas=[]
while len(cartas)<5:
    cartas.append(poker(baraja,figura))
    set(cartas)
    print(cartas)

# Imprimir las cartas en juego
for n in range(len(cartas)):
    print(f"{cartas[n][0]} de {cartas[n][1]}")

# cuenta la cantidad de veces que se repite una carta del mismo numero y diferente figura
repetidos=[]
for n in range(len(cartas)):
    ganador=0
    for i in range(len(cartas)):
        if cartas[n][1]!=cartas[i][1]:
            if cartas[n][0]==cartas[i][0]:
                ganador+=1
    repetidos.append(ganador)

print(repetidos)
# Indica si hay poker: 4 cartas iguales
if ganador >= 5:
    print(f"\nTienes {ganador} cartas repetidas.. Es un Poker!!! :)")
else:
    print(f"\nTienes {ganador} cartas repetidas.. Mejor suerta la proxima :(")