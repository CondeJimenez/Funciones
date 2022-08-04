# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def mediaAritmetica(*muestra):
    muestra = list(muestra)
    longitudmuestra = len(muestra)
    sumamuestra = 0
    
    for media in muestra:
        sumamuestra += media
    print(f"Suma de todas las muestras {sumamuestra}")
    media = sumamuestra/longitudmuestra
    print(f"La media aritmetica de los valores ingresados son {round(media,2)}")

mediaAritmetica(2,42,35,100,80,120)