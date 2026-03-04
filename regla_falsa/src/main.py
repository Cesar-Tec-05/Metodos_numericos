# ================================================================
# TITULO: Método de la Regla Falsa - Cálculo de Raíces
# AUTOR: Cesar de Jesus Becerra Vera
# FECHA: 4 de Marzo de 2026
# VERSION: 1.0
# ARCHIVO: main.py
# CENTRO UNIVERSITARIO DE LOS ALTOS / UNIVERSIDAD DE GUADALAJARA
# INGENIERIA EN COMPUTACION / 4TO SEMESTRE
# PROFESOR: JUAN MANUEL
# DESCRIPCIÓN: Programa interactivo que implementa el método de la regla falsa para encontrar raíces de funciones.
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
    print("           MÉTODO DE LA REGLA FALSA - CÁLCULO DE RAÍCES")
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
    # Si eligió calcular, ejecutar el método de regla falsa
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
        plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
        plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.title('Gráfica de la Función', fontsize=14, fontweight='bold')
        plt.legend(fontsize=10)
        plt.tight_layout()
        print("✅ Gráfica generada. Cierra la ventana de la gráfica para continuar...\n")
        plt.show()
    except Exception as e:
        print(f"⚠️  Error al graficar: {e}\n")

    # Análisis de posibles raíces
    print("="*70)
    print("🔍 ANÁLISIS DE POSIBLES RAÍCES")
    print("="*70)
    print("Buscando intervalos donde la función cambia de signo...\n")
    
    # Analizar en un rango amplio
    cambios_signo = []
    x_test = np.linspace(-10, 10, 200)
    for i in range(len(x_test)-1):
        try:
            f1 = f(x_test[i])
            f2 = f(x_test[i+1])
            if f1 * f2 < 0:  # Cambio de signo
                cambios_signo.append((x_test[i], x_test[i+1]))
        except:
            pass
    
    if cambios_signo:
        print(f"✅ Se encontraron {len(cambios_signo)} posibles raíces en el rango [-10, 10]:")
        for idx, (a_temp, b_temp) in enumerate(cambios_signo[:5], 1):
            print(f"   {idx}. Intervalo: [{a_temp:.2f}, {b_temp:.2f}]")
        if len(cambios_signo) > 5:
            print(f"   ... y {len(cambios_signo)-5} más")
    else:
        print("⚠️  No se encontraron cambios de signo evidentes en el rango [-10, 10]")
        print("   Esto no significa que no haya raíces, puede que necesites un rango más amplio.\n")

    # Solicitar límite inferior con validación
    print("\n" + "="*70)
    print("📊 CONFIGURACIÓN DEL INTERVALO")
    print("="*70)
    
    # Ofrecer intervalos sugeridos si se encontraron cambios de signo
    if cambios_signo:
        print("\n💡 INTERVALOS SUGERIDOS (con cambio de signo):")
        for idx, (a_temp, b_temp) in enumerate(cambios_signo[:3], 1):
            print(f"   {idx}. [{a_temp:.4f}, {b_temp:.4f}]")
        print("   0. Ingresar intervalo manualmente\n")
        
        while True:
            seleccion = input("Selecciona un intervalo sugerido (0-{}) o Enter para el primero: ".format(min(3, len(cambios_signo)))).strip()
            if seleccion == "":
                a, b = cambios_signo[0]
                print(f"✅ Usando intervalo sugerido: [{a:.4f}, {b:.4f}]")
                break
            try:
                idx_sel = int(seleccion)
                if idx_sel == 0:
                    # Ingresar manualmente
                    while True:
                        try:
                            a = float(input("Ingresa el límite inferior del intervalo (xl): ").strip())
                            break
                        except ValueError:
                            print("⚠️  Error: Ingresa un número válido.\n")
                    
                    while True:
                        try:
                            b = float(input("Ingresa el límite superior del intervalo (xu): ").strip())
                            if b <= a:
                                print("⚠️  Error: El límite superior debe ser mayor que el inferior.\n")
                                continue
                            break
                        except ValueError:
                            print("⚠️  Error: Ingresa un número válido.\n")
                    break
                elif 1 <= idx_sel <= min(3, len(cambios_signo)):
                    a, b = cambios_signo[idx_sel - 1]
                    print(f"✅ Usando intervalo sugerido: [{a:.4f}, {b:.4f}]")
                    break
                else:
                    print(f"⚠️  Error: Selecciona un número entre 0 y {min(3, len(cambios_signo))}.\n")
            except ValueError:
                print("⚠️  Error: Ingresa un número válido.\n")
    else:
        # No hay cambios de signo, pedir entrada manual
        while True:
            try:
                a = float(input("Ingresa el límite inferior del intervalo (xl): ").strip())
                break
            except ValueError:
                print("⚠️  Error: Ingresa un número válido.\n")

        while True:
            try:
                b = float(input("Ingresa el límite superior del intervalo (xu): ").strip())
                if b <= a:
                    print("⚠️  Error: El límite superior debe ser mayor que el inferior.\n")
                    continue
                break
            except ValueError:
                print("⚠️  Error: Ingresa un número válido.\n")

    # Verificar que haya cambio de signo en el intervalo
    try:
        fa = f(a)
        fb = f(b)
        if fa * fb >= 0:
            print(f"\n⚠️  ADVERTENCIA: No hay cambio de signo en el intervalo [{a}, {b}]")
            print(f"   f({a}) = {fa:.6f}")
            print(f"   f({b}) = {fb:.6f}")
            print("   El método puede no converger. ¿Deseas continuar de todas formas?")
            while True:
                resp = input("   (s/n): ").strip().lower()
                if resp in ['n', 'no']:
                    continuar = preguntar_continuar()
                    if continuar:
                        continue
                    else:
                        programa_activo = False
                        break
                elif resp in ['s', 'si', 'sí', 'yes', 'y']:
                    break
                else:
                    print("⚠️  Respuesta inválida. Ingresa 's' o 'n'.")
            if not programa_activo:
                break
    except Exception as e:
        print(f"\n⚠️  Error al evaluar la función en los límites: {e}")
        continuar = preguntar_continuar()
        if continuar:
            continue
        else:
            programa_activo = False
            break

    # Solicitar tolerancia con validación
    print("\n" + "="*70)
    print("⚙️  CONFIGURACIÓN DE PARÁMETROS")
    print("="*70)
    tolerancia_sugerida = 0.00001
    print(f"Tolerancia sugerida: {tolerancia_sugerida}")
    while True:
        tol_input = input(f"Ingresa la tolerancia de error (Enter para usar {tolerancia_sugerida}): ").strip()
        if tol_input == "":
            tol = tolerancia_sugerida
            break
        try:
            tol = float(tol_input)
            if tol <= 0:
                print("⚠️  Error: La tolerancia debe ser mayor que 0.\n")
                continue
            break
        except ValueError:
            print("⚠️  Error: Ingresa un número válido.\n")

    # Solicitar número máximo de iteraciones
    max_iter_sugerido = 100
    print(f"\nIteraciones máximas sugeridas: {max_iter_sugerido}")
    while True:
        max_input = input(f"Ingresa el número máximo de iteraciones (Enter para usar {max_iter_sugerido}): ").strip()
        if max_input == "":
            max_iter = max_iter_sugerido
            break
        try:
            max_iter = int(max_input)
            if max_iter <= 0:
                print("⚠️  Error: El número de iteraciones debe ser mayor que 0.\n")
                continue
            break
        except ValueError:
            print("⚠️  Error: Ingresa un número entero válido.\n")

    # Ejecutar el método de la regla falsa
    print("\n" + "="*70)
    print("🔄 EJECUTANDO MÉTODO DE LA REGLA FALSA")
    print("="*70)
    
    # Inicializar variables
    iteraciones = []
    xl = a
    xu = b
    xr_anterior = None
    xr = None  # Inicializar para evitar NameError
    fxr = None  # Inicializar para evitar NameError
    convergio = False

    # Encabezado de la tabla
    print("\n{:<5} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
        "Iter", "xl", "xu", "xr", "f(xl)", "f(xu)", "f(xr)"))
    print("-"*85)

    # Iteraciones del método
    for i in range(max_iter):
        try:
            # Evaluar función en los extremos
            fxl = f(xl)
            fxu = f(xu)
            
            # Verificar división por cero
            if abs(fxu - fxl) < 1e-15:
                print(f"\n⚠️  Error: División por cero (f(xu) - f(xl) ≈ 0)")
                print(f"   Los valores de la función son muy similares en ambos extremos.")
                print(f"   f({xl:.6f}) = {fxl:.6e}")
                print(f"   f({xu:.6f}) = {fxu:.6e}")
                break
            
            # Fórmula de la regla falsa (interpolación lineal)
            xr = xl - (fxl * (xu - xl)) / (fxu - fxl)
            fxr = f(xr)
            
            # Guardar datos de la iteración
            iteraciones.append({
                'iter': i + 1,
                'xl': xl,
                'xu': xu,
                'xr': xr,
                'fxl': fxl,
                'fxu': fxu,
                'fxr': fxr
            })
            
            # Imprimir iteración
            print("{:<5} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format(
                i + 1, xl, xu, xr, fxl, fxu, fxr))
            
            # Verificar convergencia
            if abs(fxr) < tol:
                convergio = True
                print("\n✅ ¡Convergencia alcanzada!")
                break
            
            # Verificar error relativo si no es la primera iteración
            if xr_anterior is not None and xr != 0:
                error_relativo = abs((xr - xr_anterior) / xr) * 100
                if error_relativo < tol * 100:
                    convergio = True
                    print("\n✅ ¡Convergencia alcanzada por error relativo!")
                    break
            
            # Actualizar intervalo según el signo
            if fxl * fxr < 0:
                xu = xr
            else:
                xl = xr
            
            xr_anterior = xr
            
        except Exception as e:
            print(f"\n⚠️  Error durante la iteración {i+1}: {e}")
            break

    # Resultados finales
    print("\n" + "="*70)
    print("📊 RESULTADOS FINALES")
    print("="*70)
    
    if convergio and xr is not None:
        print(f"✅ RAÍZ ENCONTRADA: x = {xr:.8f}")
        print(f"   f({xr:.8f}) = {fxr:.8e}")
        print(f"   Iteraciones realizadas: {i + 1}")
        print(f"   Tolerancia utilizada: {tol}")
        
        # Gráfica final con la raíz
        print("\n>>> Generando gráfica con la raíz encontrada...")
        try:
            # Rango alrededor de la raíz
            rango_grafica = max(abs(xr - xl), abs(xr - xu)) * 2
            if rango_grafica < 1:
                rango_grafica = 2
            x_plot = np.linspace(xr - rango_grafica, xr + rango_grafica, 500)
            y_plot = [f(x) for x in x_plot]
            
            plt.figure(figsize=(10, 6))
            plt.plot(x_plot, y_plot, 'b-', linewidth=2, label=f'f(x) = {fun}')
            plt.plot(xr, fxr, 'ro', markersize=10, label=f'Raíz: x={xr:.6f}')
            plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
            plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
            plt.axvline(x=xr, color='r', linestyle='--', linewidth=1, alpha=0.5)
            plt.grid(True, alpha=0.3)
            plt.xlabel('x', fontsize=12)
            plt.ylabel('f(x)', fontsize=12)
            plt.title(f'Raíz encontrada por Método de Regla Falsa: x = {xr:.6f}', 
                    fontsize=14, fontweight='bold')
            plt.legend(fontsize=10)
            plt.tight_layout()
            print("✅ Gráfica generada. Cierra la ventana para continuar...\n")
            plt.show()
        except Exception as e:
            print(f"⚠️  Error al generar gráfica final: {e}\n")
    else:
        print(f"⚠️  NO SE ALCANZÓ LA CONVERGENCIA")
        if xr is not None:
            print(f"   Última aproximación: x = {xr:.8f}")
            print(f"   f({xr:.8f}) = {fxr:.8e}")
            print(f"   Iteraciones realizadas: {max_iter if not convergio else i + 1}")
        else:
            print(f"   No se pudo calcular ninguna aproximación.")
            print(f"   Verifica que el intervalo sea adecuado.")
        print(f"   Considera aumentar el número de iteraciones o cambiar el intervalo.\n")

    # Preguntar si desea continuar
    continuar = preguntar_continuar()
    if not continuar:
        programa_activo = False
        print("\n👋 ¡Gracias por usar el programa! Hasta pronto.\n")
