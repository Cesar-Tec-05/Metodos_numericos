# ================================================================
# TITULO: Método del Punto Fijo - Cálculo de Raíces
# AUTOR: Cesar de Jesus Becerra Vera
# FECHA: 15 de Abril de 2026
# VERSION: 1.0
# ARCHIVO: main.py
# CENTRO UNIVERSITARIO DE LOS ALTOS / UNIVERSIDAD DE GUADALAJARA
# INGENIERIA EN COMPUTACION / 4TO SEMESTRE
# PROFESOR: JUAN MANUEL
# DESCRIPCIÓN: Programa interactivo que implementa el método del punto fijo para encontrar raíces de funciones.
# ================================================================

# Importación de librerías necesarias
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
	print("              MÉTODO DEL PUNTO FIJO - CÁLCULO DE RAÍCES")
	print("=" * 70)
	print("\n📋 MENÚ PRINCIPAL:")
	print("   1. Calcular punto fijo de una función")
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


def mostrar_recomendaciones_usuario():
	print("\n" + "=" * 70)
	print("💡 RECOMENDACIONES PARA INGRESAR LOS DATOS")
	print("=" * 70)
	print("1. Escribe una función despejada como x = g(x), no la ecuación completa.")
	print("2. Usa 'math.' para funciones como coseno, seno, exp o log.")
	print("3. El valor inicial x0 debe estar cerca del punto fijo que esperas encontrar.")
	print("4. Si usas g(x) = (x + a/x)/2, NO uses x0 = 0.")
	print("5. La tolerancia recomendada es 0.00001 si no sabes cuál usar.")
	print("6. Usa un máximo de 100 iteraciones para empezar.")
	print("7. Si no converge, prueba otro valor inicial x0 o cambia la función g(x).")


def expresion_valida_para_inicio(expresion):
	"""
	Valida que la expresión pueda evaluarse al menos en un punto simple.
	No se usa x=0 para evitar falsos negativos en funciones como (x + 5/x)/2.
	"""
	puntos_prueba = [1.0, 0.5, -1.0, 2.0]
	for punto in puntos_prueba:
		try:
			evaluar_expresion(expresion, punto)
			return True
		except Exception:
			continue
	return False

def buscar_cambios_signo(f):
	"""
	Busca intervalos donde g(x) - x cambia de signo para sugerir valores iniciales.
	"""
	cambios_signo = []
	x_prueba = np.linspace(-10, 10, 400)
	for indice in range(len(x_prueba) - 1):
		try:
			h1 = f(x_prueba[indice]) - x_prueba[indice]
			h2 = f(x_prueba[indice + 1]) - x_prueba[indice + 1]
			if h1 * h2 < 0:
				cambios_signo.append((x_prueba[indice], x_prueba[indice + 1]))
		except Exception:
			continue
	return cambios_signo


def solicitar_valor_manual():
	while True:
		try:
			return float(input("Ingresa el valor inicial x0: ").strip())
		except ValueError:
			print("⚠️  Error: ingresa un número válido.\n")


def validar_valor_inicial(g, x0):
	"""
	Verifica que g(x0) pueda evaluarse antes de iniciar el método.
	"""
	try:
		g(x0)
		return True
	except Exception as error:
		print(f"⚠️  El valor inicial x0 = {x0} no es válido para esta función: {error}")
		print("   Prueba con otro x0 (ejemplo: para (x + 5/x)/2 usa x0 distinto de 0).\n")
		return False


def solicitar_valor_inicial(cambios_signo):
	print("\n" + "=" * 70)
	print("⚙️  PARÁMETROS DEL MÉTODO")
	print("=" * 70)
	if cambios_signo:
		print("\n💡 VALORES INICIALES SUGERIDOS:")
		for indice, (x_izquierda, x_derecha) in enumerate(cambios_signo[:3], 1):
			print(f"   {indice}. x0 ≈ {(x_izquierda + x_derecha) / 2:.6f}  (intervalo [{x_izquierda:.4f}, {x_derecha:.4f}])")
		print("   0. Ingresar valor manualmente\n")
		while True:
			seleccion = input(
				f"Selecciona una opción (0-{min(3, len(cambios_signo))}) o Enter para la primera: "
			).strip()
			if seleccion == "":
				x0 = (cambios_signo[0][0] + cambios_signo[0][1]) / 2
				print(f"✅ Usando sugerencia: x0 = {x0:.6f}")
				break
			try:
				opcion = int(seleccion)
				if opcion == 0:
					x0 = solicitar_valor_manual()
					break
				if 1 <= opcion <= min(3, len(cambios_signo)):
					intervalo = cambios_signo[opcion - 1]
					x0 = (intervalo[0] + intervalo[1]) / 2
					print(f"✅ Usando sugerencia: x0 = {x0:.6f}")
					break
				print(f"⚠️  Error: selecciona entre 0 y {min(3, len(cambios_signo))}.\n")
			except ValueError:
				print("⚠️  Error: ingresa un número válido.\n")
	else:
		print("\nNo se detectaron cambios de signo claros para g(x) - x en [-10, 10].")
		print("Ingresa manualmente un valor inicial para iniciar la iteración.\n")
		x0 = solicitar_valor_manual()
	return x0


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


