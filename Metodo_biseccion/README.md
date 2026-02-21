# Método de la Bisección
Programa interactivo para calcular raíces de funciones usando el método de bisección con visualización gráfica.

## 🎯 Características
- Entrada de funciones matemáticas personalizadas
- Visualización gráfica de la función
- Detección automática de intervalos con cambios de signo
- Recomendaciones inteligentes de parámetros
- Iteraciones detalladas en tabla
- Gráfica final con la raíz encontrada
- Validaciones robustas en todos los inputs
- Menú interactivo para múltiples cálculos

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
python "Metodo de la biseccion.py"
```
### Flujo de uso:
1. Seleccionar "Calcular" en el menú principal
2. Ingresar función en términos de `x` (ej: `x**2 - 4`)
3. Observar gráfica inicial (cierra la ventana para continuar)
4. Revisar análisis de posibles raíces
5. Ingresar parámetros de búsqueda:
   - Inicio del barrido
   - Final del barrido
   - Paso (o usar sugerencia)
   - Tolerancia (o usar default: 0.00001)
6. Ver resultados y gráfica final

## 📊 Salida del Programa
El programa muestra:
- Tabla de iteraciones con valores de `a`, `b`, `c (punto medio)`, `f(c)` y error
- Raíz aproximada con alta precisión
- Valor de f(x) en la raíz
- Error final vs tolerancia objetivo
- Número total de iteraciones

## 📚 Método de Bisección
El método de bisección es un algoritmo numérico para encontrar raíces de funciones continuas. Funciona:
1. Buscando un intervalo [a,b] donde f(a) y f(b) tienen signos opuestos
2. Dividiendo repetidamente el intervalo por la mitad
3. Seleccionando el subintervalo donde hay cambio de signo
4. Repitiendo hasta alcanzar la tolerancia deseada
**Convergencia:** Garantizada si existe una raíz en el intervalo inicial.

### Autor
- Cesar de Jesus Becerra Vera - Estudiante de Ingeniería en Computación
- Universidad de Guadalajara - Centro Universitario de los Altos (CUAltos)
- Materia: Métodos Numéricos - 4to Semestre 2026-A