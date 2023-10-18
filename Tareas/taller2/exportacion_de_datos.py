import json

def agregar_empleado(lista_empleados, nombre, salario, departamento):
    empleado = {"nombre": nombre, "salario": salario, "departamento": departamento}
    lista_empleados.append(empleado)

empleados = []

agregar_empleado(empleados, "Frank", 7000, "Ambiental")
agregar_empleado(empleados, "Hernan", 5500, "Produccion")
agregar_empleado(empleados, "Baldor", 5500, "Analisis")

# Exportar la lista de empleados a JSON
with open("empleados.json", "w") as json_file:
    json.dump(empleados, json_file)

# Imprimir los datos como lo hacías antes
for empleado in empleados:
    print("nombre: ", empleado["nombre"])
    print("salario: ", empleado["salario"])
    print("departamento: ", empleado["departamento"])
    print()