def metodo_punto_fijo(g, x0, tolerancia, max_iteraciones):
	"""
	Implementación del método del punto fijo.
	Retorna: (x_aprox, convergio, historial, motivo)
	"""
	historial = []
	x_actual = x0
	convergio = False
	motivo = ""
	print("\n" + "=" * 70)
	print("🔄 EJECUTANDO MÉTODO DEL PUNTO FIJO")
	print("=" * 70)
	print("\n{:<5} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
		"Iter", "x(n)", "g(x(n))", "ErrorAbs", "ErrorRel%", "|g(x)-x|"
	))
	print("-" * 80)
	for iteracion in range(1, max_iteraciones + 1):
		try:
			x_siguiente = g(x_actual)
		except Exception as error:
			motivo = f"⚠️  Error al evaluar la función: {error}"
			break
		error_absoluto = abs(x_siguiente - x_actual)
		error_relativo = (error_absoluto / abs(x_siguiente)) * 100 if x_siguiente != 0 else float('inf')
		try:
			residuo = abs(g(x_siguiente) - x_siguiente)
		except Exception as error:
			motivo = f"⚠️  Error al evaluar la función en la siguiente iteración: {error}"
			break
		historial.append({
			'iteracion': iteracion,
			'x_actual': x_actual,
			'x_siguiente': x_siguiente,
			'error_absoluto': error_absoluto,
			'error_relativo': error_relativo,
			'residuo': residuo
		})
		print("{:<5} {:<12.6f} {:<12.6f} {:<12.6e} {:<12.6f} {:<12.6e}".format(
			iteracion,
			x_actual,
			x_siguiente,
			error_absoluto,
			error_relativo,
			residuo
		))
		if error_absoluto < tolerancia or residuo < tolerancia:
			convergio = True
			motivo = "✅ Convergencia alcanzada por tolerancia en la diferencia sucesiva o el residuo."
			x_actual = x_siguiente
			break
		x_actual = x_siguiente
	if not convergio and not motivo:
		motivo = f"⚠️  No se alcanzó la convergencia en {max_iteraciones} iteraciones."
	return x_actual, convergio, historial, motivo


def graficar_funcion(g, expresion):
	x_rango = np.linspace(-10, 10, 1000)
	y_rango = []
	for valor in x_rango:
		try:
			y_rango.append(g(valor))
		except Exception:
			y_rango.append(np.nan)
	try:
		plt.figure(figsize=(10, 6))
		plt.plot(x_rango, y_rango, 'b-', linewidth=2, label=f'g(x) = {expresion}')
		plt.plot(x_rango, x_rango, 'g--', linewidth=2, label='y = x')
		plt.grid(True, alpha=0.3)
		plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
		plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
		plt.xlabel('x', fontsize=12)
		plt.ylabel('y', fontsize=12)
		plt.title('Gráfica del Punto Fijo: Intersección de g(x) con y = x', fontsize=14, fontweight='bold')
		plt.legend(fontsize=10)
		plt.tight_layout()
		print("✅ Gráfica generada. Cierra la ventana de la gráfica para continuar...\n")
		plt.show()
	except Exception as error:
		print(f"⚠️  Error al graficar: {error}\n")


