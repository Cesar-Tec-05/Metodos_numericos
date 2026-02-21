# ================================================================
# TITULO: Método de la Bisección - Cálculo de Raíces
# AUTOR: Cesar de Jesus Becerra Vera
# FECHA: 20 de Febrero de 2026
# VERSION: 1.0
# ARCHIVO: main.py
# CENTRO UNIVERSITARIO DE LOS ALTOS / UNIVERSIDAD DE GUADALAJARA
# INGENIERIA EN COMPUTACION / 4TO SEMESTRE
# PROFESOR: JUAN MANUEL
# DESCRIPCIÓN: Programa interactivo que implementa el método de la bisección para encontrar raíces de funciones.
# ================================================================

# Importación de librerías necesarias
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

"""
    Funcion para mostrar el menú principal y obtener la opción del usuario.
        Retorna: 'calcular' para iniciar el cálculo de raíces o 'salir' para terminar el programa.
"""
def mostrar_menu():
    # Mostrar el menú principal
    print("\n" + "="*70)
    print("             MÉTODO DE LA BISECCIÓN - CÁLCULO DE RAÍCES")
    print("="*70)
    print("\n📋 MENÚ PRINCIPAL:")
    print("   1. Calcular raíz de una función")
    print("   2. Salir del programa")
    print("-"*70)
    while True: # Validar la opción ingresada
        opcion = input("Selecciona una opción (1 o 2): ").strip()
        if opcion == '1':
            return 'calcular'
        elif opcion == '2':
            return 'salir'
        else:
            print("⚠️  Opción inválida. Por favor ingresa 1 o 2.\n")

"""
    Función para preguntar si el usuario desea continuar con otro cálculo.
        Retorna: True si desea continuar, False si desea salir.  
"""
def preguntar_continuar():
    print("\n" + "="*70)
    while True: # Validar la respuesta del usuario
        respuesta = input("¿Deseas realizar otro cálculo? (s/n): ").strip().lower()
        if respuesta in ['s', 'si', 'sí', 'yes', 'y']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print("⚠️  Respuesta inválida. Por favor ingresa 's' para sí o 'n' para no.\n")

# Variable para controlar el ciclo del programa
programa_activo = True

