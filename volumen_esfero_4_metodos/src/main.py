# ================================================================
# TITULO: Volumen de Esfera - Resolución con 4 Métodos Numéricos
# AUTOR: Cesar de Jesus Becerra Vera
# FECHA: 24 de Marzo de 2026
# VERSION: 1.0
# ARCHIVO: main.py
# CENTRO UNIVERSITARIO DE LOS ALTOS / UNIVERSIDAD DE GUADALAJARA
# INGENIERIA EN COMPUTACION / 4TO SEMESTRE
# PROFESOR: JUAN MANUEL
# DESCRIPCIÓN: Programa interactivo que implementa 4 métodos numéricos (Bisección, Regla Falsa, Newton-Raphson y Secante).
# ================================================================

# Importación de librerías necesarias
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Constantes del problema
R = 3  # Radio de la esfera

"""
    Función para definir la ecuación a resolver: π*h²*(3r - h/3) - 30 = 0
    Parámetros: h (altura del casquete esférico)
    Retorna: El resultado de evaluar la ecuación en h
"""
def f(h):
    return math.pi * (h ** 2) * (3 * R - h / 3) - 30

"""
    Función para mostrar el menú principal y obtener la opción del usuario.
    Retorna: El número del método seleccionado o 0 para salir
"""
def mostrar_menu():
    print("\n" + "=" * 70)
    print("   VOLUMEN DE ESFERA - RESOLUCIÓN CON 4 MÉTODOS NUMÉRICOS")
    print("=" * 70)
    print("\n📋 ECUACIÓN A RESOLVER: π*h²*(3r - h/3) - 30 = 0")
    print(f"   Radio de la esfera (r) = {R}")
    print(f"   Ecuación: π*h²*(9 - h/3) - 30 = 0")
    print("\n" + "-" * 70)
    print("📊 SELECCIONA UN MÉTODO:")
    print("   1. Método de la Bisección")
    print("   2. Método de la Regla Falsa")
    print("   3. Método de Newton-Raphson")
    print("   4. Método de la Secante")
    print("   5. Salir del programa")
    print("-" * 70)
    while True:  # Validar la opción ingresada
        opcion = input("Selecciona una opción (1-5): ").strip()
        if opcion in ['1', '2', '3', '4', '5']:
            return int(opcion)
        else:
            print("⚠️  Opción inválida. Por favor ingresa un número entre 1 y 5.\n")

"""
    Función para preguntar si el usuario desea continuar con otro cálculo.
    Retorna: True si desea continuar, False si desea salir.
"""
def preguntar_continuar():
    print("\n" + "=" * 70)
    while True:  # Validar la respuesta del usuario
        respuesta = input("¿Deseas intentar otro método? (s/n): ").strip().lower()
        if respuesta in ['s', 'si', 'sí', 'yes', 'y']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print("⚠️  Respuesta inválida. Por favor ingresa 's' para sí o 'n' para no.\n")

"""
    Función para graficar la función y visualizar las raíces
    Parámetros: Ninguno (utiliza la función f global)
"""
def graficar_funcion():
    print("\n>>> Graficando función para análisis visual...")
    try:
        # Crear rango de valores para h (de 0.1 a 6, ya que el volumen es limitado)
        h_range = np.linspace(0.1, 6, 1000)
        y_range = [f(h) for h in h_range]
        # Crear la gráfica
        fig = plt.figure(figsize=(10, 6))
        plt.plot(h_range, y_range, 'b-', linewidth=2, label='f(h) = π*h²*(9 - h/3) - 30')
        plt.axhline(y=0, color='r', linestyle='--', linewidth=1, label='y = 0 (raíz)')
        plt.grid(True, alpha=0.3)
        plt.xlabel('h (altura del casquete)', fontsize=12)
        plt.ylabel('f(h)', fontsize=12)
        plt.title('Función: π*h²*(3r - h/3) - 30 = 0 (r = 3)', fontsize=14, fontweight='bold')
        plt.legend(fontsize=10)
        plt.tight_layout()
        # Mostrar la gráfica
        plt.show()
        print("✅ Gráfica mostrada exitosamente.")
    except Exception as e:
        print(f"⚠️  Error al graficar: {e}")

