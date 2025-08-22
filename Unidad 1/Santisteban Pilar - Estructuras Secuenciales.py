#Trabajo Practico 1 : Secuenciales  -  Santisteban Pilar - 1 prog 2 
from math import pi
print(pi)
#Ejercicio 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")
#Ejercicio 2 : Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
nombre =  input("Ingrese su nombre: ")
print(f"Hola {nombre}!")
#Ejercicio 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad=  int(input("Ingrese su edad: "))
residencia =  input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} y  vivo en {residencia}")
#Ejercicio 4 : Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio : float = float(input("Ingrese el radio de un circulo: "))
PI : float = 3.14
area : float = PI * (radio**2)
perimetro : float =  2 * PI * radio
print(f"Segun el radio de su circulo su area vale {area} y su perimetro {perimetro}")
#Ejercicio 5 Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos : float = float(input("Ingrese una cantidad de segundo para pasar a horas: "))
horas: float= segundos / 3600 
print(f"{segundos} segundos equivalen a {horas} horas")
#Ejercicio 6 Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Ingrese un numero: "))
contador : int = 1
while contador <  11:
        print(f"{numero} x {contador} = {numero*contador}")
        contador = contador + 1
#Ejercicio 7 Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
numero1 = int(input("Ingrese un numero que no sea 0: "))
numero2 = int(input("Ingrese otro numero distinto al 0: "))
suma = numero1 + numero2
print(f"La suma de entre {numero1}  y {numero2} es igual a {suma}")
resta = numero1 - numero2
print(f"La resta de entre {numero1}  y {numero2} es igual a {resta}")
multiplicacion = numero1 * numero2
print(f"La multiplicacion de entre {numero1}  y {numero2} es igual a {multiplicacion}")
division = numero1 / numero2
print(f"La division de entre {numero1}  y {numero2} es igual a {division}")
#Ejercicio 8 Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 /(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc =  peso / (altura)**2
print(f"Su IMC es de {imc}")
#Ejercicio 9 Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
celsius = float(input("Ingrese la temperatura en grados celsius: "))
farenheit = 9/5 *  celsius + 32
print(f"{celsius}° Celsius equivale a {farenheit}° Farenheit ")
#Ejercicio 10 Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 =int(input("Ingrese un numero más: "))
promedio:float = (numero1+numero2+numero3)/3
print(f"El promedio de los tres numeros ingresados es de {promedio}")
