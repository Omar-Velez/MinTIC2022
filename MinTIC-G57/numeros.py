
while True:
    numero=input("Digite un numero: ")
    if numero.isdigit():
        numero=int(numero)
        if numero%2==0:
            print(f"Numero {numero} es par")
        else:
            print(f"Numero {numero} es impar")
    else:
        print("ingresaste caracteres :(")
        break