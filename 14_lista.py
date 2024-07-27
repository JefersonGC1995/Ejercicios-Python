mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']

print(type(mi_lista))

print(len(mi_lista))
resultado = mi_lista[0:2]

print(resultado)
print(mi_lista+mi_lista2)

mi_lista[0] = 'alfa'
print(mi_lista)

mi_lista.append('z')
print(mi_lista)

mi_lista.pop()
print(mi_lista)

mi_lista.pop(0)
print(mi_lista)

lista = ['z','a','h','u']
lista.sort()
print(lista)

lista2 = [100, 50, 40, 200]
#lista2.sort()
#print(lista2)

lista2.reverse()
print(lista2)