# ================================================================
# TITULO: Factorización LU con pivoteo parcial
# AUTOR: Cesar de Jesus Becerra Vera (adaptado por alumno)
# FECHA: 18 de Mayo de 2026
# VERSION: 1.0
# ARCHIVO: main.py
# CENTRO UNIVERSITARIO DE LOS ALTOS / UNIVERSIDAD DE GUADALAJARA
# INGENIERIA EN COMPUTACION / MÉTODOS NUMÉRICOS
# DESCRIPCIÓN: Programa interactivo que calcula la factorización LU
# ================================================================

# Importaciones
import numpy as np

def imprimir_matriz(M, nombre="M"):
    """
    Imprime una matriz con formato legible.
    """
    filas, cols = M.shape
    print(f"\n{nombre} =")
    for i in range(filas):
        print("  ", "  ".join(f"{M[i,j]:8.4f}" for j in range(cols)))

def lu_pivot(A):
    """
    Calcula la factorización LU con pivoteo parcial.
    Retorna P, L, U donde P*A = L*U.
    L tiene 1's en la diagonal.
    Lanzará ValueError si la matriz no es cuadrada o se detecta singularidad.
    """
    A = A.astype(float).copy()
    n, m = A.shape
    if n != m:
        raise ValueError("La matriz debe ser cuadrada para LU.")
    P = np.eye(n)
    L = np.zeros((n, n), dtype=float)
    U = A.copy()
    for k in range(n):
        # pivoteo parcial
        piv = np.argmax(np.abs(U[k:, k])) + k
        if abs(U[piv, k]) < 1e-12:
            raise ValueError("Matriz singular o casi singular detectada durante el pivoteo.")
        if piv != k:
            # intercambiar filas en U
            U[[k, piv], :] = U[[piv, k], :]
            # intercambiar en P
            P[[k, piv], :] = P[[piv, k], :]
            # intercambiar las filas previas de L (columna 0..k-1)
            if k >= 1:
                L[[k, piv], :k] = L[[piv, k], :k]
        # factorizar columna k
        L[k, k] = 1.0
        for i in range(k+1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] = U[i, k:] - L[i, k] * U[k, k:]
    return P, L, U

def forward_substitution(L, b):
    n = L.shape[0]
    y = np.zeros(n, dtype=float)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])
    return y

def backward_substitution(U, y):
    n = U.shape[0]
    x = np.zeros(n, dtype=float)
    for i in range(n-1, -1, -1):
        if abs(U[i, i]) < 1e-12:
            raise ValueError("Elemento diagonal de U ≈ 0; no se puede realizar sustitución hacia atrás.")
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

def solicitar_matriz():
    print("\n=== INGRESO DE MATRIZ PARA FACTORIZACIÓN LU ===")
    while True:
        try:
            n_in = input("Ingrese el tamaño n (Enter para usar n=3): ").strip()
            if n_in == "":
                n = 3
            else:
                n = int(n_in)
            if n <= 0:
                print("n debe ser entero positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
    print("\nPulse Enter para que el programa genere una matriz invertible de ejemplo,")
    print("o escriba 'm' para ingresar la matriz manualmente fila por fila.")
    modo = input("(Enter = autocompletar, m = manual): ").strip().lower()
    if modo == "m":
        A = np.zeros((n, n), dtype=float)
        print(f"Ingrese cada fila de A con {n} valores separados por espacios. Enter en una fila autocompleta con ceros.")
        for i in range(n):
            while True:
                fila = input(f"Fila {i+1}: ").strip()
                if fila == "":
                    A[i, :] = 0.0
                    break
                parts = fila.split()
                if len(parts) != n:
                    print(f"Debe ingresar exactamente {n} valores.")
                    continue
                try:
                    A[i, :] = [float(p) for p in parts]
                    break
                except ValueError:
                    print("Entrada inválida. Use números.")
    else:
        rng = np.random.default_rng()
        while True:
            A = rng.integers(-5, 6, size=(n, n)).astype(float)
            try:
                # Intentar factorizar para asegurar invertibilidad
                _ = np.linalg.inv(A)
                break
            except np.linalg.LinAlgError:
                continue
        print("\nSe generó automáticamente la matriz A de ejemplo:")
        imprimir_matriz(A, "A")
    # solicitar vector b
    print("\nIngrese el vector b (n valores) o pulse Enter para autocompletar con ceros.")
    while True:
        b_in = input("b (valores separados por espacios o Enter): ").strip()
        if b_in == "":
            b = np.zeros(n, dtype=float)
            break
        parts = b_in.split()
        if len(parts) != n:
            print(f"Ingrese exactamente {n} valores.")
            continue
        try:
            b = np.array([float(p) for p in parts], dtype=float)
            break
        except ValueError:
            print("Entrada inválida.")
    return A, b


def main():
    print("\n" + "="*70)
    print("         PROGRAMA: FACTORIZACIÓN LU - MÉTODOS NUMÉRICOS")
    print("="*70)
    while True:
        print("\nOpciones:")
        print("  1. Calcular LU y resolver Ax = b")
        print("  2. Salir")
        opc = input("Seleccione una opción (1-2): ").strip()
        if opc == '1':
            try:
                A, b = solicitar_matriz()
                imprimir_matriz(A, "A")
                P, L, U = lu_pivot(A)
                imprimir_matriz(P, "P")
                imprimir_matriz(L, "L")
                imprimir_matriz(U, "U")
                # Resolver sistema: PAx = Pb -> LUx = Pb
                Pb = P.dot(b)
                y = forward_substitution(L, Pb)
                x = backward_substitution(U, y)
                print("\nSolución x:")
                for i, xi in enumerate(x, 1):
                    print(f"  x{i} = {xi:12.8f}")
                detA = np.prod(np.diag(U))
                print(f"\nDeterminante aproximado de A: {detA:.6f}")
            except Exception as e:
                print(f"Error: {e}")
        elif opc == '2':
            print("\nGracias. Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == '__main__':
    main()
