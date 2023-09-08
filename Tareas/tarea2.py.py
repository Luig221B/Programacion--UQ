import math

class Vectorparticula:
 def __init__(self, coordenada_x, coordenada_y):
    self.x = coordenada_x
    self.y = coordenada_y
    self.magnitud = math.sqrt(self.x * 2 + self.y * 2)
    self.angulo = math.atan2(self.y, self.x)

 def __str__(self):
    respuesta = "(" + str(self.x) + " , " + str(self.y) + " ) "
    return respuesta

 def __add__(self, otro):
   respuesta = Vectorparticula(self.x + otro.x, self.y + otro.x)
   return respuesta

 def __sub__(self, otro):
   respuesta = Vectorparticula(self.x - otro.x, self.y + otro.y)
   return respuesta
 
 def __mul__(self, escalar):
    respuesta = Vectorparticula(self.x * escalar, self.y * escalar)
    return respuesta
  
 def __div__(self, ):
    respuesta = Vectorparticula(self.x / 2, self.y / 2)
    return respuesta
 
gravedad = 9.8
 
print("Ingrese coordenadas del vector")
x = float(input("Componente x: "))
y = float(input("Componente y: "))

print("Ingrese un escalar")
E = float(input("Valor: ")) 

vec = Vectorparticula(x , y)
Escalar = E
print(vec)
print(E)
resultado = (vec.__mul__(E))
print("El resultado es: ", resultado)

#Se tendra en cuenta 
print("tambien puedes conocer la posición de una particula si insertas los valores de las variables usadas")

print("Coordenadas de la posición inicial ")
pos_x = float(input("Componente x: "))
pos_y = float(input("Componente y: "))
print("Vector velocidad inicial")
v0_x = float(input("Componente x: "))
v0_y = float(input("Componente y: "))
print("Tiempo")
t = float(input("valor: "))
print("Coordenadas de la aceleración ")
a_x = float(input("Componente x: "))
a_y = float(input("Componente y: "))

vec_p = Vectorparticula(pos_x,pos_y)
resultado1 = (vec_p)

vec_v = Vectorparticula(v0_x,v0_y)
Escalar1 = t 
resultado2 = (vec_v.__mul__(t))
vec_a = Vectorparticula(a_x,a_y)
Escalar2 = 0.5
resultado3 = (vec_a.__mul__(Escalar2).__mul__(Escalar1**2))


resultado = (resultado1.__add__(resultado2).__add__(resultado3))

print("La posición final es: ", resultado)




