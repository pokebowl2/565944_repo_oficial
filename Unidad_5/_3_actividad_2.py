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

estudiantes = []

def leer_nombre():
    nombre = input("Ingrese su nombre: ")
    return nombre

def validar_nombre(nombre):
    if nombre.strip() != "":
        return True
    else:
        return False
    
def persistir_nombre(nombre):
    estudiantes.append(nombre)
    return True


def main():
    print("Bienvenido!")
    nombre = leer_nombre()
    valid_nombre = validar_nombre(nombre)
    if valid_nombre:
        persistir_nombre(nombre)
        print(f"Nombre {nombre} agregado.")
        print(estudiantes)
    else:
        print("El nombre ingresado es invalido.")

main()