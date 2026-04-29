# ================================================================
# TITULO: Método de Weignstein - Búsqueda de raíces (híbrido bisección/secante)
# AUTOR: Cesar de Jesus Becerra Vera
# FECHA: 28 de Abril de 2026
# VERSION: 1.0
# ARCHIVO: main.py
# DESCRIPCIÓN: Implementación interactiva del "Método de Weignstein".
# ================================================================

import math
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def evaluar_funcion(expr):
	"""Devuelve una función f(x) que evalúa la expresión dada por el usuario.
	   Se usa `eval` en contexto controlado para permitir `math.` y funciones de `numpy`.
	"""
	# Ambiente seguro limitado
	env = {
		'math': math,
		'np': np,
		'sin': math.sin,
		'cos': math.cos,
		'tan': math.tan,
		'exp': math.exp,
		'sqrt': math.sqrt,
		'log': math.log,
		'pi': math.pi,
		'e': math.e,
	}

	def f(x):
		return eval(expr, env, {'x': x})

	# Probar evaluación mínima
	_ = f(0)
	return f


def buscar_intervalos_cambio_signo(f, xmin=-10, xmax=10, pasos=200):
	"""Busca puntos medios de subintervalos donde f cambia de signo."""
	xs = np.linspace(xmin, xmax, pasos)
	sugeridos = []
	for i in range(len(xs) - 1):
		try:
			y1 = f(xs[i])
			y2 = f(xs[i + 1])
			if np.isnan(y1) or np.isnan(y2):
				continue
			if y1 * y2 < 0:
				sugeridos.append((xs[i], xs[i + 1], (xs[i] + xs[i + 1]) / 2))
		except Exception:
			continue
	return sugeridos


def weignstein_hibrido(f, a, b, tolerancia=1e-6, max_iter=100):
	"""Implementa un método híbrido bisección/secante.

	Estrategia (llamada aquí 'Weignstein'):
	- Parte de un intervalo [a,b] con f(a)*f(b) < 0.
	- En cada iteración intenta un paso de secante entre (a,b).
	  Si la aproximación cae dentro del intervalo y reduce la incertidumbre, la acepta.
	  En caso contrario realiza una bisección clásica.
	- Devuelve (raiz, iter, convergio, historial)
	"""
	historial = []
	fa = f(a)
	fb = f(b)
	if fa * fb > 0:
		raise ValueError('El intervalo no contiene cambio de signo.')

	for k in range(1, max_iter + 1):
		# Paso de secante
		try:
			s = (b - a) / (fb - fa) * fb  # corrección; actual secante root = b - fb*(b-a)/(fb-fa)
			x_sec = b - fb * (b - a) / (fb - fa)
		except Exception:
			x_sec = None

		use_bisec = True
		if x_sec is not None and a < x_sec < b:
			fx_sec = f(x_sec)
			# Aceptar secante si mejora la posición (reduce tamaño del intervalo)
			if abs(b - a) > 1e-15 and (abs(x_sec - a) < (b - a) and abs(x_sec - b) < (b - a)):
				x_next = x_sec
				fx_next = fx_sec
				use_bisec = False

		if use_bisec:
			x_next = (a + b) / 2.0
			fx_next = f(x_next)

		historial.append((k, a, b, x_next, fx_next, abs(b - a)))

		# Condición de parada por valor de función o por tamaño de intervalo
		if abs(fx_next) < tolerancia or abs(b - a) / 2.0 < tolerancia:
			return x_next, k, True, historial

		# Actualizar intervalo manteniendo cambio de signo
		if fa * fx_next < 0:
			b = x_next
			fb = fx_next
		else:
			a = x_next
			fa = fx_next

	return (a + b) / 2.0, max_iter, False, historial


def mostrar_menu():
	print('\n' + '=' * 70)
	print('      MÉTODO DE WEIGNSTEIN - BÚSQUEDA DE RAÍCES (HIBRIDO)')
	print('=' * 70)
	print('1. Calcular raíz de una función')
	print('2. Salir')
	while True:
		op = input('Selecciona opción (1/2): ').strip()
		if op == '1':
			return 'calcular'
		if op == '2':
			return 'salir'
		print('Opción inválida. Intenta de nuevo.')


def preguntar_continuar():
	while True:
		r = input('¿Deseas otro cálculo? (s/n): ').strip().lower()
		if r in ['', 's', 'si', 'sí', 'y']:
			return True
		if r in ['n', 'no']:
			return False
		print('Respuesta inválida.')


