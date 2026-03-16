# ================================================================
# TITULO: Método de la Secante - Cálculo de Raíces
# AUTOR: Cesar de Jesus Becerra Vera
# FECHA: 16 de Marzo de 2026
# VERSION: 1.0
# ARCHIVO: main.py
# CENTRO UNIVERSITARIO DE LOS ALTOS / UNIVERSIDAD DE GUADALAJARA
# INGENIERIA EN COMPUTACION / 4TO SEMESTRE
# PROFESOR: JUAN MANUEL
# DESCRIPCIÓN: Programa interactivo que implementa el método de la secante para encontrar raíces de funciones.
# ================================================================

import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def mostrar_menu():
	"""
	Función para mostrar el menú principal y obtener la opción del usuario.
	Retorna: 'calcular' para iniciar o 'salir' para terminar el programa.
	"""
	print("\n" + "=" * 70)
	print("              MÉTODO DE LA SECANTE - CÁLCULO DE RAÍCES")
	print("=" * 70)
	print("\n📋 MENÚ PRINCIPAL:")
	print("   1. Calcular raíz de una función")
	print("   2. Salir del programa")
	print("-" * 70)
	while True:
		opcion = input("Selecciona una opción (1 o 2): ").strip()
		if opcion == '1':
			return 'calcular'
		if opcion == '2':
			return 'salir'
		print("⚠️  Opción inválida. Por favor ingresa 1 o 2.\n")

def preguntar_continuar():
	"""
	Función para preguntar si el usuario desea continuar con otro cálculo.
	Retorna: True si desea continuar, False si desea salir.
	"""
	print("\n" + "=" * 70)
	while True:
		respuesta = input("¿Deseas realizar otro cálculo? (s/n): ").strip().lower()
		if respuesta in ['s', 'si', 'sí', 'yes', 'y']:
			return True
		if respuesta in ['n', 'no']:
			return False
		print("⚠️  Respuesta inválida. Por favor ingresa 's' para sí o 'n' para no.\n")

def evaluar_expresion(expresion, x):
	contexto = {
		'x': x,
		'math': math,
		'np': np,
		'numpy': np,
		'abs': abs
	}
	return eval(expresion, {'__builtins__': {}}, contexto)

def metodo_secante(f, x0, x1, tolerancia, max_iteraciones):
	"""
	Implementación del método de la secante.
	Retorna: (x_aprox, convergio, historial, motivo)
	"""
	historial = []
	x_anterior = x0
	x_actual = x1
	convergio = False
	motivo = ""
	print("\n" + "=" * 70)
	print("🔄 EJECUTANDO MÉTODO DE LA SECANTE")
	print("=" * 70)
	print("\n{:<5} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
		"Iter", "x(i-1)", "x(i)", "x(i+1)", "f(x(i+1))", "ErrorAbs", "ErrorRel%"
	))
	print("-" * 90)
	for iteracion in range(1, max_iteraciones + 1):
		try:
			fx_anterior = f(x_anterior)
			fx_actual = f(x_actual)
		except Exception as error:
			motivo = f"⚠️  Error al evaluar la función: {error}"
			break
		denominador = fx_actual - fx_anterior
		if abs(denominador) < 1e-15:
			motivo = "⚠️  División por cero: f(x(i)) - f(x(i-1)) es muy pequeño."
			break
		x_siguiente = x_actual - (fx_actual * (x_actual - x_anterior)) / denominador
		try:
			fx_siguiente = f(x_siguiente)
		except Exception as error:
			motivo = f"⚠️  Error al evaluar f(x(i+1)): {error}"
			break
		error_absoluto = abs(x_siguiente - x_actual)
		error_relativo = (error_absoluto / abs(x_siguiente)) * 100 if x_siguiente != 0 else float('inf')
		historial.append({
			'iteracion': iteracion,
			'x_anterior': x_anterior,
			'x_actual': x_actual,
			'x_siguiente': x_siguiente,
			'fx_siguiente': fx_siguiente,
			'error_absoluto': error_absoluto,
			'error_relativo': error_relativo
		})
		print("{:<5} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6e} {:<12.6e} {:<12.6f}".format(
			iteracion,
			x_anterior,
			x_actual,
			x_siguiente,
			fx_siguiente,
			error_absoluto,
			error_relativo
		))
		if abs(fx_siguiente) < tolerancia:
			convergio = True
			motivo = "✅ Convergencia alcanzada por |f(x)| < tolerancia."
			x_actual = x_siguiente
			break
		if error_absoluto < tolerancia:
			convergio = True
			motivo = "✅ Convergencia alcanzada por error absoluto."
			x_actual = x_siguiente
			break
		x_anterior, x_actual = x_actual, x_siguiente
	if not convergio and not motivo:
		motivo = f"⚠️  No se alcanzó la convergencia en {max_iteraciones} iteraciones."
	return x_actual, convergio, historial, motivo

