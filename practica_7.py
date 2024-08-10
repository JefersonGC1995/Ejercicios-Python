alumnos_clase = ["Maria", "Jose", "Carlos", "Martina", "Isabel","Tomas","Daniela"]

for alumnos in alumnos_clase:
    
  print("Hola, " + alumnos )

lista_numeros = [1,5,8,7,6,8]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros += numero
    
print(suma_numeros)
    
lista_numeros = [1,5,8,7,6,8]
suma_pares = 0
suma_impares= 0

for numero in lista_numeros:
    if numero % 2 == 0:
       suma_pares += numero
else:
    suma_impares += numero
    
print(f"suma de numeros pares: {suma_pares}")
print(f"suma de numeros impares:{suma_impares}")
    
  