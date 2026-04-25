def pedir_numero(nombre_variable):
    while True:
        try:
            valor = float(input(f"Ingrese {nombre_variable} (kg/h): "))
            return valor
        except ValueError:
            print("Error: debe ingresar un número válido.")

def balance_materia(entrada, salida, generacion, consumo):
    acumulacion = entrada - salida + generacion - consumo
    return acumulacion

print("=== Cálculo de Balance de Materia ===")

entrada = pedir_numero("flujo de entrada")
salida = pedir_numero("flujo de salida")
generacion = pedir_numero("generación")
consumo = pedir_numero("consumo")

resultado = balance_materia(entrada, salida, generacion, consumo)

print("La acumulación es:", resultado, "kg/h")