"""
    Implementación del Método de la Bisección
    Parámetros:
        a, b: Intervalo donde se busca la raíz
        tolerancia: Criterio de parada (cuando |b - a| < tolerancia)
        max_iteraciones: Número máximo de iteraciones
    Retorna: tupla (raiz, iteraciones, convergio, historial)
"""
def biseccion(a, b, tolerancia, max_iteraciones):
    historial = []
    convergio = False
    motivo = ""
    print("\n" + "=" * 70)
    print("🔄 EJECUTANDO MÉTODO DE LA BISECCIÓN")
    print("=" * 70)
    print(f"Intervalo inicial: [{a}, {b}]")
    print(f"Tolerancia: {tolerancia}")
    print(f"Máximo de iteraciones: {max_iteraciones}\n")
    # Validar que f(a) y f(b) tengan signos opuestos
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        motivo = "⚠️  Error: f(a) y f(b) deben tener signos opuestos."
        print(motivo)
        return None, 0, False, historial, motivo
    print(f"{'Iter':<6} {'a':<14} {'b':<14} {'c':<14} {'f(c)':<14} {'Error':<14}")
    print("-" * 70)
    for iteracion in range(1, max_iteraciones + 1):
        c = (a + b) / 2  # Punto medio
        fc = f(c)
        error = abs(b - a)
        historial.append({
            'iteracion': iteracion,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': fc,
            'error': error
        })
        # Mostrar resultado de la iteración
        print(f"{iteracion:<6} {a:<14.10f} {b:<14.10f} {c:<14.10f} {fc:<14.10e} {error:<14.10e}")
        # Verificar criterio de convergencia
        if abs(fc) < tolerancia or error < tolerancia:
            convergio = True
            motivo = f"✅ Convergencia alcanzada en iteración {iteracion}"
            print(f"\n{motivo}")
            return c, iteracion, convergio, historial, motivo
        # Actualizar el intervalo
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    motivo = f"⚠️  No convergió después de {max_iteraciones} iteraciones"
    print(f"\n{motivo}")
    return (a + b) / 2, max_iteraciones, convergio, historial, motivo

"""
    Implementación del Método de la Regla Falsa
    Parámetros:
        a, b: Intervalo donde se busca la raíz
        tolerancia: Criterio de parada
        max_iteraciones: Número máximo de iteraciones
    Retorna: tupla (raiz, iteraciones, convergio, historial)
"""
def regla_falsa(a, b, tolerancia, max_iteraciones):
    historial = []
    convergio = False
    motivo = ""
    print("\n" + "=" * 70)
    print("🔄 EJECUTANDO MÉTODO DE LA REGLA FALSA")
    print("=" * 70)
    print(f"Intervalo inicial: [{a}, {b}]")
    print(f"Tolerancia: {tolerancia}")
    print(f"Máximo de iteraciones: {max_iteraciones}\n")
    # Validar que f(a) y f(b) tengan signos opuestos
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        motivo = "⚠️  Error: f(a) y f(b) deben tener signos opuestos."
        print(motivo)
        return None, 0, False, historial, motivo
    print(f"{'Iter':<6} {'a':<14} {'b':<14} {'c':<14} {'f(c)':<14} {'Error':<14}")
    print("-" * 70)
    for iteracion in range(1, max_iteraciones + 1):
        fa = f(a)
        fb = f(b)
        # Punto de intersección de la recta secante con el eje x
        if fa == fb:
            motivo = "⚠️  Error: f(a) = f(b), no se puede calcular la regla falsa"
            print(motivo)
            return None, iteracion, False, historial, motivo
        c = a - (fa * (b - a)) / (fb - fa)
        fc = f(c)
        error = abs(b - a)
        historial.append({
            'iteracion': iteracion,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': fc,
            'error': error
        })
        # Mostrar resultado de la iteración
        print(f"{iteracion:<6} {a:<14.10f} {b:<14.10f} {c:<14.10f} {fc:<14.10e} {error:<14.10e}")
        # Verificar criterio de convergencia
        if abs(fc) < tolerancia or error < tolerancia:
            convergio = True
            motivo = f"✅ Convergencia alcanzada en iteración {iteracion}"
            print(f"\n{motivo}")
            return c, iteracion, convergio, historial, motivo
        # Actualizar el intervalo
        if fa * fc < 0:
            b = c
        else:
            a = c
    motivo = f"⚠️  No convergió después de {max_iteraciones} iteraciones"
    print(f"\n{motivo}")
    return a - (f(a) * (b - a)) / (f(b) - f(a)), max_iteraciones, convergio, historial, motivo

