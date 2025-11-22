 # llamar esta funcion en cada funcion de explicacion 
import time
import sys

def slow_print(texto, delay = 0.01):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def explicacion_grado1():
    slow_print("\n==============================")
    slow_print(" EXPLICACIÓN: FUNCIÓN DE GRADO 1")
    slow_print("==============================\n")

    slow_print("Una función de grado 1 es una fórmula de la forma:\n")
    slow_print("        f(x) = a·x + b\n")

    slow_print("¿Qué significa cada parte?")
    slow_print("f(x) o Y conocida como Variable Dependiente")
    slow_print(" - 'x' es el número que tú eliges para evaluar la función. Mas conocida como la Variable Independiente")
    slow_print("Cabe aclarar que al ser funcion grado 1 la variable x o independiente tiene exponente 1 por esta razon la funcion es de grado 1")
    slow_print(" - 'a' es la *pendiente* de la recta.")
    slow_print("     ➤ La pendiente indica qué tan inclinada está la línea.")
    slow_print("       Por ejemplo:")
    slow_print("         • Si a > 0 → la recta sube hacia la derecha.")
    slow_print("         • Si a < 0 → la recta baja hacia la derecha.")
    slow_print("         • Si a = 0 → no hay inclinación (recta horizontal).")
    slow_print(" - 'b' es la *ordenada al origen*.")
    slow_print("     ➤ Es el valor de f(x) cuando x = 0.")
    slow_print("     ➤ Es donde la recta cruza el eje Y.\n")

    slow_print("Idea clave:")
    slow_print(" Una función de grado 1 siempre dibuja una *línea recta*.")
    slow_print(" No tiene curvas, no tiene puntos máximos ni mínimos.\n")

    slow_print("Ejemplo:")
    slow_print(" Si tienes f(x) = 2x + 3:")
    slow_print("     - Subirá 2 unidades por cada 1 que avances en x.")
    slow_print("     - Cruza el eje Y en el punto (0, 3).")
    
    
    


def explicacion_grado2():
    slow_print("\n==============================")
    slow_print(" EXPLICACIÓN: FUNCIÓN DE GRADO 2")
    slow_print("==============================\n")

    slow_print("Una función de grado 2 es una fórmula de la forma:\n")
    slow_print("        f(x) = a·x² + b·x + c\n")

    slow_print("¿Qué significa cada letra?")
    slow_print(" - 'x' sigue siendo el número que eliges.")
    slow_print(" - 'a' es el término más importante.")
    slow_print("     ➤ Determina la *curvatura* de la parábola.")
    slow_print("         • Si a > 0 → la parábola abre hacia arriba.")
    slow_print("         • Si a < 0 → abre hacia abajo.")
    slow_print("     ➤ También controla qué tan 'abierta' o 'cerrada' es.")
    slow_print("         • Si |a| es grande → la parábola es angosta.")
    slow_print("         • Si |a| es pequeña → la parábola es más ancha.")
    
    slow_print(" - 'b' afecta el desplazamiento y el punto del vértice.")
    slow_print(" - 'c' es la ordenada al origen.")
    slow_print("     ➤ Es el valor de la función cuando x = 0.")
    slow_print("     ➤ Es el punto donde la parábola toca el eje Y.\n")

    slow_print("Forma de la gráfica:")
    slow_print(" Una función de grado 2 es una *parábola*.")
    slow_print(" Tiene una curva suave y un único punto importante:")
    slow_print("     ➤ *el vértice*, que puede ser un máximo o un mínimo.\n")

    slow_print("Ejemplo:")
    slow_print(" Si f(x) = x² - 4x + 3, su parábola abre hacia arriba y tiene un mínimo.")
    
    
    


def explicacion_grado3():
    slow_print("\n==============================")
    slow_print(" EXPLICACIÓN: FUNCIÓN DE GRADO 3")
    slow_print("==============================\n")

    slow_print("Una función de grado 3 tiene la forma:\n")
    slow_print("        f(x) = a·x³ + b·x² + c·x + d\n")

    slow_print("¿Qué aporta cada término?")
    slow_print(" - 'a' es el término dominante.")
    slow_print("     ➤ Controla cómo se comporta la gráfica en los extremos.")
    slow_print("         • Si a > 0 → izquierda baja, derecha sube.")
    slow_print("         • Si a < 0 → izquierda sube, derecha baja.")
    slow_print("     ➤ También influye en cuán pronunciada es la curva.\n")

    slow_print(" - 'b' y 'c' controlan la forma del tramo central.")
    slow_print("     ➤ Ajustan la cantidad de giros y la forma de la curva.")
    slow_print("     ➤ Gracias a ellos, la función puede tener:")
    slow_print("         • 0 puntos de inflexión")
    slow_print("         • 1 punto de inflexión")
    slow_print("         • hasta 2 cambios de curvatura\n")

    slow_print(" - 'd' es la ordenada al origen.")
    slow_print("     ➤ Es el valor de f(x) cuando x = 0 (punto donde toca el eje Y).\n")

    slow_print("Forma de la gráfica:")
    slow_print(" Una función de grado 3 genera curvas más complejas que pueden:")
    slow_print("     ✓ subir y luego bajar")
    slow_print("     ✓ bajar y luego subir")
    slow_print("     ✓ tener forma de 'S' suave\n")

    slow_print("Ejemplo:")
    slow_print(" f(x) = x³ - 3x tiene dos cambios de curvatura y forma de S.")
    
    
    
