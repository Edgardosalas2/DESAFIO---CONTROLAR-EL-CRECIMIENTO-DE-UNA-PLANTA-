# lagrange_interpolation.py

def lagrange(x, y, valor):
    total = 0
    n = len(x)
    for i in range(n):
        producto = y[i]
        for j in range(n):
            if i != j:
                producto *= (valor - x[j]) / (x[i] - x[j])
        total += producto
    return total

# Datos
x = [30, 60, 90]
y = [50, 100, 153.5]


# Día a evaluar
dia = 45

# Cálculo
altura_estim = lagrange(x, y, dia)

print(f"Altura estimada al día {dia} con interpolación de Lagrange: {altura_estim:.4f} cm")
