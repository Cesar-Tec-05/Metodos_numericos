# ================================================================
# TITULO: Regla de Cramer - Resolución de sistemas lineales
# AUTOR: Cesar de Jesus Becerra Vera
# FECHA: 18 de Mayo de 2026
# VERSION: 1.0
# ARCHIVO: main.py
# CENTRO UNIVERSITARIO DE LOS ALTOS / UNIVERSIDAD DE GUADALAJARA
# INGENIERIA EN COMPUTACION / MÉTODOS NUMÉRICOS
# DESCRIPCIÓN: Programa interactivo que aplica la Regla de Cramer
# ================================================================

# Importaciones 
import numpy as np

def imprimir_sistema(A, b):
    """
    Imprime el sistema Ax = b en formato legible.
    Argumentos:
        A: matriz de coeficientes (nxn)
        b: vector independiente (n,)
    """
    n = A.shape[0]
    print('\nSistema:')
    for i in range(n):
        fila = '  '.join(f"{A[i,j]:8.4f}" for j in range(n))
        print(f"[{fila}]  |  {b[i]:8.4f}")

def cramer(A, b):
    """
    Resuelve el sistema Ax = b usando la Regla de Cramer.
    Retorna un arreglo con la solución o lanza ValueError si A es singular.
    """
    det_A = np.linalg.det(A)
    if abs(det_A) < 1e-12:
        raise ValueError("La matriz de coeficientes es singular (determinante ≈ 0).")
    n = A.shape[0]
    x = np.zeros(n, dtype=float)
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        det_Ai = np.linalg.det(Ai)
        x[i] = det_Ai / det_A
    return x

def solicitar_sistema():
    """
    Solicita al usuario el tamaño del sistema y los coeficientes.
    Si el usuario pulsa Enter cuando se le pide la matriz completa,
    se generará automáticamente un sistema aleatorio invertible.
    Retorna: A, b (numpy arrays)
    """
    print("\n=== REGISTRO DEL SISTEMA PARA REGLA DE CRAMER ===")
    while True:
        try:
            n_in = input("Ingrese el número de incógnitas n (Enter para usar n=2): ").strip()
            if n_in == "":
                n = 2
            else:
                n = int(n_in)
            if n <= 0:
                print("Error: n debe ser un entero positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
    print("\nA continuación puede ingresar la matriz A fila por fila," )
    print("o simplemente pulsar Enter para generar un ejemplo aleatorio invertible.")
    entrada = input("Pulse Enter para autocompletar o escriba 'm' para meter A manualmente: ").strip().lower()
    if entrada != 'm' and entrada == '':
        # Generar matriz aleatoria invertible y vector b
        rng = np.random.default_rng()
        # generar hasta encontrar una matriz invertible
        while True:
            A = rng.integers(-9, 10, size=(n, n)).astype(float)
            if abs(np.linalg.det(A)) > 1e-6:
                break
        b = rng.integers(-9, 10, size=(n,)).astype(float)
        print("\nSe generó automáticamente el siguiente sistema de ejemplo:")
        imprimir_sistema(A, b)
        return A, b
    # Modo manual
    A = np.zeros((n, n), dtype=float)
    b = np.zeros(n, dtype=float)
    print("\nIngrese cada fila de A como n números separados por espacios.")
    print("Si presiona Enter en una fila, esa fila se autocompletará con ceros.")
    for i in range(n):
        while True:
            fila = input(f"Fila {i+1} (coeficientes A): ").strip()
            if fila == "":
                # autocompletar con ceros
                A[i, :] = 0.0
                break
            parts = fila.split()
            if len(parts) != n:
                print(f"Debe ingresar exactamente {n} valores. Intente de nuevo.")
                continue
            try:
                A[i, :] = [float(p) for p in parts]
                break
            except ValueError:
                print("Entrada inválida. Use números separados por espacios.")
    print("\nIngrese el vector b (n valores). Pulse Enter para autocompletar con ceros.")
    while True:
        b_in = input("b (valores separados por espacios o Enter): ").strip()
        if b_in == "":
            b = np.zeros(n, dtype=float)
            break
        parts = b_in.split()
        if len(parts) != n:
            print(f"Debe ingresar exactamente {n} valores. Intente de nuevo.")
            continue
        try:
            b = np.array([float(p) for p in parts], dtype=float)
            break
        except ValueError:
            print("Entrada inválida. Use números separados por espacios.")
    print("\nSistema ingresado:")
    imprimir_sistema(A, b)
    return A, b

def main():
    """
    Menú principal del programa.
    """
    print("\n" + "="*70)
    print("         PROGRAMA: REGLA DE CRAMER - SISTEMAS LINEALES")
    print("="*70)
    while True:
        print("\nOpciones:")
        print("  1. Resolver un sistema con Regla de Cramer")
        print("  2. Salir")
        opc = input("Seleccione una opción (1-2): ").strip()
        if opc == '1':
            try:
                A, b = solicitar_sistema()
                detA = np.linalg.det(A)
                print(f"\nDeterminante de A: {detA:.6f}")
                if abs(detA) < 1e-12:
                    print("La matriz A es singular o casi singular. No se puede aplicar la Regla de Cramer.")
                    continue
                x = cramer(A, b)
                print("\nSolución (x):")
                for i, xi in enumerate(x, 1):
                    print(f"  x{i} = {xi:.8f}")
            except Exception as e:
                print(f"Error: {e}")
        elif opc == '2':
            print("\nGracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == '__main__':
    main()