def graficar_resultado(g, expresion, x0, historial, x_aprox):
	if not historial:
		return
	aproximaciones = [x0] + [registro['x_siguiente'] for registro in historial]
	rango = max(max(abs(valor - x_aprox) for valor in aproximaciones), 2)
	x_plot = np.linspace(x_aprox - rango, x_aprox + rango, 600)
	y_plot = []
	for valor in x_plot:
		try:
			y_plot.append(g(valor))
		except Exception:
			y_plot.append(np.nan)
	y_recta = x_plot
	y_aprox = []
	for valor in aproximaciones:
		try:
			y_aprox.append(g(valor))
		except Exception:
			y_aprox.append(np.nan)
	try:
		plt.figure(figsize=(10, 6))
		plt.plot(x_plot, y_plot, 'b-', linewidth=2, label=f'g(x) = {expresion}')
		plt.plot(x_plot, y_recta, 'g--', linewidth=2, label='y = x')
		plt.scatter(aproximaciones, y_aprox, color='orange', s=35, label='Aproximaciones')
		plt.plot(x_aprox, g(x_aprox), 'ro', markersize=9, label=f'Punto fijo aprox: {x_aprox:.6f}')
		plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
		plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
		plt.grid(True, alpha=0.3)
		plt.xlabel('x', fontsize=12)
		plt.ylabel('y', fontsize=12)
		plt.title('Método del Punto Fijo - Aproximación del punto fijo', fontsize=14, fontweight='bold')
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
	mostrar_recomendaciones_usuario()
	while True:
		expresion = input("Ingresa la función g(x) en términos de x (ejemplo: 'math.cos(x)' o '(x + 2/x)/2'): ").strip()
		if not expresion:
			print("⚠️  Error: debes ingresar una función.\n")
			continue
		if expresion_valida_para_inicio(expresion):
			break
		print("⚠️  Error: la función no pudo evaluarse con valores de prueba.")
		print("Asegúrate de usar sintaxis Python válida (ejemplo: x/2 + 1 o math.cos(x)).")
		print("Si usas divisiones con x, evita valores iniciales donde el denominador sea 0.\n")

	def g(x):
		return evaluar_expresion(expresion, x)

	print("\n>>> Graficando función para análisis visual...")
	graficar_funcion(g, expresion)
	print("=" * 70)
	print("🔍 ANÁLISIS DE POSIBLES PUNTOS FIJOS")
	print("=" * 70)
	print("Buscando intervalos donde g(x) - x cambia de signo...\n")
	print("Si no aparecen sugerencias, puedes elegir un x0 cercano al valor donde la gráfica cruza y = x.\n")
	cambios_signo = buscar_cambios_signo(g)
	if cambios_signo:
		print(f"✅ Se encontraron {len(cambios_signo)} posibles puntos fijos:")
		for indice, (x_izquierda, x_derecha) in enumerate(cambios_signo[:5], 1):
			print(f"   {indice}. Intervalo: [{x_izquierda:.4f}, {x_derecha:.4f}]")
		if len(cambios_signo) > 5:
			print(f"   ... y {len(cambios_signo) - 5} más")
	else:
		print("⚠️  No se detectaron cambios de signo evidentes en el rango analizado.")
	while True:
		x0 = solicitar_valor_inicial(cambios_signo)
		if validar_valor_inicial(g, x0):
			break
		print("Ingresa un nuevo valor inicial para continuar.\n")
	tolerancia = solicitar_tolerancia()
	max_iteraciones = solicitar_max_iteraciones()
	x_aproximada, convergio, historial, motivo = metodo_punto_fijo(g, x0, tolerancia, max_iteraciones)
	print("\n" + "=" * 70)
	print("📊 RESULTADOS FINALES")
	print("=" * 70)
	if historial:
		ultima = historial[-1]
		valor_gx = ultima['x_siguiente']
		residuo = ultima['residuo']
		iteraciones = ultima['iteracion']
	else:
		try:
			valor_gx = g(x_aproximada)
			residuo = abs(valor_gx - x_aproximada)
		except Exception:
			valor_gx = None
			residuo = None
		iteraciones = 0
	if convergio:
		print(f"✅ PUNTO FIJO ENCONTRADO: x = {x_aproximada:.10f}")
		if valor_gx is not None:
			print(f"   g(x) = {valor_gx:.10f}")
			print(f"   |g(x) - x| = {residuo:.10e}")
		else:
			print("   g(x) = No disponible")
			print("   |g(x) - x| = No disponible")
		print(f"   Iteraciones realizadas: {iteraciones}")
		print(f"   Tolerancia utilizada: {tolerancia}")
	else:
		print("⚠️  NO SE ALCANZÓ LA CONVERGENCIA")
		print(f"   Última aproximación: x = {x_aproximada:.10f}")
		if valor_gx is not None:
			print(f"   g(x) = {valor_gx:.10f}")
			print(f"   |g(x) - x| = {residuo:.10e}")
		else:
			print("   g(x) = No disponible")
			print("   |g(x) - x| = No disponible")
		print(f"   Iteraciones realizadas: {iteraciones}")
		print(f"   Tolerancia utilizada: {tolerancia}")
	print(motivo)
	print("\n>>> Generando gráfica final...")
	graficar_resultado(g, expresion, x0, historial, x_aproximada)
	if not preguntar_continuar():
		programa_activo = False
		print("\n👋 ¡Gracias por usar el programa! Hasta pronto.\n")
