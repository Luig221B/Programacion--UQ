import json

def productos_con_precio_superior(archivo, umbral):
    with open(archivo, 'r') as file:
        data = json.load(file)
        for producto in data:
            if producto['precio'] > umbral:
                yield producto

# Reemplaza 'productos.json' con el nombre de tu archivo JSON
archivo_json = 'productos.json'
umbral_precio = 15.0  # Reemplaza con el umbral de precio deseado

for producto in productos_con_precio_superior(archivo_json, umbral_precio):
    print(f'Nombre: {producto["nombre"]}')
    print(f'Precio: {producto["precio"]}')
    print(f'Stock: {producto["stock"]}')
    print()
