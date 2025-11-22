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
    print("Esta función representa una *recta*. Tiene dos valores importantes:")
    print("- a : la pendiente (indica cuánto sube o baja la recta)")
    print("- b : el intercepto en el eje Y (donde la recta corta el eje vertical)")
    print()

    a = float(input("Ingresa el valor de a (pendiente): "))
    b = float(input("Ingresa el valor de b (intercepto en Y): "))
    x = float(input("Ingresa el valor de x: "))

    print("\nPASO 1: Escribir la fórmula general")
    print("f(x) = a·x + b")

    print("\nPASO 2: Sustituir los valores entregados")
    print(f"f({x}) = {a} · {x} + {b}")

    # Cálculo parcial
    ax = a * x
    print(f"\nPASO 3: Multiplicar a por x")
    print(f"{a} · {x} = {ax}")

    print("\nPASO 4: Sumar ese resultado con b")
    resultado = ax + b
    print(f"{ax} + {b} = {resultado}")

    print(f"\nRESULTADO FINAL: f({x}) = {resultado}\n")
    print("Cierre el plano cartesiano para continuar...")
    x = np.linspace(-10, 10, 400)

    y = a * x + b

    plt.plot(x, y, '-r', label=f'y = {a}x + {b}')

    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)

    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title("Recta con ejes X e Y")
    plt.legend()

    plt.grid(True)
    plt.show()
    



def func2():
    print("\nFUNCIÓN DE GRADO 2 (f(x) = ax² + bx + c)")
    print("Esta función representa una *parábola*. Cada valor significa:")
    print("- a : abre hacia arriba si es positivo o hacia abajo si es negativo")
    print("- b : afecta la inclinación inicial")
    print("- c : es el valor donde la gráfica corta el eje Y")
    print()

    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))
    c = float(input("Ingresa el valor de c: "))
    x = float(input("Ingresa el valor de x: "))

    print("\nPASO 1: Escribir la fórmula general")
    print("f(x) = a·x² + b·x + c")

    print("\nPASO 2: Sustituir valores")
    print(f"f({x}) = {a}·({x}²) + {b}·({x}) + {c}")

    # Cálculos parciales
    x2 = x ** 2
    ax2 = a * x2
    bx = b * x

    print("\nPASO 3: Calcular x²")
    print(f"{x}² = {x2}")

    print("\nPASO 4: Multiplicar a por x²")
    print(f"{a} · {x2} = {ax2}")

    print("\nPASO 5: Multiplicar b por x")
    print(f"{b} · {x} = {bx}")

    print("\nPASO 6: Sumar todos los valores")
    resultado = ax2 + bx + c
    print(f"{ax2} + {bx} + {c} = {resultado}")

    print(f"\nRESULTADO FINAL: f({x}) = {resultado}\n")



def func3():
    print("\nFUNCIÓN DE GRADO 3 (f(x) = ax³ + bx² + cx + d)")
    print("Esta función representa una *curva cúbica*. Cada valor influye en:")
    print("- a : forma general de la curva (subida y bajada)")
    print("- b : curvatura secundaria")
    print("- c : inclinación local")
    print("- d : corte con el eje Y")
    print()

    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))
    c = float(input("Ingresa el valor de c: "))
    d = float(input("Ingresa el valor de d: "))
    x = float(input("Ingresa el valor de x: "))

    print("\nPASO 1: Escribir la fórmula general")
    print("f(x) = a·x³ + b·x² + c·x + d")

    print("\nPASO 2: Sustituir valores")
    print(f"f({x}) = {a}·({x}³) + {b}·({x}²) + {c}·({x}) + {d}")

    # Cálculos parciales
    x3 = x ** 3
    x2 = x ** 2
    ax3 = a * x3
    bx2 = b * x2
    cx = c * x

    print("\nPASO 3: Calcular x³ y x²")
    print(f"{x}³ = {x3}")
    print(f"{x}² = {x2}")

    print("\nPASO 4: Multiplicar a por x³")
    print(f"{a} · {x3} = {ax3}")

    print("\nPASO 5: Multiplicar b por x²")
    print(f"{b} · {x2} = {bx2}")

    print("\nPASO 6: Multiplicar c por x")
    print(f"{c} · {x} = {cx}")

    print("\nPASO 7: Sumar todos los valores")
    resultado = ax3 + bx2 + cx + d
    print(f"{ax3} + {bx2} + {cx} + {d} = {resultado}")

    print(f"\nRESULTADO FINAL: f({x}) = {resultado}\n")




if opcion == 1:
    procesamiento = func1()
elif opcion == 2:
    procesamiento = func2()
elif opcion == 3:
    procesamiento = func3()
elif opcion == 4:
    procesamiento = menu_explicacion()
    os.system("cls")
    if procesamiento == 1:
        explicacion_grado1()
        pregunta = int(input("Quieres ver la explicacion detallada de la funcion grado 2 o 3: "))
        if pregunta == 2:
            os.system("cls")
            explicacion_grado2()
            print()
            #menu_explicacion()
        elif pregunta == 3:
            os.system("cls")
            explicacion_grado3()
            print()
            #menu_explicacion()
    elif procesamiento == 2:
        explicacion_grado2()
        pregunta = int(input("Quieres ver la explicacion detallada de la funcion grado 1 o 3:"))
        if pregunta == 1:
            os.system("cls")
            explicacion_grado1()
            print()
            #menu_explicacion()
        elif pregunta == 3:
            os.system("cls")
            explicacion_grado3()
            print()
            #menu_explicacion()
    elif procesamiento == 3:
        explicacion_grado3()
        pregunta = int(input("Quieres ver la explicacion detallada de la funcion grado 1 o 2:"))
        if pregunta == 1:
            os.system("cls")
            explicacion_grado1()
            print()
            #menu_explicacion()
        elif pregunta == 2:
            os.system("cls")
            explicacion_grado2()
            print()
            #menu_explicacion()
    else:
        print("Ocurrio un Error")
else:
    print("opcion invalida")