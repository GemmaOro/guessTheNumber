from random import *
intentos = 0
estimado = 0
numero_secreto = randint(1,101)
nombre = input("Cuál es tu nombre? ")
print(f"Bueno {nombre} he pensado un número del 1 al 100,\n¿Crees que puedes adivinarlo en 8 intentos? ")

while intentos < 8:
    estimado = int(input("Cuál es el número secreto? "))
    intentos = intentos + 1
    if estimado not in range(1,101):
        print("Tu número está fuera del rango permitido. ")
    elif estimado < numero_secreto:
        print("El número secreto es mayor que el que has elegido. ")
    elif estimado > numero_secreto:
        print("El número secreto es menor que el número que has elegido ")
    else:
        print(f"Felicidades adivinaste el número, te tomo {intentos} intentos! ")
        break

if estimado != numero_secreto:
    print(f"Lo siento se han acabado los intentos, el número secreto era {numero_secreto}")



