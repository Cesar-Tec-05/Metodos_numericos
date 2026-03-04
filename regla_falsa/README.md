# Método de la Regla Falsa (Falsa Posición)
Programa interactivo para calcular raíces de funciones usando el método de la regla falsa.

## 📐 ¿Qué es el Método de la Regla Falsa?
El método de la regla falsa (también conocido como método de falsa posición) es un método numérico para encontrar raíces de funciones. Es similar al método de bisección, pero en lugar de dividir el intervalo a la mitad, utiliza interpolación lineal para encontrar un punto más cercano a la raíz.

### Fórmula
La nueva aproximación se calcula con:

$$x_r = x_l - \frac{f(x_l) \cdot (x_u - x_l)}{f(x_u) - f(x_l)}$$

Donde:
- $x_l$ es el límite inferior del intervalo
- $x_u$ es el límite superior del intervalo
- $x_r$ es la nueva aproximación de la raíz

### Requisitos
- La función debe ser continua en el intervalo
- Debe haber un cambio de signo en el intervalo: $f(x_l) \cdot f(x_u) < 0$

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
python main.py
```

## 📊 Ejemplos de Funciones
### Ejemplo 1: Polinomio cúbico
```
Función: x**3 - x - 2
Intervalo: [1, 2]
Raíz: x ≈ 1.52138
```

### Ejemplo 2: Función trigonométrica
```
Función: math.cos(x) - x
Intervalo: [0, 1]
Raíz: x ≈ 0.73909
```

### Ejemplo 3: Ecuación exponencial
```
Función: math.exp(x) - 3*x
Intervalo: [0, 1]
Raíz: x ≈ 0.61906
```

## 👨‍🎓 Información Académica
**Autor**: Cesar de Jesus Becerra Vera  
**Institución**: Centro Universitario de los Altos / Universidad de Guadalajara  
**Programa**: Ingeniería en Computación - 4to Semestre  
**Profesor**: Juan Manuel  
**Fecha**: 4 de Marzo de 2026
