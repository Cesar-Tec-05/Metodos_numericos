# ================================================================
# TITULO: Método de Newton-Raphson - Cálculo de Raíces
# AUTOR: Cesar de Jesus Becerra Vera
# FECHA: 11 de Marzo de 2026
# VERSION: 2.0
# ARCHIVO: Main.py
# CENTRO UNIVERSITARIO DE LOS ALTOS / UNIVERSIDAD DE GUADALAJARA
# INGENIERIA EN COMPUTACION / 4TO SEMESTRE
# PROFESOR: JUAN MANUEL
# DESCRIPCIÓN: Programa interactivo que implementa el método de Newton-Raphson para encontrar raíces de funciones.
# ================================================================

# Importación de librerías necesarias
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

"""
    Función para mostrar el menú principal y obtener la opción del usuario.
        Retorna: 'calcular' para iniciar el cálculo de raíces o 'salir' para terminar el programa.
"""
def mostrar_menu():
    # Mostrar el menú principal
    print("\n" + "="*70)
    print("           MÉTODO DE NEWTON-RAPHSON - CÁLCULO DE RAÍCES")
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

"""
    Función para calcular la derivada numérica de una función.
        Parámetros:
            f: función a derivar
            x: punto donde calcular la derivada
            h: paso para la aproximación (default: 1e-5)
        Retorna: Aproximación de f'(x) usando diferencias centrales
"""
def derivada_numerica(f, x, h=1e-5):
    try:
        # Usar diferencias centrales para mayor precisión: f'(x) ≈ [f(x+h) - f(x-h)] / (2h)
        return (f(x + h) - f(x - h)) / (2 * h)
    except:
        # Si falla, usar diferencias hacia adelante: f'(x) ≈ [f(x+h) - f(x)] / h
        return (f(x + h) - f(x)) / h

"""
    Función que implementa el método de Newton-Raphson para encontrar raíces.
        Parámetros:
            f: función a la que encontrar la raíz
            x0: valor inicial (punto de partida)
            tolerancia: criterio de parada (cuando |f(x)| < tolerancia)
            max_iteraciones: número máximo de iteraciones permitidas
            usar_derivada_numerica: si True, calcula la derivada numéricamente; si False, pide al usuario
            df: función derivada (solo si usar_derivada_numerica es False)
        Retorna: tupla (raiz, iteraciones, convergio, historial)
            raiz: aproximación de la raíz encontrada
            iteraciones: número de iteraciones realizadas
            convergio: True si encontró la raíz, False si no convergió
            historial: lista de tuplas (iteracion, x, f(x), error) para cada paso
"""
def newton_raphson(f, x0, tolerancia, max_iteraciones, usar_derivada_numerica=True, df=None):
    historial = []  # Lista para almacenar el historial de iteraciones
    x_actual = x0
    convergio = False
    # Encabezado de la tabla de iteraciones
    print("\n" + "="*70)
    print("📊 ITERACIONES DEL MÉTODO DE NEWTON-RAPHSON")
    print("="*70)
    print(f"{'Iter':<8} {'x_n':<18} {'f(x_n)':<18} {'|f(x_n)|':<18}")
    print("-" * 70)
    for contador in range(max_iteraciones):
        try:
            # Evaluar la función en el punto actual
            fx = f(x_actual)
            error = abs(fx)
            # Guardar en el historial
            historial.append((contador, x_actual, fx, error))
            # Imprimir el estado actual
            print(f"{contador:<8} {x_actual:<18.10f} {fx:<18.10f} {error:<18.10f}")
            # Condición de parada: Si |f(x)| < tolerancia, se encontró la raíz
            if error < tolerancia:
                convergio = True
                print("-" * 70)
                print(f"✅ Convergencia alcanzada en {contador} iteraciones")
                break
            # Calcular la derivada
            if usar_derivada_numerica:
                dfx = derivada_numerica(f, x_actual)
            else:
                dfx = df(x_actual)
            # Verificar que la derivada no sea cero (evitar división por cero)
            if abs(dfx) < 1e-10:
                print("-" * 70)
                print("⚠️  Error: La derivada es prácticamente cero en este punto.")
                print("   El método no puede continuar (tangente horizontal).")
                break
            # Aplicar la fórmula de Newton-Raphson: x_{n+1} = x_n - f(x_n) / f'(x_n)
            x_nuevo = x_actual - (fx / dfx)
            # Verificar convergencia (cambio relativo muy pequeño)
            if abs(x_nuevo - x_actual) < tolerancia * abs(x_actual) and abs(x_actual) > 0:
                convergio = True
                x_actual = x_nuevo
                print("-" * 70)
                print(f"✅ Convergencia alcanzada por cambio relativo en {contador + 1} iteraciones")
                break
            # Actualizar x para la siguiente iteración
            x_actual = x_nuevo
        except Exception as e:
            print("-" * 70)
            print(f"⚠️  Error durante el cálculo: {e}")
            break
    if not convergio and contador == max_iteraciones - 1:
        print("-" * 70)
        print(f"⚠️  No se alcanzó la convergencia en {max_iteraciones} iteraciones")
    return x_actual, contador if convergio else max_iteraciones, convergio, historial

