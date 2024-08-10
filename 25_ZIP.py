nombres = ['Pedro','Ana','Lorena']
edades = [20, 50, 15, 40]

combinados = list(zip(nombres,edades))
print(combinados)

for nombre, edad in combinados:
    print(f"{nombre} tiene {edad}")