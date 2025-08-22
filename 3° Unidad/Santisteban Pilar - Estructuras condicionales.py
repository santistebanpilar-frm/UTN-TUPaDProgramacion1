#Trabajo Practico 2 - Estructuras Condicionales - Santisteban Pilar 1 pro 2
#Ejercicio 1 Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad : int = int(input("Ingrese su edad: "))
if edad >= 18 and edad <=100:
    print("Es mayor de edad")
elif edad >= 0 and edad <18:
    print("No es mayor de edad")
else:
    print("El valor introducido es invalido")

#Ejercicio 2 Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,  mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota : float = float(input("Ingrese una nota: "))
if nota >= 6 and nota <=10:
    print("Aprobado")
elif nota>0 and nota<6:
    print("Desaprobado")
else:
    print("El valor de la nota introducida es invalida")

#Ejercicio 3 
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar
numero : int = int(input("Ingrese un numero: "))
if numero % 2==0 :
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#Ejercicio 4
#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
edad : int = int(input("Ingrese su edad: "))
if edad >= 0 and edad <12:
    print("Usted esta dentro de la categoria: Niño")
elif edad >=12 and edad <18 :
    print("Usted esta dentro de la categoria: Adolescente")
elif edad >=18 and edad < 30 :
    print("Usted esta dentro de la categoria: Adulto joven")
elif edad<=30 and edad <=100:
    print("Usted esta dentro de la categoria: Adulto")
else:
    print("El valor introducido es invalido")

#Ejercicio 5 
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
contrasena : str = str(input("Ingrese su contraseña: "))
if len(contrasena)>= 8 and  len(contrasena)<=14:
    print("Ha ingreado una conrtaseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
from statistics import mode,median, mean
import random
numeros_aleatorios : float = [random.randint(1,100) for i in range(50)]
moda :float = mode(numeros_aleatorios)
mediana :float= median(numeros_aleatorios)
media :float= mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Segun la lista de numeros hay sesgo positivo/a la derecha")
elif media<mediana and mediana < moda:
    print("Segun la lista de numeros hay sesgo negativo/a la izquierda")
elif media==mediana==moda:
    print("Segun la lista de numeros no hay sesgo")

#Ejercicio 7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla
frase : str = str(input("Ingrese una frase o palabra: "))
longitud=len(frase)
for i in range(len(frase)):
    letra = frase[i]
if  frase[longitud-1]== "a" or frase[longitud-1]== "e" or  frase[longitud-1]== "i" or  frase[longitud-1]== "o" or frase[longitud-1]== "u":
        print(frase,"!")
else:
    print(frase)

#Eercicio 8 
#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre : str = str(input("Ingrese su nombre: "))
print("Eliga una opcion de la siguiente lista:")
print("1) Si quiere su nombre en mayúsculas.")
print("2) Si quiere su nombre en minúsculas.")
print("3) Si quiere su nombre con la primera letra mayúscula.")
opcion : int = int(input("Seleccione una opcion del 1 al 3 para converitr su nombre: "))
if opcion==1:
    print(nombre.upper())
elif opcion==2:
    print(nombre.lower())
elif opcion==3:
    print(nombre.title())
else:
    print("No ha ingresado una opción disponible")

#Ejercicio 9 
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud : float = float(input("Ingrese la magnitud de un terremoto: "))
if magnitud > 0 and magnitud < 3 :
    print("Muy leve (imperceptible)")
elif magnitud >=3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud>=4 and magnitud < 5 :
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud>= 5 and magnitud < 6 :
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7 :
    print("Muy fuerte (puede causar daños significativos)")
elif magnitud>=7 and magnitud <= 10:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("El valor ingresado no es valido")

#Ejercicio 10
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano
hemisferio : str = str(input("Ingrese si se encuentra en el hemisferio norte (N) o  el sur (S): "))
if hemisferio.upper()== "N" or hemisferio.upper() == "S":
    mes : int = int(input("En que mes se encuntra actualmente? Ingrese el mes en formato de numero del 1 al 12: "))
    if mes>=1 and mes<=12:
        dia : int = int(input("Ingrese el dia de hoy en formato numero del 1 al 31: "))
        if dia>=1 and dia<=31:
            if hemisferio.upper()== "N":
                if mes == 12 and dia <=21 or mes <=3 and dia<=20:
                    print("Invierno") 
                elif mes == 3 and dia <=21 or mes <=6 and dia<=20:
                    print("Primavera")
                elif mes == 6 and dia <=21 or mes <=9 and dia<=20:
                    print("Verano")
                elif mes == 9 and dia <=21 or mes <=12 and dia<=20:
                    print("Otoño")
            elif hemisferio.upper() == "S":
                if mes ==12 and dia <=21 or mes <=3 and dia<=20:
                    print("Verano")
                elif  mes == 3 and dia <=21 or mes <=6 and dia<=20:
                    print("Otoño")
                elif mes == 6 and dia <=21 or mes <=9 and dia<=20:
                    print("Invierno") 
                elif  mes == 9 and dia <=21 or mes <=12 and dia<=20:
                    print("Primavera")
                else:
                    print("NO ha ingresado una respuesta correscta")
        else:
            print("NO ha ingresado una respuesta correscta")
    else:
        print("NO ha ingresado una respuesta correscta")
else:
    print("NO ha ingresado una respuesta correscta")
