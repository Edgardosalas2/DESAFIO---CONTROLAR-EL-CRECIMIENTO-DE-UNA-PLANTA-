# newton_interpolation.py

def diferencias_divididas(x, y):
    n = len(x)
    coef = [yi for yi in y]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

def evaluar_newton(x, coef, valor):
    n = len(coef)
    resultado = coef[-1]
    for i in range(n - 2, -1, -1):
        resultado = resultado * (valor - x[i]) + coef[i]
    return resultado

# Datos
x = [30, 60, 90]
y = [50, 100, 153.5]

# Día a evaluar
dia = 45

# Cálculo
coeficientes = diferencias_divididas(x, y)
altura_estim = evaluar_newton(x, coeficientes, dia)

print(f"Altura estimada al día {dia} con interpolación de Newton: {altura_estim:.4f} cm")
