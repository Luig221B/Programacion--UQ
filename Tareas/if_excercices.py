#ejercicios 7, 4, 11

# credits = int(input("¿cuantos creditos has tomado': "))
# if credits <=100:
#     print("fiera") 
# elif credits <=84:
#     print("el estudiante esta maquina")
# elif credits <=53:
#          print("El estudiante es junior")
# elif credits <=24:
#             print("cambiese de carrera")

#numero 11

# hora_inical = int(input("Ingresa una hora: "))
# tipo_de_hora = int(input(" am(1) or pm (2)?"))   #terminar 
# if tipo_de_hora == 1:
#     return 1

# nueva_hora = int(input("¿cuantas horas quieres sumar"))      #buscar ejercicio

# elif: tipo_de_hora ==2:


# print(hora_inical + nueva_hora + tipo_de_hora) 



#Programa que pregunta al usuario, que ingrese un valor de temperatura y la escala, y el programa imprimira la temperatura en C y F

print(" PROGRAMA PARA HACER CONVERSION DE ESCALA DE TEMPERATURA \n")
programa_temperatura = int(input("Ingresa un valor de temperatura: "))
print("¿En qué escala de temperatura quieres tenerlo: ")
escala = int(input(" Celcius(1) o Farenheit(2): "))

if escala == 1:
    print("Tu temperatura escogida es: ", programa_temperatura, "Celsius" )

elif escala ==2:
    print("tu temperatura escogida es: ", programa_temperatura , "Farenheit")


conversion_CF = 9/5*programa_temperatura +32

conversion_FC = 5/9*(programa_temperatura - 32)


if escala ==1:
    print(" y en la otra escala es: ", conversion_CF, "Farenheit")

elif escala ==2:                                                                               #se puede usar else o elif, en este caso
    print(" y en la otra escala es: ", conversion_FC, "Celsius")




