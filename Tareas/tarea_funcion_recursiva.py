#   def factorial (n):
#   if n == 0:
#     return 1

#   else: 

#    return n* factorial(n-1) 



# resultado = factorial(3)
# print(resultado)


# def suma_larga(lista):
#     if not lista:
#         return 0
#     else:
#         if ista[0], list):isinstance(l
#             return suma_larga(lista[0]) + suma_larga(lista[1:])
#         else:
#             return lista[0] + suma_larga(lista[1:])

# # Ejemplos de listas
# lista_1 = [1, 2]
# lista_2 = [[3, 4]]
# lista_3 = [[[5, 6]]]
# lista_4 = [[[[7, 8]]]]

# # Ejemplos de uso
# print(suma_larga(lista_1))  # Output: 3
# print(suma_larga(lista_2))  # Output: 7
# print(suma_larga(lista_3))  # Output: 11
# print(suma_larga(lista_4))  # Output: 15
# print(suma_larga(lista_1) + suma_larga(lista_2) + suma_larga(lista_3) + suma_larga(lista_4) )

# def derivadas(polinomio):
#     # Caso base: Si el polinomio está vacío, regresa una lista vacía
#     if not polinomio:
#         return []

#     # Calcula la derivada del primer término (b, n)
#     b, n = polinomio[0]
#     derivada_b = b * n
#     derivada_n = n - 1

#     # Si la derivada del término no es cero, agrega el término a la derivada
#     if derivada_b != 0:
#         derivada = (derivada_b, derivada_n)
#         derivada_resultante = [derivada]
#     else:
#         derivada_resultante = []

#     # Llama recursivamente a derivadas para el resto del polinomio
#     derivada_resultante.extend(derivadas(polinomio[1:]))

#     return derivada_resultante

# # Función para ingresar el polinomio desde el usuario
# def ingresar_polinomio():
#     entrada = input("Introduce el polinomio de la forma [(b,n)] (o 'fin' para terminar): ")
#     polinomio = []

#     while entrada.lower() != 'fin':
#         try:
#             b, n = eval(entrada)  # Convierte la entrada en una tupla (b, n)
#             polinomio.append((b, n))
#         except:
#             print("Formato incorrecto. Introduce el polinomio de la forma [(b,n)]")
#         entrada = input("Introduce el siguiente término (o 'fin' para terminar): ")

#     return polinomio

# # Ejemplo de uso
# polinomio = ingresar_polinomio()
# derivada = derivadas(polinomio)
# print("Polinomio original:", polinomio)
# print("Derivada:", derivada)

# def sucesion_fibo(n):
#     if n ==0 or n==1:
#      return n
#     else : 
#        return sucesion_fibo(n-1) + sucesion_fibo(n-2)
    
# n = int(input("numero hasta el cual se desea calcular la suseción: "))

# for i in range(n):
#    resultado = sucesion_fibo(i)
#    print(resultado, end=" ")  
   

