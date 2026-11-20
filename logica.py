def confirmacion_borrar_contactos(mensaje):
    while True:
        seguro = input(mensaje).strip().lower()
        if seguro in ("s", "si", "sí"):
            return True
        elif seguro in ("n", "no"):
            return False
        else:
            print("\nNo válido")


def editar_etiquetas(mi_agenda: Agenda, nombre):
    etiqueta = pedir_etiqueta()
    resultado = mi_agenda.comprobar_si_un_contacto_tiene_etiqueta_en_especifico(
        nombre, etiqueta
    )
    if resultado:
        print("\nEl contacto ya tiene esa etiqueta")
        return
    mi_agenda.añadir_etiqueta(nombre, etiqueta)
    print(f"\nSe ha añadido la etiqueta al contacto {nombre}")
    print("\nEtiquetas del contacto\n")
    mi_agenda.mostrar_etiquetas_de_un_contacto(nombre)


def tiene_etiquetas(mi_agenda: Agenda, nombre):
    print(f"\nEtiquetas actuales de {nombre}\n")
    etiquetas = mi_agenda.mostrar_etiquetas_de_un_contacto(nombre)
    if etiquetas is not None:
        menu_editar_etiquetas()
        opcion = pedir_opcion([1, 2])
        if opcion == 1:
            editar_etiquetas(mi_agenda, nombre)
        else:
            eliminar_etiquetas(mi_agenda, nombre)


def no_tiene_etiquetas(mi_agenda: Agenda, nombre):
    print(f"\n{nombre} no tiene etiquetas actualmente.")
    menu_añadir_etiquetas()
    opcion = pedir_opcion([1])
    if opcion == 1:
        etiqueta = pedir_etiqueta()
        mi_agenda.añadir_etiqueta(nombre, etiqueta)
        print(f"\nSe ha añadido la etiqueta al contacto {nombre}")
        print("\nEtiquetas del contacto\n")
        mi_agenda.mostrar_etiquetas_de_un_contacto(nombre)


def eliminar_etiquetas(mi_agenda: Agenda, nombre):
    print("\nSeleccione la etiqueta a eliminar\n")
    lista, cantidad_de_etiquetas = mi_agenda.mostrar_etiquetas_de_un_contacto(nombre)
    opcion = pedir_opcion(range(1, cantidad_de_etiquetas + 1))
    eliminado = lista.pop(opcion - 1)
    mi_agenda.guardar_json()
    print(f"\nHa eliminado la etiqueta '{eliminado}' del contacto {nombre}")
    print(f"\nEtiquetas actuales de {nombre}\n")
    mi_agenda.mostrar_etiquetas_de_un_contacto(nombre)