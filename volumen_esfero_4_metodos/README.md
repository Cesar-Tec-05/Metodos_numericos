# Volumen de Esfera - Resolución con 4 Métodos Numéricos

## 📋 Descripción

Este programa implementa **4 métodos numéricos diferentes** para resolver la ecuación que determina la altura de un casquete esférico:

$$\pi \cdot h^2 \cdot \left(3r - \frac{h}{3}\right) - 30 = 0$$

Donde:
- **r = 3** (radio de la esfera)
- **h** = altura del casquete que queremos encontrar
- **30** = volumen objetivo del casquete

### Ecuación Específica del Problema
Sustituyendo r = 3:

$$\pi \cdot h^2 \cdot \left(9 - \frac{h}{3}\right) - 30 = 0$$

## 📚 Métodos Implementados
### 1. **Bisección**
- Método de búsqueda que divide repetidamente un intervalo por la mitad
- **Ventajas:** Convergencia garantizada, simple de implementar
- **Desventajas:** Convergencia lenta
- **Requiere:** Un intervalo [a, b] donde f(a)·f(b) < 0

### 2. **Regla Falsa (Posición Falsa)**
- Método que interpola linealmente entre dos puntos
- **Ventajas:** Convergencia más rápida que bisección
- **Desventajas:** Puede ser lento en algunos casos
- **Requiere:** Un intervalo [a, b] donde f(a)·f(b) < 0

### 3. **Newton-Raphson**
- Método que usa la derivada de la función
- **Ventajas:** Convergencia muy rápida (cuadrática)
- **Desventajas:** Requiere la derivada, puede no converger
- **Requiere:** Un valor inicial h₀ cercano a la raíz

### 4. **Secante**
- Método similar a Newton-Raphson pero sin usar la derivada
- **Ventajas:** No requiere calcular la derivada analítica
- **Desventajas:** Convergencia más lenta que Newton-Raphson
- **Requiere:** Dos valores iniciales h₀ y h₁

## 🚀 Uso del Programa

### Requisitos
- Python 3.x
- Librerías: `numpy`, `matplotlib`

### Instalación de dependencias
```bash
pip install numpy matplotlib
```

### Ejecución
```bash
python main.py
```

## 📝 Notas Matemáticas

La ecuación representa el volumen de un casquete esférico:
$$V = \pi h^2 \left(3r - \frac{h}{3}\right) = 30$$

Donde:
- h está entre 0 y 2r = 6 (diámetro de la esfera)
- Cuando h = 0: V = 0
- Cuando h = 2r = 6: V = 36π ≈ 113.1 (volumen total de la esfera)
- Cuando h = 3: V = π·9·(9-1) = 72π ≈ 226.2 (mayor que 30)

## 👨‍💻 Autor

**Cesar de Jesus Becerra Vera**
- Centro Universitario de Los Altos / Universidad de Guadalajara
- Ingeniería en Computación - 4to Semestre
- Profesor: Juan Manuel

## 📅 Versión e Información

- **Versión:** 1.0
- **Fecha:** 24 de Marzo de 2026
- **Archivo:** main.py

## 📄 Licencia
Este proyecto es parte de la asignatura de Métodos Numéricos.

---

**¡Gracias por usar el programa!** 🚀
