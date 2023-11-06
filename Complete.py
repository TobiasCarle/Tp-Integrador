import os


def obtener_informacion_cliente():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    dni = input("Ingresa tu número de DNI: ")
    telefono = input("Ingresa tu número de teléfono: ")
    direccion = input("Ingresa tu dirección: ")
    print(" ")
    print(f"--------BIENVENIDO {nombre.upper()} {apellido.upper()}--------")
    return nombre, apellido, dni, telefono, direccion


def calcular_volumen_concreto(longitud, anchura, altura):
    # Calcula el volumen multiplicando las dimensiones
    volumen = longitud * anchura * altura
    return volumen


def convertir_volumen(volumen, unidad_destino):
    if unidad_destino == "pies":
        return volumen * 35.3147
    elif unidad_destino == "centimetros":
        return volumen * 100
    elif unidad_destino == "metros":
        return volumen
    else:
        return "Unidad de destino no válida"


def solicitar_conversion_volumen(volumen_concreto):
    convertir = input(
        "¿Desea convertir el volumen a pies o centímetros? (si/no): "
    ).lower()
    if convertir == "si":
        unidad_destino = input(
            "¿A qué unidad desea convertir (pies/centimetros)? "
        ).lower()
        resultado = convertir_volumen(volumen_concreto, unidad_destino)
        print(
            f"Se necesitan {resultado:.2f} {unidad_destino} de hormigón, que equivalen a {volumen_concreto:.2f} metros cúbicos"
        )
        return True
    return False


def main():
    print("Bienvenido a la Calculadora de Concreto")
    nombre, apellido, dni, telefono, direccion = obtener_informacion_cliente()

    print("\nInformación del Cliente:")
    print(f"Nombre: {nombre} {apellido}")
    print(f"DNI: {dni}")
    print(f"Teléfono: {telefono}")
    print(f"Dirección: {direccion}")
    while True:
        try:
            longitud = float(input("\nIngrese la longitud de la superficie (en metros): "))
            if isinstance(longitud, (float, int)):
                break
            else:
                print("Longitud inválida")
        except ValueError as e:
            print("Ha ocurrido un error: ", e)
    anchura = float(input("Ingrese la anchura de la superficie (en metros): "))
    altura = float(input("Ingrese la altura de la superficie (en metros): "))

    volumen_concreto = calcular_volumen_concreto(longitud, anchura, altura)

    print(f"\nSe necesitan {volumen_concreto:.2f} metros cúbicos de hormigón.")

    if solicitar_conversion_volumen(volumen_concreto):
        nueva_conversion = input(
            "\n¿Desea convertir de nuevo a pies o centímetros? (si/no): "
        ).lower()
        if nueva_conversion == "si":
            unidad_origen = input(
                "¿A qué unidad desea convertir (pies/centimetros)? "
            ).lower()
            resultado = convertir_volumen(volumen_concreto, unidad_origen)
            print(
                f"Se necesitan {resultado:.2f} {unidad_origen} de hormigón que equivalen a {volumen_concreto:.2f} metros cúbicos"
            )

    tipo_hormigon = input(
        "\nIngrese el tipo de hormigón (normal, ligero o pesado): "
    ).lower()

    while tipo_hormigon not in ["normal", "ligero", "pesado"]:
        print("El tipo de hormigón ingresado no es válido.")
        tipo_hormigon = input(
            "Ingrese el tipo de hormigón (normal, ligero o pesado): "
        ).lower()

    if tipo_hormigon == "normal":
        costo_hormigon = 100
    elif tipo_hormigon == "ligero":
        costo_hormigon = 80
    elif tipo_hormigon == "pesado":
        costo_hormigon = 120

    cantidad_hormigon = volumen_concreto
    costo_total = costo_hormigon * cantidad_hormigon

    print(f"El costo del hormigón es de {costo_hormigon} dólares por metro cúbico.")
    print(f"El costo total del hormigón es de {costo_total:.2f} dólares.")
    # Crear el directorio "carpeta_clientes" y guardar la información del cliente
    # os.mkdir("carpeta_clientes")
    os.chdir("carpeta_clientes")
    nombre_fichero = "datos-clientes" + ".txt"
    f = open(nombre_fichero, "w")
    f.write(
        str(
            f" CLIENTE: {nombre.upper()} {apellido.upper()}\n DNI: {dni} TEL: {telefono} DIR: {direccion.upper()} \n CANT.HORMIGON REQ: {volumen_concreto:.2f} \n TOTAL COSTO: ${costo_total}"
        )
    )
    f.close()


if __name__ == "__main__":
    main()
