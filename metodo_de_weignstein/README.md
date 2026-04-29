# Método de Weignstein
Programa interactivo para encontrar raíces de funciones usando una variante híbrida
(bisección + secante) — estilo y documentación consistente con las otras prácticas.

## 📐 ¿Qué es el "Método de Weignstein"?
En este repositorio se denomina "Weignstein" a una estrategia híbrida que combina
pasos de la secante y bisección para obtener un algoritmo robusto y eficiente
cuando se parte de un intervalo con cambio de signo.

## 📋 Requisitos
### Python
- Python 3.7 o superior
### Dependencias
```
numpy
matplotlib
```

## 🚀 Instalación
1. Navega al directorio del proyecto `metodo_de_weignstein`.
2. Instala dependencias:
```bash
pip install numpy matplotlib
```
3. En Linux, si `matplotlib` no muestra ventanas, instala `tk`:
```bash
sudo apt-get install python3-tk
```

## 💻 Uso
### Ejecutar el programa:
```bash
cd metodo_de_weignstein/src
python main.py
```

## 📊 Ejemplos de Uso

```
Función: x**3 - x - 2
Intervalo sugerido: [1.0, 2.0]
Tolerancia: 1e-6
Raíz aproximada: x ≈ 1.5213797069
```

## 🧮 Sintaxis de Funciones
Usa sintaxis válida de Python. Puedes emplear `math.` o las funciones básicas expuestas
por el programa (`sin`, `cos`, `exp`, `sqrt`, `log`, `pi`, `e`). Ejemplos:
```python
math.sqrt(x)
math.sin(x)
x**3 - x - 2
```

## 👨‍🎓 Información Académica
**Autor**: Cesar de Jesus Becerra Vera  
**Institución**: Centro Universitario de los Altos / Universidad de Guadalajara  
**Programa**: Ingeniería en Computación - 4to Semestre  
**Profesor**: Juan Manuel  
**Fecha**: 28 de Abril de 2026  
**Versión**: 1.0


