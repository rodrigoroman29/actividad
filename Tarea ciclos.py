"Problema numero 1"
numero = int(input("Ingrese un número: "))

suma = 0


for i in range(numero + 1):
    suma += i
print(f"La suma de 0 a {numero} es: {suma}")


"Problema numero 2"
n = int(input("Ingrese la cantidad de artículos: "))

lista = []

for i in range(n):
    articulo = input("Ingrese el artículo")
    lista.append(articulo)

lista.sort()

print("Lista de compras en orden alfabético:")
for articulo in lista:
    print(articulo)
    
"Problema numero 8"    
def sumaomult(num1, num2, num3):
    if num1 > 100 or num2 > 100 or num3 > 100:
        suma = num1 + num2 + num3
        return suma
    else:
        multiplicacion = num1 * num2 * num3
        return multiplicacion
    
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

resultado = sumaomult(num1, num2, num3)

print(f"El resultado es: {resultado}")

"Problema numero 5"

def vocales(cadena):
    
    vocales = "aeiouAEIOU"
    resultado = ""
    for caracter in cadena:
        if caracter in vocales:
            resultado += caracter
    print(resultado)
entrada = input("Ingrese una cadena de texto: ")
vocales(entrada)

"Problema numero 4"
n = int(input("Ingrese la cantidad de números: "))
numeros = []
for i in range(n):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)
numerospares = [num for num in numeros if num % 2 == 0]
print("Números pares en la lista:")
print(numerospares)

"Problema numero 6"
def n243(numero):
    return numero % 243 == 0
numero = int(input("Ingrese un número: "))
resultado = n243(numero)

if resultado:
    print(f"{numero} es divisible por 243.")
else:
    print(f"{numero} no es divisible por 243.")
    
"Probelma numero 7"
def multstring(cadena, n):
    if n <= 0:
        return ""
    else:
        return cadena * n
texto = input("Ingrese un texto: ")
n = int(input("Ingrese un número entero positivo: "))

resultado = multstring(texto, n)

print(f"El resultado es: {resultado}")
