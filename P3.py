# spline_cubico.py

from scipy.interpolate import CubicSpline

# Datos conocidos
x = [30, 60, 90]           # Días
y = [50, 100, 153.5]       # Alturas en cm

# Crear spline cúbico
spline = CubicSpline(x, y)

# Día a evaluar
dia = 45

# Evaluar spline en el día 45
altura_estim = spline(dia)

print(f"Altura estimada al día {dia} con Splines Cúbicos: {altura_estim:.4f} cm")
