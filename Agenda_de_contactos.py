# agenda de contactos. pedir nombres y telefonos hasta que el usuario escriba "fin"
# Guardar en diccionario y mostrar al final.
# Funciones a añadir: agregar_contacto, buscar_contacto, eliminar_contacto, mostrar_agenda
# main() con menú
"""1. Función pedir_nombre(mensaje)  ok
2. Función pedir_telefono(mensaje)  ok
3. Función agregar_contacto(agenda)  ok
4. Función buscar_contacto(agenda) ok
5. Función eliminar_contacto(agenda) ok
6. Función mostrar_agenda(agenda)  ok
7. Función menu()
8. Función pedir_opcion(mensaje, opciones)
9. Función main()"""


def pedir_nombre():
    return input("\nNuevo contacto: ").title().strip()


def pedir_telefono():
    while True:
        try:
            teléfono = int(input("\nIntroduzca el número telefónico: "))
        except ValueError:
            print("Solo números.")
            continue
        return teléfono


def agregar_contacto(agenda):
    while True:
        nombre = pedir_nombre()
        if any(contacto["Nombre"] == nombre for contacto in agenda):
            print("\nEse contacto ya está en la agenda")
            continue
        else:
            telefono = pedir_telefono()
            agenda.append({"Nombre": nombre, "Teléfono": telefono})
            print(f"\nContacto {nombre} añadido\n")
            break


def buscar_contacto(agenda):
    contacto_a_buscar = input("\nIntroduzca el contacto a buscar: ").title().strip()
    encontrado = False
    for contacto in agenda:
        if contacto["Nombre"] == contacto_a_buscar:
            print("\nResultado de la búsqueda: ")
            print(f'\n{contacto["Nombre"]}: {contacto["Teléfono"]}')
            encontrado = True
            
    if not encontrado:
        print("\nContacto no existe")


def eliminar_contacto(agenda):
    contacto_a_eliminar = input("\nIntroduzca el nombre del contacto a eliminar: ") .title() .strip()
    for contacto in agenda:
        if contacto["Nombre"] == contacto_a_eliminar:
            agenda.remove(contacto)
            return f"\nSe ha eliminado el contacto {contacto_a_eliminar}."
    return f"\nNo se encontró ningún contacto llamado {contacto_a_eliminar}."


def mostrar_agenda(agenda):
    print("\nLa lista de contactos es la siguiente: \n")
    ordenados = sorted(agenda, key=lambda x: x["Nombre"])
    for i, contactos in enumerate(ordenados, start=1):
        print(f"{i}. {contactos['Nombre']}: {contactos['Teléfono']}")


def eliminar_todos_los_contactos(agenda):
    agenda.clear()
    print("\nSe han eliminado todos los contactos de la agenda\n")


def menu():
    print("\n____MENU____")
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Eliminar todos los contactos")
    print("6. Salir")


def pedir_opcion(opciones):
    while True:
        opcion = input("\nIntroduzca una opción: ")
        if opcion in opciones:
            return opcion
        else:
            print("\nOpción no válida")


def programa():
    agenda = []
    print("\nBienvenido a su agenda de contactos")
    while True:
        menu()
        opcion = pedir_opcion(["1", "2", "3", "4", "5", "6"])
        match opcion:
            case "1":
                agregar_contacto(agenda)
            case "2":
                if not agenda:
                    print("\nAún no ha guardado ningún contacto")
                else:
                    mostrar_agenda(agenda)
            case "3":
                if not agenda:
                    print("\nAún no ha guardado ningún contacto")
                else:
                    buscar_contacto(agenda)
            case "4":
                if not agenda:
                    print("\nAún no ha guardado ningún contacto")
                else:
                    elimino = eliminar_contacto(agenda)
                    print(elimino)
            case "5":
                if not agenda:
                    print("\nAún no ha guardado ningún contacto")
                else:
                    eliminar_todos_los_contactos(agenda)
            case "6":
                return


def main():
    programa()
    print("\nHa salido satisfactoriamente del programa.\n")


if __name__ == "__main__":
    main()
