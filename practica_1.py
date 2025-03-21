import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return x**2

def f2(x):
    return np.abs((x - 5) / (2 + np.sin(x)))

def f3(x):
    return np.log(x + 1)

def optimizar(func, rango_min, rango_max, num_individuos, maximizar):
    individuos = np.random.randint(0, 2, (num_individuos, 4))
    x = np.array([int("".join(map(str, ind)), 2) for ind in individuos])
    x = np.clip(x, rango_min, rango_max)
    y = func(x)
    
    if maximizar:
        optimo = np.max(y)
        optimo_x = x[np.argmax(y)]
    else:
        optimo = np.min(y)
        optimo_x = x[np.argmin(y)]
    
    return x, y, optimo_x, optimo

def decimal_a_gray(n):
    return n ^ (n >> 1)

def ejecutar_optimizacion():
    print("Seleccione la función:")
    print("1. f(x) = x^2")
    print("2. f(x) = |(x - 5) / (2 + sen(x))|")
    print("3. f(x) = log(x + 1)")
    opcion_funcion = int(input("Ingrese el número de la función: ")) - 1
    func = funciones[opcion_funcion]
    
    rango_min = int(input("Ingrese el rango mínimo: "))
    rango_max = int(input("Ingrese el rango máximo: "))
    num_individuos = int(input("Ingrese el número de individuos: "))
    
    print("Seleccione la opción de optimización:")
    print("1. Maximizar")
    print("2. Minimizar")
    opcion_optimizacion = int(input("Ingrese el número de la opción: "))
    maximizar = opcion_optimizacion == 1
    
    print("Seleccione el tipo de representación:")
    print("1. Binaria")
    print("2. Gray")
    opcion_representacion = int(input("Ingrese el número de la opción: "))
    usar_gray = opcion_representacion == 2
    
    x, y, optimo_x, optimo = optimizar(func, rango_min, rango_max, num_individuos, maximizar)
    
    indices_ordenados = np.argsort(x)
    x_ordenado = x[indices_ordenados]
    y_ordenado = y[indices_ordenados]
    
    plt.plot(x_ordenado, y_ordenado, 'b-', label='Valores Evaluados')
    plt.plot(optimo_x, optimo, 'ro', label='Óptimo')
    plt.xlabel('Valores Decimales')
    plt.ylabel('Valor de la Función')
    plt.title('Optimización de la Función')
    plt.legend()
    plt.show()
    
    print(f"El mejor valor obtenido es:\nNúmero decimal: {optimo_x}\nResultado de la función: {optimo}")
    
    print("No.\tDecimal\tRepresentación\tResultado")
    print("-" * 40)
    for i in range(num_individuos):
        decimal = x[i]
        if usar_gray:
            representacion = format(decimal_a_gray(decimal), '04b')
        else:
            representacion = format(decimal, '04b')
        resultado = y[i]
        print(f"{i+1}\t{decimal}\t{representacion}\t{resultado:.5f}")

funciones = [f1, f2, f3]

if __name__ == "__main__":
    ejecutar_optimizacion()
