def balance_materia(entrada, salida, generacion, consumo):
    acumulacion = entrada - salida + generacion - consumo
    return acumulacion

entrada = float(input("Flujo de entrada (kg/h): "))
salida = float(input("Flujo de salida (kg/h): "))
generacion = float(input("Generación (kg/h): "))
consumo = float(input("Consumo (kg/h): "))

resultado = balance_materia(entrada, salida, generacion, consumo)

print("La acumulación es:", resultado, "kg/h")