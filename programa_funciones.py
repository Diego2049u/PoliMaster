import matplotlib.pyplot as plt
import numpy as np
import os
from explicaciones import explicacion_grado1, explicacion_grado2, explicacion_grado3
"""
x = np.linspace(-10, 10, 400)

y = 2 * x + 3

plt.plot(x, y, '-r', label='y = 2x + 3')

plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Recta con ejes X e Y")
plt.legend()

plt.grid(True)
plt.show()
"""

def menu():
    print("1.- Funcion de grado 1: ")
    print("2.- Funcion de grado 2: ")
    print("3.- Funcion de grado 3: ")
    print("4.- Explicacion rapida de la estructura de las formulas Grado 1,2 y 3")
    print()
    op = int(input("Escoge una opcion (1,2,3,4): "))
    return op

opcion = menu()

os.system("cls")
def menu_explicacion():
    print("1.- Explicacion logica de Funciones Grado 1: ")
    print("2.- Explicacion logica de Funciones Grado 2: ")
    print("3.- Explicacion logica de Funciones Grado 3: ")
    print()
    o = int(input("Cual es la que no entiendes?: "))
    return o

#un segundo modulo puede ser entregar ejercicios random para el usuario usando la libreria random lo que seria
# "random" serian los valores numericos del ejercicio y cual seria la incognita
def func1():
    print("\nFUNCIÓN DE GRADO 1 (f(x) = ax + b)")
    print("Lo que ves aca arriba es la formula de una funcion de grado 1 en Funciones Polinomicas")
    print("Te pedire los valores uno por uno y estos remplazaran su respectiva letra para poder hacer el ejercicio")
    print()
    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))
    x = float(input("Ingresa el valor de x: "))
    print(f"f({x})= {a} {b} + {b}") #ESTA LINEA ES DE EJEMPLO PARA IMPLEMENTAR MAS TARDE
    resultado = a * x + b
    print(f"f({x}) = {resultado}\n")


def func2():
    print("\nFUNCIÓN DE GRADO 2 (f(x) = ax^2 + bx + c)")
    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))
    c = float(input("Ingresa el valor de c: "))
    x = float(input("Ingresa el valor de x: "))
    resultado = a * (x ** 2) + b * x + c
    print(f"f({x}) = {resultado}\n")


def func3():
    print("\nFUNCIÓN DE GRADO 3 (f(x) = ax^3 + bx^2 + cx + d)")
    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))
    c = float(input("Ingresa el valor de c: "))
    d = float(input("Ingresa el valor de d: "))
    x = float(input("Ingresa el valor de x: "))
    resultado = a * (x ** 3) + b * (x ** 2) + c * x + d
    print(f"f({x}) = {resultado}\n")



if opcion == 1:
    procesamiento = func1()
elif opcion == 2:
    procesamiento = func2()
elif opcion == 3:
    procesamiento = func3()
elif opcion == 4:
    procesamiento = menu_explicacion()
    if procesamiento == 1:
        explicacion_grado1()
    elif procesamiento == 2:
        explicacion_grado2()
    elif procesamiento == 3:
        explicacion_grado3()
    else:
        print("Ocurrio un Error")
else:
    print("opcion invalida")