if __name__ == '__main__':
	activo = True
	while activo:
		opcion = mostrar_menu()
		if opcion == 'salir':
			print('\nGracias. Hasta pronto.')
			break

		print('\n' + '=' * 70)
		print('📝 INGRESA LA FUNCIÓN f(x)')
		print('=' * 70)
		ejemplo = 'x**3 - x - 2'
		while True:
			fun = input(f"Ingresa f(x) (ejemplo: {ejemplo}) [ENTER para usar ejemplo]: ").strip()
			if fun == '':
				fun = ejemplo
			try:
				f = evaluar_funcion(fun)
				# probar evaluación
				_ = f(1.0)
				break
			except Exception as e:
				print(f'Error al evaluar la función: {e}')

		# Buscar intervalos con cambio de signo
		sugeridos = buscar_intervalos_cambio_signo(f)
		si = sugeridos
		if sugeridos:
			print('\n✅ Se encontraron posibles intervalos con cambio de signo:')
			for i, (aa, bb, xm) in enumerate(sugeridos[:5], 1):
				print(f'  {i}. [{aa:.4f}, {bb:.4f}]  sugerido x0 = {xm:.4f}')
		else:
			print('\n⚠️  No se encontraron cambios de signo en [-10,10]. Se pueden probar intervalos manuales.')

		# Obtener a y b del usuario con sugerencia al presionar ENTER
		print('\nIngresa los extremos del intervalo [a,b] donde exista cambio de signo.')
		if sugeridos:
			a_def, b_def, xm_def = sugeridos[0]
		else:
			a_def, b_def = -1.0, 1.0

		while True:
			try:
				a_in = input(f"a [{a_def}]: ").strip()
				a = float(a_in) if a_in != '' else float(a_def)
				b_in = input(f"b [{b_def}]: ").strip()
				b = float(b_in) if b_in != '' else float(b_def)
				fa = f(a)
				fb = f(b)
				if fa * fb > 0:
					print('⚠️  El intervalo no muestra cambio de signo. Intenta otro intervalo.')
					continue
				break
			except ValueError:
				print('Ingresa números válidos.')
			except Exception as e:
				print(f'Error: {e}')

		# Parámetros del método
		while True:
			try:
				tol_in = input('Tolerancia [1e-6]: ').strip()
				tol = float(tol_in) if tol_in != '' else 1e-6
				if tol <= 0:
					print('La tolerancia debe ser positiva.')
					continue
				break
			except Exception:
				print('Valor inválido para tolerancia.')

		while True:
			try:
				max_in = input('Máx. iteraciones [100]: ').strip()
				max_it = int(max_in) if max_in != '' else 100
				if max_it <= 0:
					print('Debe ser entero positivo.')
					continue
				break
			except Exception:
				print('Valor inválido para iteraciones.')

		# Ejecutar el método
		try:
			raiz, iters, conv, hist = weignstein_hibrido(f, a, b, tol, max_it)
			print('\n' + '=' * 70)
			print('📈 RESULTADO')
			print('=' * 70)
			if conv:
				print(f'✅ Raíz encontrada: x = {raiz:.10f}')
				print(f'   f(x) = {f(raiz):.2e}')
				print(f'   Iteraciones: {iters}')
			else:
				print('⚠️  No convergió dentro del máximo de iteraciones.')
				print(f'Última aproximación: x = {raiz:.10f}  f(x) = {f(raiz):.2e}')

			# Gráfica: función y aproximaciones
			try:
				xs = np.linspace(min(a, b) - 1, max(a, b) + 1, 500)
				ys = [f(x) for x in xs]
				fig, ax = plt.subplots(figsize=(8, 5))
				ax.plot(xs, ys, 'b-', label=f'f(x) = {fun}')
				ax.axhline(0, color='k', linewidth=0.8)
				# Marcar los puntos de iteración
				xs_it = [h[3] for h in hist]
				ys_it = [f(x) for x in xs_it]
				ax.plot(xs_it, ys_it, 'ro', label='Iteraciones')
				ax.set_title('Función y aproximaciones (Weignstein)')
				ax.grid(True, alpha=0.3)
				ax.legend()
				plt.tight_layout()
				print('Mostrando gráfica. Ciérrala para continuar...')
				plt.show()
			except Exception as e:
				print(f'Error al graficar: {e}')

		except Exception as e:
			print(f'Error durante el método: {e}')

		if not preguntar_continuar():
			activo = False
			print('\nGracias. Hasta pronto.')