def graficar_funcion(f, expresion):
	x_rango = np.linspace(-10, 10, 1000)
	y_rango = []
	for valor in x_rango:
		try:
			y_rango.append(f(valor))
		except Exception:
			y_rango.append(np.nan)
	try:
		plt.figure(figsize=(10, 6))
		plt.plot(x_rango, y_rango, 'b-', linewidth=2, label=f'f(x) = {expresion}')
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
	except Exception as error:
		print(f"⚠️  Error al graficar: {error}\n")

def buscar_cambios_signo(f):
	cambios_signo = []
	x_prueba = np.linspace(-10, 10, 200)
	for indice in range(len(x_prueba) - 1):
		try:
			f1 = f(x_prueba[indice])
			f2 = f(x_prueba[indice + 1])
			if f1 * f2 < 0:
				cambios_signo.append((x_prueba[indice], x_prueba[indice + 1]))
		except Exception:
			continue
	return cambios_signo

def solicitar_puntos_iniciales(cambios_signo):
	print("\n" + "=" * 70)
	print("⚙️  PARÁMETROS DEL MÉTODO")
	print("=" * 70)
	if cambios_signo:
		print("\n💡 VALORES INICIALES SUGERIDOS:")
		for indice, (x_izquierda, x_derecha) in enumerate(cambios_signo[:3], 1):
			print(f"   {indice}. x0 = {x_izquierda:.4f}, x1 = {x_derecha:.4f}")
		print("   0. Ingresar valores manualmente\n")
		while True:
			seleccion = input(
				f"Selecciona una opción (0-{min(3, len(cambios_signo))}) o Enter para la primera: "
			).strip()
			if seleccion == "":
				x0, x1 = cambios_signo[0]
				print(f"✅ Usando sugerencia: x0 = {x0:.6f}, x1 = {x1:.6f}")
				break
			try:
				opcion = int(seleccion)
				if opcion == 0:
					x0, x1 = solicitar_valores_manuales()
					break
				if 1 <= opcion <= min(3, len(cambios_signo)):
					x0, x1 = cambios_signo[opcion - 1]
					print(f"✅ Usando sugerencia: x0 = {x0:.6f}, x1 = {x1:.6f}")
					break
				print(f"⚠️  Error: selecciona entre 0 y {min(3, len(cambios_signo))}.\n")
			except ValueError:
				print("⚠️  Error: ingresa un número válido.\n")
	else:
		print("\nNo se detectaron cambios de signo claros en [-10, 10].")
		print("Ingresa manualmente dos valores iniciales distintos.\n")
		x0, x1 = solicitar_valores_manuales()
	return x0, x1

def solicitar_valores_manuales():
	while True:
		try:
			x0 = float(input("Ingresa x0: ").strip())
			break
		except ValueError:
			print("⚠️  Error: ingresa un número válido.\n")
	while True:
		try:
			x1 = float(input("Ingresa x1: ").strip())
			if x1 == x0:
				print("⚠️  Error: x1 debe ser diferente de x0.\n")
				continue
			break
		except ValueError:
			print("⚠️  Error: ingresa un número válido.\n")
	return x0, x1

def solicitar_tolerancia():
	tolerancia_sugerida = 0.00001
	print(f"\nTolerancia sugerida: {tolerancia_sugerida}")
	while True:
		entrada = input(f"Ingresa la tolerancia (Enter para usar {tolerancia_sugerida}): ").strip()
		if entrada == "":
			return tolerancia_sugerida
		try:
			tolerancia = float(entrada)
			if tolerancia <= 0:
				print("⚠️  Error: la tolerancia debe ser mayor que 0.\n")
				continue
			return tolerancia
		except ValueError:
			print("⚠️  Error: ingresa un número válido.\n")

def solicitar_max_iteraciones():
	max_sugerido = 100
	print(f"\nIteraciones máximas sugeridas: {max_sugerido}")
	while True:
		entrada = input(f"Ingresa el número máximo de iteraciones (Enter para usar {max_sugerido}): ").strip()
		if entrada == "":
			return max_sugerido
		try:
			max_iteraciones = int(entrada)
			if max_iteraciones <= 0:
				print("⚠️  Error: el número debe ser mayor que 0.\n")
				continue
			return max_iteraciones
		except ValueError:
			print("⚠️  Error: ingresa un número entero válido.\n")

