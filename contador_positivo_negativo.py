'''
Leer números enteros de teclado, hasta que el usuario ingrese el 0.
Mostrar al final, el conteo de los números positivos ingresados y el conteo
de los negativos. con Break

'''
positivos, negativos = 0,0

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    
    if numero == 0:
        break  
    if numero > 0: positivos += 1
    elif numero < 0: negativos += 1

print(f"Cantidad de números positivos ingresados: {positivos}")
print(f"Cantidad de números negativos ingresados: {negativos}")