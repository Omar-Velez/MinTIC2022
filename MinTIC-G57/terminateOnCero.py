contador=0
while True:
    numero=input("Digite un numero diferente de 0: ")
    if numero.isdigit():
        numero=int(numero)
        if numero!=0:
            contador+=numero
            print(f"\nNumero !! {numero} ¡¡ es valido..... total suma {contador}\n")
        else:
            print(f"\nNumero >> {numero} << prohibido!!! Error!!! Aiuda!!! \n")
            break
    else:
        print("ingresaste caracteres :(")
