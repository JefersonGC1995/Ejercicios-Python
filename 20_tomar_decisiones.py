#if 10 > 9:
    #print('Es correcto')
#if True:
    #print('Es correcto')    

if 2 == 5:
   print('Es correcto')    
else:
    print('No es correcto')   
    
    
mascota = 'perro'

if mascota == 'perro':
    print("Tu mascota es un perro")
elif mascota == 'gato':
    print("Tu mascota es un gato")
elif mascota == 'loro':
    print("Tu mascota es un loro")    
else:
    print("No tienes mascota")
    
    
edad = 15
calificacion = 5

if edad < 18:
    print("Eres menor de edad")
    if calificacion >= 3:
        print("Aprobaste el curso")
    else: 
        print("No aprobaste el curso")

else:
    print("Eres adulto")