# Variable para controlar el ciclo del programa
programa_activo = True

# Bucle principal del programa
while programa_activo:
    opcion = mostrar_menu()  # Mostrar el menú y obtener la opción del usuario
    if opcion == 'salir':  # Si el usuario eligió salir, terminar el programa
        print("\n👋 ¡Gracias por usar el programa! Hasta pronto.\n")
        break
    # Si eligió calcular, ejecutar el método de Newton-Raphson
    print("\n" + "="*70)
    print("📝 CONFIGURACIÓN DE LA FUNCIÓN")
    print("="*70)
    # Solicitar la función con validación
    while True:  # Validar que se ingrese una función
        fun = input("\nIngresa la función f(x) en términos de x (ejemplo: 'x**2 - 5'): ").strip()
        if not fun:  # Validar que no esté vacía
            print("⚠️  Error: Debes ingresar una función. Intenta de nuevo.\n")
            continue
        # Validar que la función sea evaluable
        try:
            test_val = eval(fun.replace('x', '(0)'))
            break
        except Exception as e:
            print(f"⚠️  Error al evaluar la función: {e}")
            print("Asegúrate de usar sintaxis Python válida (ejemplo: x**2 - 5 o math.sin(x))\n")
    
    """
    Función para evaluar la función ingresada por el usuario.
        Parámetros: x (valor numérico para evaluar la función)
        Retorna: El resultado de evaluar la función en x.
    """
    def f(x):
        return eval(fun)
    # Preguntar si quiere ingresar la derivada o calcularla numéricamente
    print("\n" + "="*70)
    print("🔧 CONFIGURACIÓN DE LA DERIVADA")
    print("="*70)
    print("\nOpciones para la derivada f'(x):")
    print("   1. Calcular automáticamente (derivada numérica)")
    print("   2. Ingresar la derivada manualmente")
    print("-"*70)
    usar_derivada_numerica = True
    df = None
    while True:
        opcion_derivada = input("Selecciona una opción (1 o 2): ").strip()
        if opcion_derivada == '1':
            usar_derivada_numerica = True
            print("✅ Se usará cálculo numérico automático de la derivada")
            break
        elif opcion_derivada == '2':
            usar_derivada_numerica = False
            # Solicitar la derivada
            while True:
                fun_derivada = input("\nIngresa la derivada f'(x) en términos de x (ejemplo: '2*x'): ").strip()
                if not fun_derivada:
                    print("⚠️  Error: Debes ingresar la derivada. Intenta de nuevo.\n")
                    continue
                try:
                    test_val = eval(fun_derivada.replace('x', '(1)'))
                    def df(x):
                        return eval(fun_derivada)
                    print("✅ Derivada ingresada correctamente")
                    break
                except Exception as e:
                    print(f"⚠️  Error al evaluar la derivada: {e}")
                    print("Asegúrate de usar sintaxis Python válida\n")
            break
        else:
            print("⚠️  Opción inválida. Por favor ingresa 1 o 2.\n")
    # Graficar la función para análisis visual
    print("\n>>> Graficando función para análisis visual...")
    x_range = np.linspace(-10, 10, 1000)  # 1000 puntos para una gráfica suave
    try:
        # Evaluar la función en el rango para graficar
        y_range = [f(x) for x in x_range]
        # Crear la gráfica
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        # Gráfica de la función
        ax1.plot(x_range, y_range, 'b-', linewidth=2, label=f'f(x) = {fun}')
        ax1.grid(True, alpha=0.3)
        ax1.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
        ax1.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
        ax1.set_xlabel('x', fontsize=12)
        ax1.set_ylabel('f(x)', fontsize=12)
        ax1.set_title('Gráfica de la Función', fontsize=14, fontweight='bold')
        ax1.legend(fontsize=10)
        # Gráfica de la derivada
        if usar_derivada_numerica:
            y_derivada = [derivada_numerica(f, x) for x in x_range]
        else:
            y_derivada = [df(x) for x in x_range]
        ax2.plot(x_range, y_derivada, 'r-', linewidth=2, label="f'(x)")
        ax2.grid(True, alpha=0.3)
        ax2.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
        ax2.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
        ax2.set_xlabel('x', fontsize=12)
        ax2.set_ylabel("f'(x)", fontsize=12)
        ax2.set_title('Gráfica de la Derivada', fontsize=14, fontweight='bold')
        ax2.legend(fontsize=10)
        plt.tight_layout()
        print("✅ Gráfica generada. Cierra la ventana de la gráfica para continuar...\n")
        plt.show()
    except Exception as e:
        print(f"⚠️  Error al graficar: {e}\n")
    # Análisis de posibles raíces (ceros de la función)
    print("\n" + "="*70)
    print("🔍 ANÁLISIS DE POSIBLES RAÍCES")
    print("="*70)
    print("Buscando intervalos donde la función cambia de signo...\n")
    cambios_signo = []
    x_test = np.linspace(-10, 10, 200)
    for i in range(len(x_test)-1):
        try:
            f1 = f(x_test[i])
            f2 = f(x_test[i+1])
            if f1 * f2 < 0:  # Cambio de signo indica posible raíz
                punto_medio = (x_test[i] + x_test[i+1]) / 2
                cambios_signo.append(punto_medio)
        except:
            pass
    if cambios_signo:
        print(f"✅ Se encontraron {len(cambios_signo)} posibles raíces en el rango [-10, 10]:")
        for idx, x_sugerido in enumerate(cambios_signo[:5], 1):
            print(f"   {idx}. Valor sugerido para x0: {x_sugerido:.4f}")
        if len(cambios_signo) > 5:
            print(f"   ... y {len(cambios_signo)-5} más")
    else:
        print("⚠️  No se encontraron cambios de signo evidentes en el rango [-10, 10]")
        print("   Nota: Newton-Raphson puede encontrar raíces sin cambio de signo.")
    # Solicitar valor inicial x0
    print("\n" + "="*70)
    print("⚙️  PARÁMETROS DEL MÉTODO")
    print("="*70)
    # Sugerir valor inicial si se encontraron cambios de signo
    if cambios_signo:
        print(f"\n💡 Valor sugerido para x0: {cambios_signo[0]:.4f}")
        usar_sugerido = input(f"¿Usar este valor? (s/n) [s]: ").strip().lower()
        if usar_sugerido in ['', 's', 'si', 'sí', 'yes', 'y']:
            x0 = cambios_signo[0]
            print(f"✅ Usando x0 = {x0:.4f}")
        else:
            while True:
                try:
                    x0 = float(input("Ingresa el valor inicial x0: ").strip())
                    break
                except ValueError:
                    print("⚠️  Error: Ingresa un número válido.\n")
    else:
        while True:
            try:
                x0 = float(input("\nIngresa el valor inicial x0: ").strip())
                break
            except ValueError:
                print("⚠️  Error: Ingresa un número válido.\n")
    # Solicitar tolerancia
    while True:
        try:
            tolerancia_input = input("\nIngresa la tolerancia (ejemplo: 0.0001) [0.0001]: ").strip()
            if tolerancia_input == '':
                tolerancia = 0.0001
            else:
                tolerancia = float(tolerancia_input)
                if tolerancia <= 0:
                    print("⚠️  Error: La tolerancia debe ser positiva.\n")
                    continue
            print(f"✅ Tolerancia establecida: {tolerancia}")
            break
        except ValueError:
            print("⚠️  Error: Ingresa un número válido.\n")
    # Solicitar máximo de iteraciones
    while True:
        try:
            max_iter_input = input("\nIngresa el número máximo de iteraciones [100]: ").strip()
            if max_iter_input == '':
                max_iteraciones = 100
            else:
                max_iteraciones = int(max_iter_input)
                if max_iteraciones <= 0:
                    print("⚠️  Error: El número de iteraciones debe ser positivo.\n")
                    continue
            print(f"✅ Máximo de iteraciones: {max_iteraciones}")
            break
        except ValueError:
            print("⚠️  Error: Ingresa un número entero válido.\n")
    # Ejecutar el método de Newton-Raphson
    raiz, iteraciones, convergio, historial = newton_raphson(
        f, x0, tolerancia, max_iteraciones, usar_derivada_numerica, df
    )
    # Mostrar resultados finales
    print("\n" + "="*70)
    print("📈 RESULTADO FINAL")
    print("="*70)
    if convergio:
        print(f"\n✅ Raíz encontrada: x = {raiz:.10f}")
        print(f"   f({raiz:.10f}) = {f(raiz):.2e}")
        print(f"   Iteraciones realizadas: {iteraciones}")
        print(f"   Valor inicial: x0 = {x0}")
        print(f"   Tolerancia: {tolerancia}")
    else:
        print(f"\n⚠️  No se alcanzó convergencia")
        print(f"   Última aproximación: x = {raiz:.10f}")
        print(f"   f({raiz:.10f}) = {f(raiz):.2e}")
        print(f"   Iteraciones realizadas: {iteraciones}")
    # Graficar las iteraciones
    if len(historial) > 0:
        print("\n>>> Generando gráfica de convergencia...")
        try:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
            # Gráfica 1: Función con las iteraciones
            x_plot = np.linspace(min([h[1] for h in historial]) - 1, 
                                max([h[1] for h in historial]) + 1, 500)
            y_plot = [f(x) for x in x_plot]
            ax1.plot(x_plot, y_plot, 'b-', linewidth=2, label=f'f(x) = {fun}')
            ax1.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
            ax1.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
            # Marcar las iteraciones
            for i, (iter_num, x_val, f_val, _) in enumerate(historial):
                if i == 0:
                    ax1.plot(x_val, f_val, 'go', markersize=10, label='Inicio', zorder=5)
                elif i == len(historial) - 1:
                    ax1.plot(x_val, f_val, 'ro', markersize=10, label='Final', zorder=5)
                else:
                    ax1.plot(x_val, f_val, 'yo', markersize=6, alpha=0.6, zorder=4)
                # Dibujar tangente para algunas iteraciones
                if i < len(historial) - 1 and i < 5:
                    if usar_derivada_numerica:
                        pendiente = derivada_numerica(f, x_val)
                    else:
                        pendiente = df(x_val)
                    x_tang = np.array([x_val - 0.5, x_val + 0.5])
                    y_tang = f_val + pendiente * (x_tang - x_val)
                    ax1.plot(x_tang, y_tang, 'r--', alpha=0.3, linewidth=1)
            ax1.grid(True, alpha=0.3)
            ax1.set_xlabel('x', fontsize=12)
            ax1.set_ylabel('f(x)', fontsize=12)
            ax1.set_title('Iteraciones del Método Newton-Raphson', fontsize=14, fontweight='bold')
            ax1.legend(fontsize=10)
            # Gráfica 2: Convergencia del error
            iteraciones_plot = [h[0] for h in historial]
            errores_plot = [h[3] for h in historial]
            ax2.semilogy(iteraciones_plot, errores_plot, 'b-o', linewidth=2, markersize=6)
            ax2.axhline(y=tolerancia, color='r', linestyle='--', linewidth=2, label=f'Tolerancia = {tolerancia}')
            ax2.grid(True, alpha=0.3)
            ax2.set_xlabel('Iteración', fontsize=12)
            ax2.set_ylabel('|f(x)|  (escala logarítmica)', fontsize=12)
            ax2.set_title('Convergencia del Error', fontsize=14, fontweight='bold')
            ax2.legend(fontsize=10)
            plt.tight_layout()
            print("✅ Gráfica de convergencia generada. Cierra la ventana para continuar...")
            plt.show()
        except Exception as e:
            print(f"⚠️  Error al graficar convergencia: {e}")
    # Preguntar si desea continuar
    if not preguntar_continuar():
        programa_activo = False
        print("\n👋 ¡Gracias por usar el programa! Hasta pronto.\n")