"""
    Función para calcular la derivada numérica de la función f
    Parámetros:
        h: punto donde calcular la derivada
        paso: incremento pequeño para la aproximación (default: 1e-5)
    Retorna: Aproximación de f'(h) usando diferencias centrales
"""
def derivada_numerica(h, paso=1e-5):
    try:
        # Usar diferencias centrales para mayor precisión
        return (f(h + paso) - f(h - paso)) / (2 * paso)
    except:
        # Si falla, usar diferencias hacia adelante
        return (f(h + paso) - f(h)) / paso

"""
    Implementación del Método de Newton-Raphson
    Parámetros:
        h0: valor inicial (punto de partida)
        tolerancia: Criterio de parada
        max_iteraciones: Número máximo de iteraciones
    Retorna: tupla (raiz, iteraciones, convergio, historial)
"""
def newton_raphson(h0, tolerancia, max_iteraciones):
    historial = []
    convergio = False
    print("\n" + "=" * 70)
    print("🔄 EJECUTANDO MÉTODO DE NEWTON-RAPHSON")
    print("=" * 70)
    print(f"Valor inicial (h0): {h0}")
    print(f"Tolerancia: {tolerancia}")
    print(f"Máximo de iteraciones: {max_iteraciones}\n")
    print(f"{'Iter':<6} {'h_n':<14} {'f(h_n)':<14} {'f\'(h_n)':<14} {'h_(n+1)':<14} {'Error':<14}")
    print("-" * 85)
    h_actual = h0
    for iteracion in range(1, max_iteraciones + 1):
        try:
            fh = f(h_actual)
            fh_prima = derivada_numerica(h_actual)
            # Validar que la derivada no sea cero
            if abs(fh_prima) < 1e-15:
                motivo = "⚠️  Error: La derivada es muy cercana a cero (f'(h) ≈ 0)"
                print(f"\n{motivo}")
                return None, iteracion, False, historial, motivo
            h_siguiente = h_actual - fh / fh_prima
            error = abs(h_siguiente - h_actual)
            historial.append({
                'iteracion': iteracion,
                'h_n': h_actual,
                'f(h_n)': fh,
                'f_prima(h_n)': fh_prima,
                'h_siguiente': h_siguiente,
                'error': error
            })
            # Mostrar resultado de la iteración
            print(f"{iteracion:<6} {h_actual:<14.10f} {fh:<14.10e} {fh_prima:<14.10e} {h_siguiente:<14.10f} {error:<14.10e}")
            # Verificar criterio de convergencia
            if abs(fh) < tolerancia or error < tolerancia:
                convergio = True
                motivo = f"✅ Convergencia alcanzada en iteración {iteracion}"
                print(f"\n{motivo}")
                return h_siguiente, iteracion, convergio, historial, motivo
            h_actual = h_siguiente
        except Exception as e:
            motivo = f"⚠️  Error durante la iteración: {e}"
            print(f"\n{motivo}")
            return None, iteracion, False, historial, motivo
    motivo = f"⚠️  No convergió después de {max_iteraciones} iteraciones"
    print(f"\n{motivo}")
    return h_actual, max_iteraciones, convergio, historial, motivo

