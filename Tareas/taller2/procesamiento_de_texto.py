class ProcesadorDeTexto:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.parrafos = self.leer_archivo()

    def leer_archivo(self):
        try:
            with open(self.ruta_archivo, 'r') as file:
                texto = file.read()
                parrafos = texto.split('\n\n')  # Suponemos que los párrafos están separados por líneas en blanco
                return parrafos
        except FileNotFoundError:
            print(f"El archivo '{self.ruta_archivo}' no se encontró.")

    def lista_de_tuplas_parrafos_longitud(self):
        tuplas = [(parrafo, len(parrafo)) for parrafo in self.parrafos]
        return tuplas

    def parrafos_mas_largos(self, n):
        tuplas = self.lista_de_tuplas_parrafos_longitud()
        tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1], reverse=True)
        return tuplas_ordenadas[:n]


ruta_archivo = 'texto.txt'  # Reemplaza con la ruta de tu archivo de texto

procesador = ProcesadorDeTexto(ruta_archivo)


lista_tuplas = procesador.lista_de_tuplas_parrafos_longitud()

for parrafo, longitud in lista_tuplas:
    print(f'Longitud: {longitud} - Párrafo: {parrafo}\n')

# Obtener los 3 párrafos más largos (ejemplo con N=3)
n_mas_largos = procesador.parrafos_mas_largos(3)

for i, (parrafo, longitud) in enumerate(n_mas_largos, 1):
    print(f'Párrafo {i}:')
    print(parrafo)
    print(f'Longitud: {longitud}\n')
