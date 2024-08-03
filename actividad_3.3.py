texto = input("Ingrese un texto: ")
texto_min = texto.lower()

letra1 = input("Ingrese letra uno:").lower()
letra2 = input("Ingrese letra dos:").lower()
letra3 = input("Ingrese letra tres:").lower()

print ("Las letras que ingresaste son:",letra1,letra2,letra3) 
mi_lista = ["letra1","letra2","letra3"]

conteo_letra1 = texto_min .count(letra1)
conteo_letra2 = texto_min .count(letra2)
conteo_letra3 =texto_min .count(letra3)

print(f"La letra '{letra1}' aparece {conteo_letra1} veces.")
print(f"La letra '{letra2}' aparece {conteo_letra2} veces.")
print(f"La letra '{letra3}' aparece {conteo_letra3} veces.")

palabras = texto_min .split()
numero_de_palabras = len(palabras)
print(f"El número de palabras escritas en el texto: {numero_de_palabras}")

primera_letra = texto_min [0]
ultima_letra = texto_min [-1]

print(f"La primera letra: {primera_letra}")
print(f"La última letra: {ultima_letra}")

fragmento = texto_min  [::-1]
print(f"texto invertido: {fragmento}")
#texto= input("Escribe tu texto:")

buscar_python = "python" in texto
dic= {True: "SI", False: "NO"}
print(dic[buscar_python])
