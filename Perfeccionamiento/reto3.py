iteraciones=int(input())
cafe=[]

while iteraciones>0:
    cafe.append([int(valor) for valor in input().split()])
    iteraciones-=1

precios=0
for n in range(0,len(cafe)):
    if cafe[n][0] >=10 and cafe[n][0] <=12:
        if cafe[n][1] <=18:
            if cafe[n][2]>=15:
                if cafe[n][3]<=92:
                    print(cafe[n][4])
                    precios+=1

if precios <=0:
    print("NO DISPONIBLE")