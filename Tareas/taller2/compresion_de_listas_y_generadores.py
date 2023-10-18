def palabras_mas_de_cinco_letras(lista_palabras):
    for palabra in lista_palabras:
        if len(palabra) > 5:
            yield palabra


lista_de_palabras = ["manzana", "pera", "plátano", "sandía", "uva", "naranja"]

generador = palabras_mas_de_cinco_letras(lista_de_palabras)

for palabra in generador:
    print(palabra)
