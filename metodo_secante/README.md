# Método de la Secante
Programa interactivo para calcular raíces de funciones usando el método de la secante.

## 📐 ¿Qué es el Método de la Secante?
El método de la secante es un método numérico iterativo para encontrar raíces de funciones. Es una variante de Newton-Raphson que no requiere la derivada analítica, ya que aproxima la pendiente usando dos puntos previos.

### Fórmula
La nueva aproximación se calcula con:

$$x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}$$

Donde:
- $x_{n-1}$ y $x_n$ son las dos aproximaciones previas
- $x_{n+1}$ es la nueva aproximación
- $f(x_n)$ y $f(x_{n-1})$ son los valores de la función en esos puntos

## 📋 Requisitos
### Python
- Python 3.7 o superior
### Dependencias
```
numpy
matplotlib
```

## 🚀 Instalación
1. **Clonar el repositorio o navegar al directorio del proyecto**
2. **Instalar dependencias:**
	```bash
	pip install numpy matplotlib
	```
3. **En Linux, si matplotlib no muestra gráficas, instalar:**
	```bash
	sudo apt-get install python3-tk
	```

## 💻 Uso
### Ejecutar el programa:
```bash
cd src
python main.py
```

### Flujo del programa
1. **Seleccionar opción** del menú principal
2. **Ingresar la función** en términos de x (ejemplo: `x**3 - x - 2`)
3. **Ver gráfica** inicial para análisis visual
4. **Revisar intervalos sugeridos** (si se detectan cambios de signo)
5. **Configurar parámetros**:
	- Dos valores iniciales $x_0$ y $x_1$
	- Tolerancia (default: 0.00001)
	- Máximo de iteraciones (default: 100)
6. **Observar iteraciones** en tabla
7. **Revisar resultado final** y gráfica con aproximaciones

## 📊 Ejemplos de funciones

### Ejemplo 1: Función cúbica
```
Función: x**3 - x - 2
x0: 1
x1: 2
Raíz: x ≈ 1.52138
```

### Ejemplo 2: Función trigonométrica
```
Función: math.cos(x) - x
x0: 0
x1: 1
Raíz: x ≈ 0.73909
```

### Ejemplo 3: Ecuación exponencial
```
Función: math.exp(x) - 3*x
x0: 0
x1: 1
Raíz: x ≈ 0.61906
```

## 🧮 Sintaxis de funciones
### Operadores básicos
- `+` : Suma
- `-` : Resta
- `*` : Multiplicación
- `/` : División
- `**` : Potencia
- `%` : Módulo

### Funciones matemáticas (con prefijo `math.`)
```python
math.sqrt(x)    # Raíz cuadrada
math.sin(x)     # Seno
math.cos(x)     # Coseno
math.tan(x)     # Tangente
math.exp(x)     # Exponencial (e^x)
math.log(x)     # Logaritmo natural
math.log10(x)   # Logaritmo base 10
math.pi         # Constante π
math.e          # Constante e
```

## 👨‍🎓 Información Académica
**Autor**: Cesar de Jesus Becerra Vera  
**Institución**: Centro Universitario de los Altos / Universidad de Guadalajara  
**Programa**: Ingeniería en Computación - 4to Semestre  
**Profesor**: Juan Manuel  
**Fecha**: 16 de Marzo de 2026  
**Versión**: 1.0

