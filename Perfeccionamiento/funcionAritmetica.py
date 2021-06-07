def operacion(a,b,operador):
    if operador=="+":
        return a+b
    elif operador=="-":
        return a-b
    elif operador=="*":
        return a*b
    elif operador=="/":
        return a/b
    elif operador=="%":
        return a%b
    else: 
        return "No ingresaste un operador"

a=int(input("Digite el primer numero: "))
b=int(input("Digite el segundo numero: "))
operador=input("Digite un operador ( + - * / % ): ")
print(operacion(a,b,operador))

