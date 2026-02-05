# Calculadora de Matrices - Método Gauss-Jordan

**Autor:** Cesar de Jesus Becerra Vera  
**Institución:** Centro Universitario de los Altos - Universidad de Guadalajara  
**Carrera:** Ingeniería en Computación - 4to Semestre  
**Profesor:** Juan Manuel  
**Fecha:** 04 de Febrero de 2026  
**Versión:** 1.0

## Descripción

Programa de terminal que implementa el método de Gauss-Jordan para reducir matrices a su forma escalonada reducida. El programa muestra paso a paso las operaciones realizadas durante el proceso de eliminación.

## Características

- Entrada de matrices de cualquier dimensión
- Visualización paso a paso del proceso de reducción
- Manejo de pivotes cero y casos especiales
- Interfaz de terminal interactiva
- Formato numérico preciso con 4 decimales

## Requisitos

- Python 3.x
- NumPy

## Instalación

```bash
pip install numpy
```

## Uso

Ejecutar el programa:

```bash
python src/main.py
```

### Ejemplo de uso

1. Seleccionar opción 1 para reducir una matriz
2. Ingresar número de filas y columnas
3. Ingresar los elementos de cada fila separados por espacios
4. El programa mostrará cada paso de la reducción

**Ejemplo de entrada:**
```
Número de filas: 3
Número de columnas: 4
Fila 1: 2 1 -1 8
Fila 2: -3 -1 2 -11
Fila 3: -2 1 2 -3
```

## Método Gauss-Jordan

El método realiza las siguientes operaciones:

1. **Pivoteo parcial:** Selecciona el elemento de mayor valor absoluto como pivote
2. **Normalización:** Divide la fila del pivote para que el pivote sea 1
3. **Eliminación:** Elimina los elementos arriba y abajo del pivote en su columna

El resultado es una matriz en forma escalonada reducida donde se puede leer directamente la solución del sistema.

## Estructura del Proyecto

```
calculadora_gauss_jordan/
├── src/
│   └── main.py          # Código principal
├── dist/                # Ejecutables compilados
├── doc/                 # Documentación adicional
└── README.md           # Este archivo
```

## Autor

Cesar de Jesus Becerra Vera  
Centro Universitario de los Altos - Universidad de Guadalajara  
Ingeniería en Computación - Metodos Numéricos
