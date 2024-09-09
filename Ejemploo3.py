# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(ancho, largo):
    return ancho * largo

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

# Función principal
def main():
    # Cálculo del área del rectángulo
    ancho_rectangulo = 4
    largo_rectangulo = 6
    area_rectangulo = calcular_area_rectangulo(ancho_rectangulo, largo_rectangulo)
    print("Área del rectángulo:", area_rectangulo)

    # Cálculo del área del triángulo
    base_triangulo = 5
    altura_triangulo = 8
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print("Área del triángulo:", area_triangulo)

# Ejecutar el programa
main()

