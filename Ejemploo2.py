# Función que realiza una multiplicación y luego suma un tercer valor
def calcular_producto_y_suma(multiplicando, multiplicador, suma_extra):
    return multiplicando * multiplicador + suma_extra

# Función principal que define los valores y llama a la función de cálculo
def ejecutar_calculo():
    valor1 = 5
    valor2 = 3
    valor_extra = 7
    resultado = calcular_producto_y_suma(valor1, valor2, valor_extra)
    print("El resultado es:", resultado)

# Ejecutar el programa
ejecutar_calculo()
