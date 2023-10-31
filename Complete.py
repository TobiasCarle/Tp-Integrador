import datetime

fecha_actual = datetime.date.today()

print(fecha_actual.strftime("%d/%m/%Y"))

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
    convertir = input("¿Desea convertir el volumen a pies o centímetros? (si/no): ").lower()
    if convertir == "si":
        unidad_destino = input("¿A qué unidad desea convertir (pies/centimetros)? ").lower()
        resultado = convertir_volumen(volumen_concreto, unidad_destino)
        print(f"Se necesitan {resultado:.2f} {unidad_destino} de hormigón, que equivalen a {volumen_concreto:.2f} metros cúbicos")
        return True
    return False

def main():
    print("Bienvenido a la Casa del Hormigon")
    nombre, apellido, dni, telefono, direccion = obtener_informacion_cliente()

    print("\nInformación del Cliente:")
    print(f"Nombre: {nombre} {apellido}")
    print(f"DNI: {dni}")
    print(f"Teléfono: {telefono}")
    print(f"Dirección: {direccion}")

    longitud = float(input("\nIngrese la longitud de la superficie (en metros): "))
    anchura = float(input("Ingrese la anchura de la superficie (en metros): "))
    altura = float(input("Ingrese la altura de la superficie (en metros): "))

    volumen_concreto = calcular_volumen_concreto(longitud, anchura, altura)

    print(f"\nSe necesitan {volumen_concreto:.2f} metros cúbicos de hormigón.")

    if solicitar_conversion_volumen(volumen_concreto):
        nueva_conversion = input("\n¿Desea convertir de nuevo a pies o centímetros? (si/no): ").lower()
        if nueva_conversion == "si":
            unidad_origen = input("¿A qué unidad desea convertir (pies/centimetros)? ").lower()
            resultado = convertir_volumen(volumen_concreto, unidad_origen)
            print(f"Se necesitan {resultado:.2f} {unidad_origen} de hormigón que equivalen a {volumen_concreto:.2f} metros cúbicos")

    tipo_hormigon = input("\nIngrese el tipo de hormigón (normal, ligero o pesado): ").lower()

    while tipo_hormigon not in ["normal", "ligero", "pesado"]:
        print("El tipo de hormigón ingresado no es válido.")
        tipo_hormigon = input("Ingrese el tipo de hormigón (normal, ligero o pesado): ").lower()

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
    if not os.path.exists("carpeta_clientes"):
        os.mkdir("carpeta_clientes")

    nombre_fichero = os.path.join("carpeta_clientes", "datos-clientes.txt")
    with open(nombre_fichero, "w") as f:
        f.write(f"CLIENTE: {nombre.upper()} {apellido.upper()}\nDNI: {dni}\nTEL: {telefono}\nDIR: {direccion.upper()}\nCANT.HORMIGON REQ: {volumen_concreto:.2f} metros cúbicos.\nCOSTO TOTAL: ${costo_total:.2f}")
       
if __name__ == "__main__":
    main()



