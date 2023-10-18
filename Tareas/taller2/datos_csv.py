import csv


nombres = []
edades = []
calificaciones = []

with open('datos.csv') as per:
    reader = csv.reader(per)
    
    for fila in reader:
        if len(fila) >= 3:  
            nombre = fila[0]  
            edad = int(fila[1])   
            calificacion = float(fila[2]) 
            
          
            nombres.append(nombre)
            edades.append(edad)
            calificaciones.append(calificacion)
            
            
            print(f"Nombre: {nombre} ,Edad: {edad} ,Calificación: {calificacion}")




promedio_de_edad = sum(edades)/ len(edades)
print(f"Este el promedio de edad: {promedio_de_edad}")

promedio_de_calificacion = sum(calificaciones)/ len(calificaciones)
print(f"Este el promedio de notas: {promedio_de_calificacion}")

print("Estudiantes que perdieron la materia: ")

for i in range(len(calificaciones)):
    if calificaciones[i] < 3:
        print(f"Nombre : {nombres[i]} Calificacion : {calificaciones[i]}")



calificaiones_ordenadas = sorted(calificaciones, reverse=True)
total_elementos = len(calificaiones_ordenadas)
mejor_10 = int(0.10* total_elementos)

print("Las mejores calificaciones (10% superior) son:")
for i in range(len(calificaiones_ordenadas)):
    if calificaciones[i] >= calificaiones_ordenadas[mejor_10]:
        print(f"Nombre: {nombres[i]}, Calificación: {calificaciones[i]}")


