import csv

asistencia = open('asistencia-mod.txt', 'r')
lines = asistencia.read().splitlines()
stripped = [line.replace(",", " ").split() for line in lines]
grouped = zip(*[stripped]*1)
with open('teste.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(('Zoom', 'Hora', 'Mensaje'))
    for group in grouped:
        writer.writerows(group)

print(asistencia)