def graficar_resultado(f, expresion, x0, x1, historial, x_aprox):
	if not historial:
		return
	rango = max(abs(x_aprox - x0), abs(x_aprox - x1), 2)
	x_plot = np.linspace(x_aprox - rango, x_aprox + rango, 600)
	y_plot = []
	for valor in x_plot:
		try:
			y_plot.append(f(valor))
		except Exception:
			y_plot.append(np.nan)
	aproximaciones = [x0, x1] + [registro['x_siguiente'] for registro in historial]
	y_aprox = []
	for valor in aproximaciones:
		try:
			y_aprox.append(f(valor))
		except Exception:
			y_aprox.append(np.nan)
	try:
		plt.figure(figsize=(10, 6))
		plt.plot(x_plot, y_plot, 'b-', linewidth=2, label=f'f(x) = {expresion}')
		plt.scatter(aproximaciones, y_aprox, color='orange', s=35, label='Aproximaciones')
		plt.plot(x_aprox, f(x_aprox), 'ro', markersize=9, label=f'Raíz aprox: {x_aprox:.6f}')
		plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
		plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
		plt.grid(True, alpha=0.3)
		plt.xlabel('x', fontsize=12)
		plt.ylabel('f(x)', fontsize=12)
		plt.title('Método de la Secante - Aproximación de la raíz', fontsize=14, fontweight='bold')
		plt.legend(fontsize=10)
		plt.tight_layout()
		print("✅ Gráfica final generada. Cierra la ventana para continuar...\n")
		plt.show()
	except Exception as error:
		print(f"⚠️  Error al generar gráfica final: {error}\n")

programa_activo = True
while programa_activo:
	opcion = mostrar_menu()
	if opcion == 'salir':
		print("\n👋 ¡Gracias por usar el programa! Hasta pronto.\n")
		break
	print("\n" + "=" * 70)
	print("📝 CONFIGURACIÓN DE LA FUNCIÓN")
	print("=" * 70)
	while True:
		expresion = input("Ingresa la función f(x) en términos de x (ejemplo: 'x**3 - x - 2'): ").strip()
		if not expresion:
			print("⚠️  Error: debes ingresar una función.\n")
			continue
		try:
			evaluar_expresion(expresion, 0)
			break
		except Exception as error:
			print(f"⚠️  Error al evaluar la función: {error}")
			print("Asegúrate de usar sintaxis Python válida (ejemplo: x**2 - 4 o math.sin(x))\n")
	def f(x):
		return evaluar_expresion(expresion, x)
	print("\n>>> Graficando función para análisis visual...")
	graficar_funcion(f, expresion)
	print("=" * 70)
	print("🔍 ANÁLISIS DE POSIBLES RAÍCES")
	print("=" * 70)
	print("Buscando intervalos con cambio de signo en [-10, 10]...\n")
	cambios_signo = buscar_cambios_signo(f)
	if cambios_signo:
		print(f"✅ Se encontraron {len(cambios_signo)} posibles raíces:")
		for indice, (x_izquierda, x_derecha) in enumerate(cambios_signo[:5], 1):
			print(f"   {indice}. Intervalo: [{x_izquierda:.4f}, {x_derecha:.4f}]")
		if len(cambios_signo) > 5:
			print(f"   ... y {len(cambios_signo) - 5} más")
	else:
		print("⚠️  No se detectaron cambios de signo evidentes en el rango analizado.")
	x0, x1 = solicitar_puntos_iniciales(cambios_signo)
	tolerancia = solicitar_tolerancia()
	max_iteraciones = solicitar_max_iteraciones()
	x_aproximada, convergio, historial, motivo = metodo_secante(f, x0, x1, tolerancia, max_iteraciones)
	print("\n" + "=" * 70)
	print("📊 RESULTADOS FINALES")
	print("=" * 70)
	if historial:
		ultima = historial[-1]
		valor_fx = ultima['fx_siguiente']
		iteraciones = ultima['iteracion']
	else:
		valor_fx = f(x_aproximada)
		iteraciones = 0
	if convergio:
		print(f"✅ RAÍZ ENCONTRADA: x = {x_aproximada:.10f}")
		print(f"   f(x) = {valor_fx:.10e}")
		print(f"   Iteraciones realizadas: {iteraciones}")
		print(f"   Tolerancia utilizada: {tolerancia}")
	else:
		print("⚠️  NO SE ALCANZÓ LA CONVERGENCIA")
		print(f"   Última aproximación: x = {x_aproximada:.10f}")
		print(f"   f(x) = {valor_fx:.10e}")
		print(f"   Iteraciones realizadas: {iteraciones}")
		print(f"   Tolerancia utilizada: {tolerancia}")
	print(motivo)
	print("\n>>> Generando gráfica final...")
	graficar_resultado(f, expresion, x0, x1, historial, x_aproximada)
	if not preguntar_continuar():
		programa_activo = False
		print("\n👋 ¡Gracias por usar el programa! Hasta pronto.\n")
