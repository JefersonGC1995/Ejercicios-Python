diccionario ={'c1':'valor1','c2': 'valor2'}

print(type(diccionario))

resultado = diccionario['c2']

print(resultado)

dic = {'c1':55, 'c2':[10,20,30],'c3':{"s1":100,"s2":200}}
resultado = dic['c2'][1]
print(resultado)

resultado = dic['c3']['s2']

dic2 = {'c1':['a','b','c'],'c2':['e','f','g']}
resultado = dic2['c2'][1].upper()
print(resultado)

dic3 = {1:'a', 2: 'b'}
dic3[2]='c'
print(dic3)

dic3[3]='x'
print(dic3)

print(dic3.keys())
print(dic3.values())
print(dic3.items())