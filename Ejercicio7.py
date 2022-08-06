def cuadrados(numeros):

    """función que reciba una muestra de números en una lista 
    y devuelve otra lista con su cuadrado"""

    numcuadrados = []

    for i in numeros:
        i = i**2
        numcuadrados.append(i)
    return numcuadrados

print(cuadrados([2,3,4,5]))