import math

def calcular_probabilidad_azar(intentos, aciertos):
    """
    Calcula la probabilidad de obtener 'n' aciertos por puro azar
    en una prueba Zener estándar (p = 0.2).
    """
    p = 0.2  # Probabilidad de 1 en 5
    q = 0.8  # Probabilidad de fallo
    
    # Fórmula de distribución binomial
    combinaciones = math.comb(intentos, aciertos)
    probabilidad = combinaciones * (p**aciertos) * (q**(intentos - aciertos))
    
    return probabilidad * 100

# Ejemplo de uso para el investigador
print(f"Probabilidad de 10 aciertos en 25 intentos: {calcular_probabilidad_azar(25, 10):.4f}%")