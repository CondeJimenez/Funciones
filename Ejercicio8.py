# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

def edadesMuestra(muestra):
    muestra = list(muestra)
    media = 0
    varianza = 0
    datos = {}

    for i in muestra:
        media += i
    media /= len(muestra)

    for j in muestra:
        varianza += (j - media)**2
    varianza /= len(muestra)
    desviacion = varianza **.5    
    
    datos['Media'] = media
    datos['Varianza'] = varianza
    datos['Desviacion Estandar'] = desviacion
    print("SOLUCION DE KEVIN ",datos)

edadesMuestra([5,6,6,7,8])

# # Solcuion de ALF
# def square(sample):
#     """Función que calcula los cuadrados de una lista de números.
#     Parámetros
#     sample: Es una lista de números
#     Devuelve una lista con los cuadrados de los números de la lista sample.
#     """
#     list = []
#     for i in sample:
#         list.append(i**2)
#     return list

# def statistics(sample):
#     """Función que calcula la media, varianza y desviación típica de una muestra de números.
#     Parámetros
#     sample: Es una lista de números
#     Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
#     """
#     stat = {}
#     stat['media'] = sum(sample)/len(sample)
#     stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
#     stat['desviacion tipica'] = stat['varianza']**0.5
#     print("Solucion de ALF", stat)

# statistics([5,6,6,7,8])