def sucesion_fibo(n):
    if n ==0 or n==1:
     return n
    else : 
       return sucesion_fibo(n-1) + sucesion_fibo(n-2)
    
n = int(input("numero hasta el cual se desea calcular la suseción: "))

for i in range(n):
    resultado = sucesion_fibo(i)
    print(resultado, end=" ")  

print("\n Pares hasta donde escogites la sucesion: ")  
for i in range(n): 
     resultado = sucesion_fibo(i)
     if resultado % 2 == 0:
      print(resultado , end= " ")