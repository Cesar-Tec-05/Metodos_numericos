# Método del Punto Fijo
Programa interactivo para calcular puntos fijos de funciones usando iteración sucesiva.

## 📐 ¿Qué es el Método del Punto Fijo?
El método del punto fijo es un método numérico iterativo para resolver ecuaciones de la forma $x = g(x)$. Si el proceso converge, el valor obtenido es un punto fijo de la función y también una solución de la ecuación original.

### Idea Principal
La iteración se calcula con:

$$x_{n+1} = g(x_n)$$

Donde:
- $x_n$ es la aproximación actual
- $x_{n+1}$ es la siguiente aproximación
- $g(x)$ es la función de iteración

### Interpretación Geométrica
El punto fijo aparece donde la gráfica de $y = g(x)$ intersecta a la recta $y = x$.

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

## 📊 Ejemplos de funciones

### Ejemplo 1: Punto fijo de coseno
```
Función: math.cos(x)
x0: 0.5
Punto fijo: x ≈ 0.7390851332
```

### Ejemplo 2: Método de Herón para raíz cuadrada
```
Función: (x + 5/x) / 2
x0: 2.0
Nota: x0 debe ser distinto de 0
Punto fijo: x ≈ 2.2360679775
```

### Ejemplo 3: Función exponencial
```
Función: math.exp(-x)
x0: 0.5
Punto fijo: x ≈ 0.5671432904
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
**Fecha**: 15 de Abril de 2026  
**Versión**: 1.0
