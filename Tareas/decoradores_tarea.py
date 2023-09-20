# Los decoradores, son un tipo de función que le añade, algo (una funcionalidad) a otras funciones que se esten usando; se entiende mas facil con un ejemplo.

#facilita el acceso a un parametro que se quiera agregar en varias funciones, y evitar tener que ir en cada una colocando  ese mismo parametro 

# def funcion_decoradora(funcion_parametro):

#     def funcion_interior():

#         print(" Vamos a realizar un calculo: " )

#         funcion_parametro()


#         print("Hemos terminado el calculo")

#     return funcion_interior

      


# @funcion_decoradora

# def suma():

#     print(10+22)

# @funcion_decoradora
# def resta():

#     print(20-15)

# suma()    

# resta()



#ejemplo tomado 


# Definir una función decoradora que multiplica por 2
def multiplicar_por_dos(funcion_parametro):
    def funcion_decorada(numero):
        resultado = funcion_parametro(numero * 2)
        return resultado
    return funcion_decorada

# Aplicar el decorador a una función que suma 1
@multiplicar_por_dos
def suma_uno(numero):
    return numero + 1

# Llamar a la función decorada
resultado = suma_uno(4)
print("Resultado:", resultado)
