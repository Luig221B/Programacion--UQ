

def suma_acumulativa(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            numbers = line.strip().split(',')
            for num in numbers:
                try:
                    num = int(num)
                    total += num
                except ValueError:
                    print(f"El valor '{num}' no es un número válido y se omitirá.")
                    continue
                yield total

# Reemplaza 'numeros.txt' con el nombre de tu archivo de texto
archivo = 'numeros.txt'

for suma in suma_acumulativa(archivo):
    print(f'Suma acumulativa: {suma}')

