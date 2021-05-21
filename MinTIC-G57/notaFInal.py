notaFinal={
    "parcial":[],
    "examenFinal":0,
    "trabajoFinal":0
}

for notas in range(3):
    notaFinal["parcial"].append(float(input(f"Ingrese la nota {notas+1} del parcial: ")))
notaFinal["examenFinal"]=float(input(f"Ingrese la nota del examen final: "))
notaFinal["trabajoFinal"]=float(input(f"Ingrese la nota del trabajo final: "))
print("La nota final del estudiante es: ", round(((notaFinal["parcial"][0]+notaFinal["parcial"][1]+notaFinal["parcial"][2])/3)*.4+(notaFinal["examenFinal"]*.5)+(notaFinal["trabajoFinal"]*.1),2))