"""
    Implementación del Método de la Secante
    Parámetros:
        h0, h1: dos valores iniciales
        tolerancia: Criterio de parada
        max_iteraciones: Número máximo de iteraciones
    Retorna: tupla (raiz, iteraciones, convergio, historial)
"""
def metodo_secante(h0, h1, tolerancia, max_iteraciones):
    historial = []
    convergio = False
    print("\n" + "=" * 70)
    print("🔄 EJECUTANDO MÉTODO DE LA SECANTE")
    print("=" * 70)
    print(f"Valores iniciales: h0 = {h0}, h1 = {h1}")
    print(f"Tolerancia: {tolerancia}")
    print(f"Máximo de iteraciones: {max_iteraciones}\n")
    print(f"{'Iter':<6} {'h_(i-1)':<14} {'h_i':<14} {'f(h_(i-1))':<14} {'f(h_i)':<14} {'h_(i+1)':<14} {'Error':<14}")
    print("-" * 100)
    h_anterior = h0
    h_actual = h1
    for iteracion in range(1, max_iteraciones + 1):
        try:
            fh_anterior = f(h_anterior)
            fh_actual = f(h_actual)
            # Validar que el denominador no sea cero
            denominador = fh_actual - fh_anterior
            if abs(denominador) < 1e-15:
                motivo = "⚠️  Error: f(h_i) - f(h_(i-1)) es muy cercano a cero"
                print(f"\n{motivo}")
                return None, iteracion, False, historial, motivo
            h_siguiente = h_actual - (fh_actual * (h_actual - h_anterior)) / denominador
            error = abs(h_siguiente - h_actual)
            historial.append({
                'iteracion': iteracion,
                'h_anterior': h_anterior,
                'h_actual': h_actual,
                'f(h_anterior)': fh_anterior,
                'f(h_actual)': fh_actual,
                'h_siguiente': h_siguiente,
                'error': error
            })
            # Mostrar resultado de la iteración
            print(f"{iteracion:<6} {h_anterior:<14.10f} {h_actual:<14.10f} {fh_anterior:<14.10e} {fh_actual:<14.10e} {h_siguiente:<14.10f} {error:<14.10e}")
            # Verificar criterio de convergencia
            if abs(fh_actual) < tolerancia or error < tolerancia:
                convergio = True
                motivo = f"✅ Convergencia alcanzada en iteración {iteracion}"
                print(f"\n{motivo}")
                return h_siguiente, iteracion, convergio, historial, motivo
            h_anterior = h_actual
            h_actual = h_siguiente
        except Exception as e:
            motivo = f"⚠️  Error durante la iteración: {e}"
            print(f"\n{motivo}")
            return None, iteracion, False, historial, motivo
    motivo = f"⚠️  No convergió después de {max_iteraciones} iteraciones"
    print(f"\n{motivo}")
    return h_actual, max_iteraciones, convergio, historial, motivo

"""
    Función para mostrar y procesar los resultados después de la ejecución de un método
    Parámetros:
        raiz: valor aproximado de la raíz encontrada
        iteraciones: número de iteraciones realizadas
        convergio: booleano indicando si convergió
        historial: lista de diccionarios con el historial de iteraciones
        motivo: mensaje descriptivo del resultado
"""
def procesar_resultados(raiz, iteraciones, convergio, historial, motivo):
    print("\n" + "=" * 70)
    print("📋 RESUMEN DE RESULTADOS")
    print("=" * 70)
    if raiz is not None:
        print(f"✅ Raíz aproximada encontrada: h = {raiz:.10f}")
        print(f"   Número de iteraciones: {iteraciones}")
        print(f"   f(h) = {f(raiz):.10e}")
        print(f"   Volumen del casquete: V = π·h²·(3r - h/3) ≈ {math.pi * (raiz ** 2) * (3 * R - raiz / 3):.10f} u³")
        # Validación: la altura no puede ser mayor que el diámetro
        if raiz > 2 * R:
            print(f"   ⚠️  Advertencia: La altura h = {raiz:.10f} es mayor que el diámetro (2r = {2*R})")
        print(f"\n{motivo}")
    else:
        print(f"❌ No se encontró raíz.")
        print(f"\n{motivo}")

