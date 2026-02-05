# ================================================================
# TITULO: Calculadora de matrices usando el método de Gauss-Jordan
# AUTOR: Cesar de Jesus Becerra Vera
# FECHA: 04 de Febrero de 2026
# VERSION: 1.0
# ARCHIVO: main.py
# CENTRO UNIVERSITARIO DE LOS ALTOS / UNIVERSIDAD DE GUADALAJARA
# INGENIERIA EN COMPUTACION / 4TO SEMESTRE
# PROFESOR: JUAN MANUEL
# DESCRIPCIÓN: Este programa implementa una calculadora de matrices que utiliza el método de Gauss-Jordan en terminal.
# ================================================================

import numpy as np

def imprimir_matriz(matriz, paso=""):

    """
        Imprime la matriz de forma legible
        Argumentos:
            matriz: La matriz a imprimir
            paso: Descripción del paso actual (opcional)
    """

    if paso: # Si se proporciona una descripción del paso
        print(f"\n{paso}")
    for fila in matriz: # Imprimir cada fila de la matriz
        print("  ".join(f"{elem:8.4f}" for elem in fila))
    print()

def gauss_jordan(matriz):

    """
    Aplica el método de Gauss-Jordan a una matriz aumentada
    Retorna la matriz en su forma escalonada reducida
    Argumentos:
        matriz: La matriz aumentada a reducir
    Retorna:
        La matriz reducida
    """

    # Variables para el número de filas y columnas
    filas, columnas = matriz.shape
    matriz = matriz.astype(float)
    # Imprimir la matriz inicial
    print("\nMatriz inicial:")
    imprimir_matriz(matriz)
    
    col_actual = 0  # Columna actual que estamos procesando
    fila_pivote = 0  # Fila actual donde buscamos pivote
    
    while fila_pivote < filas and col_actual < columnas:
        # Buscar pivote en la columna actual desde la fila actual hacia abajo
        max_fila = fila_pivote + np.argmax(np.abs(matriz[fila_pivote:, col_actual]))
        # Si el pivote es cero, pasar a la siguiente columna sin avanzar fila
        if abs(matriz[max_fila, col_actual]) < 1e-10:
            print(f"Advertencia: Columna {col_actual+1} sin pivote válido, saltando...")
            col_actual += 1
            continue
        # Intercambiar filas si es necesario
        if max_fila != fila_pivote:
            matriz[[fila_pivote, max_fila]] = matriz[[max_fila, fila_pivote]]
            imprimir_matriz(matriz, f"Paso: Intercambio de filas {fila_pivote+1} y {max_fila+1}")
        # Normalizar fila del pivote
        pivote = matriz[fila_pivote, col_actual]
        matriz[fila_pivote] = matriz[fila_pivote] / pivote
        imprimir_matriz(matriz, f"Paso: Dividir fila {fila_pivote+1} por {pivote:.4f}")
        # Eliminar elementos arriba y abajo del pivote
        for j in range(filas):
            if j != fila_pivote and abs(matriz[j, col_actual]) > 1e-10:
                factor = matriz[j, col_actual]
                matriz[j] = matriz[j] - factor * matriz[fila_pivote]
                imprimir_matriz(matriz, f"Paso: F{j+1} = F{j+1} - ({factor:.4f}) * F{fila_pivote+1}")
        col_actual += 1  # Avanzar a la siguiente columna
        fila_pivote += 1  # Avanzar a la siguiente fila
    return matriz

def resolver_sistema():
    
    """
        Función principal para reducir una matriz
    """

    # Encabezado del programa
    print("="*60)
    print("CALCULADORA DE MATRICES - MÉTODO GAUSS-JORDAN")
    print("="*60)
    
    try: # Manejo de excepciones para entradas inválidas
        while True: # Validar número de filas y columnas
            filas = int(input("\nIngrese el número de filas de la matriz: "))
            columnas = int(input("Ingrese el número de columnas de la matriz: "))
            if filas <= 0 or columnas <= 0: # Validar valores positivos
                print("Error: El número de filas y columnas debe ser positivo")
                continue
            break
        print(f"\nIngrese los elementos de la matriz de {filas}x{columnas}:")
        print("(Ingrese los valores separados por espacios)\n")
        # Matriz para almacenar los valores
        matriz = []
        for i in range(filas): # Iterar sobre cada fila
            while True: # Validar entrada de fila
                try:
                    fila = input(f"Fila {i+1}: ").split()
                    fila = [float(x) for x in fila]
                    if len(fila) != columnas: # Validar número de columnas
                        print(f"Error: Debe ingresar {columnas} valores")
                        continue
                    matriz.append(fila)
                    break
                except ValueError: # Capturar errores de conversión
                    print("Error: Ingrese solo números separados por espacios")
        # Convertir a numpy array
        matriz = np.array(matriz)
        # Resolver usando Gauss-Jordan
        resultado = gauss_jordan(matriz)
        # Imprimir resultado final
        print("\n" + "="*60)
        print("RESULTADO FINAL:")
        print("="*60)
        imprimir_matriz(resultado, "Matriz en forma escalonada reducida:")
        print ("¿Quiere realizar otra operación? 1. Sí  2. No")
    except ValueError: # Capturar errores de conversión
        print("Error: Entrada inválida")
    except Exception as e: # Capturar cualquier otro error
        print(f"Error: {e}")

def menu():

    """
        Menú principal del programa en terminal
    """

# Encabezado del menú
    print("\n" + "="*60)
    print("MENÚ PRINCIPAL")
    print("="*60)
    print("1. Reducir matriz por Gauss-Jordan")
    print("2. Salir")
    while True: # Bucle del menú
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1": # Opción para reducir matriz
            resolver_sistema()
        elif opcion == "2": # Opción para salir
            print("\n¡Hasta luego!")
            break
        else: # Opción inválida
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__": # Punto de entrada del programa
    menu()