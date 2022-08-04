def area (radio, altura):
    pi = 3.14
    circulo = (pi * radio) ** 2
    triangulo = ((pi * altura) * (radio**2))

    print(f"El área de un circulo es {round(circulo,2)}")
    print(f"El área del tirangulo es {round(triangulo,2)}")
    
area(3, 10)