# Bucle principal del programa
while programa_activo:
    opcion = mostrar_menu() # Mostrar el menú y obtener la opción del usuario
    if opcion == 'salir': # Si el usuario eligió salir, terminar el programa
        print("\n👋 ¡Gracias por usar el programa! Hasta pronto.\n")
        break
    # Si eligió calcular, ejecutar el método de bisección
    print("\n" + "="*70)
    # Solicitar la función con validación
    while True: # Validar que se ingrese una función
        fun = input("Ingresa la función f(x) en términos de x (ejemplo: 'x**2 - 4'): ").strip()
        if not fun: # Validar que no esté vacía
            print("⚠️  Error: Debes ingresar una función. Intenta de nuevo.\n")
            continue
        # Validar que la función sea evaluable
        try:
            test_val = eval(fun.replace('x', '(0)'))
            break
        except Exception as e:
            print(f"⚠️  Error al evaluar la función: {e}")
            print("Asegúrate de usar sintaxis Python válida (ejemplo: x**2 + 3*x - 5)\n")

    """
    Función para evaluar la función ingresada por el usuario.
        Parámetros: x (valor numérico para evaluar la función)
        Retorna: El resultado de evaluar la función en x.
    """
    def f(x):
        return eval(fun)

    print("\n>>> Graficando función para análisis visual...")
    # Rango inicial amplio para la gráfica
    x_range = np.linspace(-10, 10, 1000) # 1000 puntos para una gráfica suave
    try:
        # Evaluar la función en el rango para graficar
        y_range = [f(x) for x in x_range]
        # Crear la gráfica
        fig = plt.figure(figsize=(10, 6))
        ax = plt.gca()
        plt.plot(x_range, y_range, 'b-', linewidth=2, label=f'f(x) = {fun}')
        plt.grid(True, alpha=0.3)
        # Ejes en el centro
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        # Etiquetas y título
        plt.xlabel('x', loc='right')
        plt.ylabel('y', loc='top')
        plt.title('Gráfica de la función f(x)')
        plt.legend()
        # Buscar cambios de signo para recomendaciones
        cambios_signo = []
        for i in range(len(y_range) - 1):
            if y_range[i] * y_range[i + 1] < 0:
                cambios_signo.append((x_range[i], x_range[i + 1]))
        # Marcar los cambios de signo en la gráfica
        if cambios_signo:
            for cs in cambios_signo[:5]:  # Mostrar máximo 5
                x_mid = (cs[0] + cs[1]) / 2
                plt.axvline(x=x_mid, color='r', linestyle='--', alpha=0.5)
                plt.plot(x_mid, 0, 'ro', markersize=8)
        print("\n✓ Gráfica generada. Cierra la ventana para continuar...\n")
        plt.show()
        print("Continuando con el método de bisección...\n")
        # Mostrar recomendaciones basadas en cambios de signo
        if cambios_signo:
            print(f"📊 ANÁLISIS: Se detectaron {len(cambios_signo)} posibles raíces en [-10, 10]")
            print("   Cambios de signo encontrados (zonas donde hay raíces):\n")
            for i, (x1, x2) in enumerate(cambios_signo[:5], 1):
                print(f"   {i}. Entre x ≈ {x1:.2f} y x ≈ {x2:.2f}")
            print()
        else:
            print("⚠️  No se detectaron cambios de signo evidentes en [-10, 10]")
            print("   Puede que necesites ajustar el rango de búsqueda.\n")
    except Exception as e:
        print(f"⚠️  No se pudo graficar: {e}")
        print("Continuando sin gráfica...\n")

    """
    Función para solicitar los parámetros de barrido al usuario.
        Retorna: inicio_barrido, fin_barrido, paso
    """
    def variables():
        while True: # Validar el inicio del barrido
            try:
                inicio_barrido = float(input("Ingresa el inicio del barrido (ejemplo: -5): "))
                break
            except ValueError:
                print("⚠️  Error: Ingresa un número válido.\n")
        while True: # Validar el final del barrido
            try:
                fin_barrido = float(input("Ingresa el final del barrido (ejemplo: 5): "))
                if fin_barrido <= inicio_barrido:
                    print("⚠️  Error: El final debe ser mayor que el inicio.\n")
                    continue
                break
            except ValueError:
                print("⚠️  Error: Ingresa un número válido.\n")
        # Sugerir paso automáticamente
        rango = fin_barrido - inicio_barrido
        paso_sugerido = rango / 100  # 100 puntos de muestreo   
        while True: # Validar el paso del barrido
            try:
                paso_input = input(f"Ingresa el paso del barrido (sugerido: {paso_sugerido:.3f}): ").strip()
                if paso_input == "": # Si el usuario presiona Enter, usar el paso sugerido
                    paso = paso_sugerido
                    print(f"   Usando paso sugerido: {paso:.3f}")
                else: # Validar que el paso ingresado sea un número positivo y adecuado para el rango
                    paso = float(paso_input)
                    if paso <= 0:
                        print("⚠️  Error: El paso debe ser positivo.\n")
                        continue
                    if paso >= (fin_barrido - inicio_barrido):
                        print("⚠️  Error: El paso es demasiado grande para el rango.\n")
                        continue
                break
            except ValueError:
                print("⚠️  Error: Ingresa un número válido.\n")
        return inicio_barrido, fin_barrido, paso

    # Variables para el barrido inicial
    inicio_barrido, fin_barrido, paso = variables()

    # Solicitar tolerancia con validación
    while True:
        try:
            tol_input = input("\nIngresa la tolerancia deseada (presiona Enter para usar 0.00001): ").strip()
            if tol_input == "":
                tolerancia = 0.00001
            else:
                tolerancia = float(tol_input)
                if tolerancia <= 0:
                    print("⚠️  Error: La tolerancia debe ser positiva.\n")
                    continue
            break
        except ValueError:
            print("⚠️  Error: Ingresa un número válido.\n")
    # Limitar el número máximo de iteraciones para evitar bucles infinitos
    max_iteraciones = 150 
    print("\n" + "="*70)
    print(">>> Buscando intervalo inicial...")
    print("="*70)
    # BARRIDO INICIAL PARA ENCONTRAR INTERVALO CON CAMBIO DE SIGNO
    a = inicio_barrido
    b = a + paso
    intervalo_encontrado = False
    intentos = 0
    max_intentos = int((fin_barrido - inicio_barrido) / paso)
    # Avanzar el paso hasta encontrar un cambio de signo o llegar al final del barrido
    while a < fin_barrido:
        intentos += 1
        try:
            fa = f(a)
            fb = f(b)
            # Verificar si hay un cambio de signo entre f(a) y f(b)
            if fa * fb < 0:
                intervalo_encontrado = True
                print(f"\n✓ ¡Intervalo válido encontrado! -> [{a:.4f}, {b:.4f}]")
                print(f"  f({a:.4f}) = {fa:.6f}")
                print(f"  f({b:.4f}) = {fb:.6f}")
                print(f"  Producto f(a)*f(b) = {fa * fb:.6f} < 0 ✓")
                break
        except Exception as e:
            print(f"⚠️  Error evaluando f({a}) o f({b}): {e}")
        # Si no, avanzamos el paso
        a = b
        b = a + paso
        # Mostrar progreso cada 20%
        if intentos % max(1, max_intentos // 5) == 0:
            progreso = (intentos / max_intentos) * 100
            print(f"   Búsqueda: {progreso:.0f}% completado... (revisando x ≈ {a:.2f})")
    # --- MÉTODO DE BISECCIÓN ---
    if intervalo_encontrado:
        print("\n" + "="*70)
        print(">>> Iniciando Método de Bisección...")
        print("="*70)
        print(f"\n{'Iter':<6} {'a':<12} {'b':<12} {'c (pm)':<12} {'f(c)':<12} {'Error':<12}")
        print("-" * 70)
        # Inicialización de variables para el método de bisección
        contador = 0
        error = abs(b - a) # Error inicial (tamaño del intervalo)
        c_anterior = a
        # El bucle principal de la bisección
        while error > tolerancia and contador < max_iteraciones:
            c = (a + b) / 2   # Calcular punto medio
            try:
                fc = f(c)         # Evaluar función en el medio
            except Exception as e:
                print(f"\n⚠️  Error al evaluar f({c}): {e}")
                break
            # Imprimir la fila de la tabla
            print(f"{contador:<6} {a:<12.6f} {b:<12.6f} {c:<12.6f} {fc:<12.6f} {error:<12.6f}")
            # Verificar si se ha encontrado una raíz exacta (o muy cercana a cero)
            if abs(fc) < 1e-10: # Se encuentra raíz exacta (casi cero)
                print(f"\n✓ ¡Raíz exacta encontrada! f({c:.6f}) ≈ 0")
                break
            # Lógica de decisión: ¿A qué lado está la raíz?
            if f(a) * fc < 0:
                b = c  # La raíz está a la izquierda, mover el límite derecho
            else:
                a = c  # La raíz está a la derecha, mover el límite izquierdo
            # Recalculamos el error y aumentamos contador
            c_anterior = c
            error = abs(b - a)
            contador += 1
        # Mostrar resultado final con formato destacado
        print("-" * 70)
        print(f"\n{'='*70}")
        print("RESULTADO FINAL:")
        print(f"{'='*70}")
        print(f"  Raíz aproximada:     x = {c:.10f}")
        print(f"  f(x) =                   {f(c):.10e}")
        print(f"  Error final:             {error:.10e}")
        print(f"  Tolerancia objetivo:     {tolerancia:.10e}")
        print(f"  Iteraciones totales:     {contador}")
        print(f"{'='*70}\n")
        # Mostrar gráfica final con la raíz
        try:
            x_plot = np.linspace(inicio_barrido, fin_barrido, 500)
            y_plot = [f(x) for x in x_plot]
            # Crear la gráfica
            plt.figure(figsize=(10, 6))
            ax = plt.gca()
            plt.plot(x_plot, y_plot, 'b-', linewidth=2, label=f'f(x) = {fun}')
            plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
            plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
            plt.plot(c, f(c), 'ro', markersize=10, label=f'Raíz: x = {c:.6f}')
            plt.grid(True, alpha=0.3)
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Raíz encontrada por el Método de Bisección')
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"⚠️  No se pudo mostrar la gráfica final: {e}")
    # Si no se encontró ningún intervalo con cambio de signo, mostrar mensaje de error y sugerencias
    else:
        print("\n" + "="*70)
        print("⚠️  ERROR: No se encontró ningún cambio de signo")
        print("="*70)
        print("\n💡 SUGERENCIAS:")
        print("   1. Amplía el rango de búsqueda (inicio_barrido y fin_barrido)")
        print("   2. Reduce el paso para una búsqueda más fina")
        print("   3. Verifica que la función tenga raíces reales")
        print("   4. Observa la gráfica para identificar dónde buscar")
        print("="*70 + "\n")
    # Preguntar si desea continuar
    if not preguntar_continuar():
        print("\n👋 ¡Gracias por usar el programa! Hasta pronto.\n")
        programa_activo = False
