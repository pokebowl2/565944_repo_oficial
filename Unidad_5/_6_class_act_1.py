"""
CONSIGNA:
Se nos solicita crear un bloque de código que realice lo siguiente:

1. Imprimir un mensaje de bienvenida
2. Leer el nombre de un estudiante por consola
3. Verificar que sea un nombre válido
4. Si es válido guardarlo en la lista global
5. Si es inválido, mostrar un mensaje en la consola
6. A fin de poder repetir el flujo, incluir el código dentro de un bucle while
"""

# Declaro la variable global
estudiantes = []

while True:
    print("Bienvenida...")
    nombre = input("Ingrese su nombre: ")

    if nombre.strip() != "": # != falso
        # condicion True
        # Guardo el nombre en la lista global
        estudiantes.append(nombre)
        print(f"La lista actualizada es: {estudiantes}")
    else:
        # Condicion False
        print("Nombre No puede quedar en blanco")

    flag = input("Ingrese 's' para terminar: ")





# if nombre.strip() == "": # != falso
#     # condicion True
#     print("Nombre No puede quedar en blanco")
# else:
#     # Condicion False
#     print("Nombre OK")

