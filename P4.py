# logistica.py

import math

def logistica(x, a, b, K):
    return K / (1 + math.exp(-(a + b * x)))

# Parámetros ya ajustados
a = 0.5
b = 0.11810
K = 74.95994

# Día a evaluar
dia = 45

# Cálculo
altura = logistica(dia, a, b, K)

print(f"Altura estimada al día {dia} con regresión logística: {altura:.4f} cm")
