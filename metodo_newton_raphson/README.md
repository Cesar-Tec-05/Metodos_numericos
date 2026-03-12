# Método de Newton-Raphson
Programa interactivo para calcular raíces de funciones usando el método de Newton-Raphson.

## 📐 ¿Qué es el Método de Newton-Raphson?
El método de Newton-Raphson (también conocido como método de Newton) es un método numérico iterativo para encontrar raíces de funciones. Es uno de los métodos más eficientes cuando converge, logrando convergencia cuadrática cerca de la raíz.

### Fórmula
La nueva aproximación se calcula con:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Donde:
- $x_n$ es la aproximación actual
- $x_{n+1}$ es la siguiente aproximación
- $f(x_n)$ es el valor de la función en $x_n$
- $f'(x_n)$ es el valor de la derivada en $x_n$

### Interpretación Geométrica
El método traza una línea tangente a la función en el punto actual y toma como nueva aproximación el punto donde esta tangente cruza el eje x.

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
python Main.py
```

### Flujo del Programa
1. **Seleccionar opción** del menú principal
2. **Ingresar la función** en términos de x (ejemplo: `x**2 - 5`)
3. **Elegir método de derivada**:
   - Cálculo automático (recomendado)
   - Ingreso manual (si conoces la derivada)
4. **Ver gráficas** de la función y su derivada
5. **Revisar análisis** de posibles raíces
6. **Configurar parámetros**:
   - Valor inicial $x_0$
   - Tolerancia (default: 0.0001)
   - Máximo de iteraciones (default: 100)
7. **Observar iteraciones** y resultados
8. **Ver gráficas de convergencia**

## 📊 Ejemplos de Funciones

### Ejemplo 1: Raíz cuadrada (Método de Herón)
```
Función: x**2 - 5
x0: 2.0
Raíz: x ≈ 2.2360679775 (√5)
Convergencia: 3-4 iteraciones
```

### Ejemplo 2: Función cúbica
```
Función: x**3 - x - 2
x0: 1.5
Raíz: x ≈ 1.5213797069
Convergencia: 4-5 iteraciones
```

### Ejemplo 3: Función trigonométrica
```
Función: math.cos(x) - x
x0: 0.5
Raíz: x ≈ 0.7390851332 (punto fijo de coseno)
Convergencia: 4-5 iteraciones
```

### Ejemplo 4: Función exponencial
```
Función: math.exp(x) - 3
x0: 1.0
Raíz: x ≈ 1.0986122887 (ln(3))
Convergencia: 4-5 iteraciones
```

### Ejemplo 5: Ecuación trascendental
```
Función: x*math.exp(x) - 1
x0: 0.5
Raíz: x ≈ 0.5671432904 (función W de Lambert)
Convergencia: 5-6 iteraciones
```

## 🧮 Sintaxis de Funciones
### Operadores Básicos
- `+` : Suma
- `-` : Resta
- `*` : Multiplicación
- `/` : División
- `**` : Potencia
- `%` : Módulo

### Funciones Matemáticas (requieren prefijo `math.`)
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
**Fecha**: 11 de Marzo de 2026  
**Versión**: 2.0