# ============================================================================
# BUCLE PRINCIPAL DEL PROGRAMA
# ============================================================================
programa_activo = True
while programa_activo:
    opcion = mostrar_menu()  # Mostrar el menú y obtener la opción del usuario
    if opcion == 5:  # Si el usuario eligió salir
        print("\n👋 ¡Gracias por usar el programa! Hasta pronto.\n")
        break
    # Graficar la función para visualización
    graficar_funcion()
    # Obtener parámetros del usuario
    print("\n" + "=" * 70)
    print("⚙️  PARÁMETROS DE EJECUCIÓN")
    print("=" * 70)
    
    while True:
        try:
            entrada_tol = input("Ingresa la tolerancia (por defecto: 1e-10): ").strip()
            if entrada_tol == "":
                tolerancia = 1e-10
                print(f"   Usando tolerancia: {tolerancia}")
            else:
                tolerancia = float(entrada_tol)
            if tolerancia <= 0:
                print("⚠️  La tolerancia debe ser un valor positivo.\n")
                continue
            break
        except ValueError:
            print("⚠️  Error: Debes ingresar un número válido.\n")
    
    while True:
        try:
            entrada_iter = input("Ingresa el máximo de iteraciones (por defecto: 100): ").strip()
            if entrada_iter == "":
                max_iteraciones = 100
                print(f"   Usando máximo de iteraciones: {max_iteraciones}")
            else:
                max_iteraciones = int(entrada_iter)
            if max_iteraciones <= 0:
                print("⚠️  El número de iteraciones debe ser positivo.\n")
                continue
            break
        except ValueError:
            print("⚠️  Error: Debes ingresar un número entero válido.\n")
    # Ejecutar el método seleccionado
    try:
        if opcion == 1:  # Bisección
            while True:
                try:
                    entrada_a = input("Ingresa el extremo inferior del intervalo (por defecto: 1.0): ").strip()
                    entrada_b = input("Ingresa el extremo superior del intervalo (por defecto: 2.0): ").strip()
                    
                    if entrada_a == "":
                        a = 1.0
                    else:
                        a = float(entrada_a)
                    
                    if entrada_b == "":
                        b = 2.0
                    else:
                        b = float(entrada_b)
                    
                    if entrada_a == "" and entrada_b == "":
                        print(f"   Usando intervalo: [{a}, {b}]")
                    
                    if a >= b:
                        print("⚠️  Error: a debe ser menor que b.\n")
                        continue
                    break
                except ValueError:
                    print("⚠️  Error: Debes ingresar números válidos.\n")
            raiz, iteraciones, convergio, historial, motivo = biseccion(a, b, tolerancia, max_iteraciones)
            procesar_resultados(raiz, iteraciones, convergio, historial, motivo)
        elif opcion == 2:  # Regla Falsa
            while True:
                try:
                    entrada_a = input("Ingresa el extremo inferior del intervalo (por defecto: 1.0): ").strip()
                    entrada_b = input("Ingresa el extremo superior del intervalo (por defecto: 2.0): ").strip()
                    
                    if entrada_a == "":
                        a = 1.0
                    else:
                        a = float(entrada_a)
                    
                    if entrada_b == "":
                        b = 2.0
                    else:
                        b = float(entrada_b)
                    
                    if entrada_a == "" and entrada_b == "":
                        print(f"   Usando intervalo: [{a}, {b}]")
                    
                    if a >= b:
                        print("⚠️  Error: a debe ser menor que b.\n")
                        continue
                    break
                except ValueError:
                    print("⚠️  Error: Debes ingresar números válidos.\n")
            raiz, iteraciones, convergio, historial, motivo = regla_falsa(a, b, tolerancia, max_iteraciones)
            procesar_resultados(raiz, iteraciones, convergio, historial, motivo)
        elif opcion == 3:  # Newton-Raphson
            while True:
                try:
                    entrada_h0 = input("Ingresa el valor inicial (por defecto: 1.5): ").strip()
                    if entrada_h0 == "":
                        h0 = 1.5
                        print(f"   Usando valor inicial: {h0}")
                    else:
                        h0 = float(entrada_h0)
                    break
                except ValueError:
                    print("⚠️  Error: Debes ingresar un número válido.\n")
            raiz, iteraciones, convergio, historial, motivo = newton_raphson(h0, tolerancia, max_iteraciones)
            procesar_resultados(raiz, iteraciones, convergio, historial, motivo)
        elif opcion == 4:  # Secante
            while True:
                try:
                    entrada_h0 = input("Ingresa el primer valor inicial (por defecto: 1.0): ").strip()
                    entrada_h1 = input("Ingresa el segundo valor inicial (por defecto: 2.0): ").strip()
                    
                    if entrada_h0 == "":
                        h0 = 1.0
                    else:
                        h0 = float(entrada_h0)
                    
                    if entrada_h1 == "":
                        h1 = 2.0
                    else:
                        h1 = float(entrada_h1)
                    
                    if entrada_h0 == "" and entrada_h1 == "":
                        print(f"   Usando valores iniciales: h0={h0}, h1={h1}")
                    
                    if h0 == h1:
                        print("⚠️  Error: h0 y h1 deben ser diferentes.\n")
                        continue
                    break
                except ValueError:
                    print("⚠️  Error: Debes ingresar números válidos.\n")
            raiz, iteraciones, convergio, historial, motivo = metodo_secante(h0, h1, tolerancia, max_iteraciones)
            procesar_resultados(raiz, iteraciones, convergio, historial, motivo)
    except Exception as e:
        print(f"\n❌ Error durante la ejecución del método: {e}")
    # Preguntar si desea intentar otro método
    if not preguntar_continuar():
        print("\n👋 ¡Gracias por usar el programa! Hasta pronto.\n")
        programa_activo = False
