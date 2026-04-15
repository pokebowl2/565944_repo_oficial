"""
CONSIGNA:
Generar una función principal y luego subfunciones que sean invocadas desde la función principal,
de manera de mantener el mismo workflow de la actividad_1, pero aprovechando las ventajas
de trabajar módulos reutilixables.

1. Imprimir un mensaje de bienvenida
2. Leer el nombre de un estudiante por consola
3. Verificar que sea un nombre válido
4. Si es válido guardarlo en la lista global
5. Si es inválido, mostrar un mensaje en la consola
6. A fin de poder repetir el flujo, incluir el código dentro de un bucle while

"""

# Declaro la variable global
estudiantes = []

# Funcion leer consola
def leer_nombre():
    nombre = input("Ingrese su nombre: ")
    return nombre

# Funcion validar nombre
def validar_nombre(nombre):
    if nombre.strip() != "":
        return True
    else:
        return False

# Funcion persistir
def persistir_nombre(nombre):
    estudiantes.append(nombre)
    return True


# Funcion Principal
def main():
    print("Bienvenida...")
    nombre = leer_nombre()
    valid_nombre = validar_nombre(nombre)
    if valid_nombre:
        # Persisto
        persistir_nombre(nombre)
        print("Nombre guardado")
        print(estudiantes)
    else:
        print("Nombre invalido!")

main()



