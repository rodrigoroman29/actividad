"Problema de año bisiesto"
Año = int(input("Escriba un año"))

if Año%4==0:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
    
    
"Porblema de indentificacion de numeros"
num = int(input("Ingrese un numero"))

if num > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")
if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es inpar")
if num > 100:
    print("El numero es mayor a 100")
else:
    print("El numero es menor a 100")

"Problema de arreglar los numero"
Numeros = [12, 456, 2, 123]
Numeros_bien = sorted(Numeros)
print(Numeros_bien)

"Problema de nombres"
nombres = ("Jose Miguel", "Carlos", "Manuel", "Memo")
NombreCorrecto = input("Escriba un nombres de los que aparecen")

if NombreCorrecto in nombres:
    print("True")
else:
    print("false")
    
"Problema de cuadrado o rectangulo"
Lado = float(input("Esrciba un numero decimal"))
Diagonal = float(input("Esrciba un numero decimal"))

if Lado > 0 and Diagonal > 0:
    if Lado == Diagonal:
        print("Es un cuadrado")
    else:
        print("Es un rectangulo")

