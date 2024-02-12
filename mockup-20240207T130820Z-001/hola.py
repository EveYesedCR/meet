 
    
#Ejercicio numero 2

#entradas
hemoglobina = int(input('Dijite su nivel de hemoglobina en sangre '))
sexo = int(input('Dijite (1. Hombre / 2. Mujer) '))


#pedir edad en caso de que sean meses 
condiedad = int(input('Si su edad es menor a un año precione (1 / 0) en caso contrario '))

if condiedad == 1 :    
    
    edadmeses = int(input('Dijite su edad en meses '))
    
    if edadmeses <=1 and hemoglobina>=13 and hemoglobina<=26:
        
        print('Su resultado de hemoglobina es negativo')
    
    else : 
        print ('Su resultado de hemoglobina es positivo')
        
    
elif condiedad == 0 :
    
    edad = int(input('Dijite su edad'))
    
else : 
    
    print('Dijite correctamente el numero e intente de nuevo')







