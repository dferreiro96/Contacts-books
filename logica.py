from Clases import Agenda, ContactoLaboral, ContactoPersonal
from menus import (
    menu_añadir_etiquetas,
    menu_editar_etiquetas,
    menu_editar_por,
    menu_filtar_contactos,
    menu_mostrar_tipo_de_contacto,
    menu_tipo_de_contacto,
)
from utilidades import (
    pedir_cargo,
    pedir_correo_electronico,
    pedir_empresa,
    pedir_etiqueta,
    pedir_fecha_cumple,
    pedir_nombre,
    pedir_opcion,
    pedir_parentesco,
    pedir_telefono,
)


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
    
    
def formatear_numero_de_telefono(telefono):
    if len(telefono) == 8:
        return f"+53 {telefono[:1]}-{telefono[1:4]}-{telefono[4:]}"
    else:
        return telefono


def modificar_fecha_de_cumpleaños(mi_agenda: Agenda, nombre):
    nueva_fecha_de_cumpleaños = mi_agenda.modificar_fecha_de_cumpleaños(nombre)
    if nueva_fecha_de_cumpleaños:
        print("\nHa cambiado la fecha de cumpleaños correctamente.")
    else:
        print("\nNo se le puede añadir fecha de cumpleaños a ese tipo de contacto")


def modificar_generica(funcion, mensaje, mensaje2):
    if funcion:
        print(f"\nHa editado {mensaje} correctamente.")
    else:
        print(f"\nYa existe un contacto con {mensaje2}")


def modificar_etiquetas(mi_agenda: Agenda, nombre):
    tiene_etiqueta = mi_agenda.comprobar_si_un_contacto_tiene_etiquetas(nombre)
    if tiene_etiqueta is not None:
        tiene_etiquetas(mi_agenda, nombre)
        return
    no_tiene_etiquetas(mi_agenda, nombre)


def gestionar_edicion_de_contactos(mi_agenda: Agenda):
    nombre = pedir_nombre()
    contacto = mi_agenda.buscar_contacto_por_nombre(nombre)
    if contacto is not None:
        menu_editar_por()
        opcion = pedir_opcion([1, 2, 3, 4, 5, 6])
        match opcion:
            case 1:
                modificar_generica(
                    mi_agenda.modificar_nombre(contacto),
                    "el nombre del contacto",
                    "ese nombre",
                )
            case 2:
                modificar_generica(
                    mi_agenda.modificar_telefono(contacto),
                    "el número de teléfono",
                    "ese número de teléfono",
                )
            case 3:
                modificar_generica(
                    mi_agenda.modificar_correo_electronico(contacto),
                    "la dirección de correo electrónica",
                    "esa dirección de correo electrónica",
                )
            case 4:
                modificar_fecha_de_cumpleaños(mi_agenda, nombre)
            case 5:
                modificar_etiquetas(mi_agenda, nombre)
            case 6:
                return
    else:
        print("\nContacto no existe")


def gestionar_busqueda_de_contactos(mi_agenda: Agenda):
    if not mi_agenda.lista_de_contactos:
        print("\nAún no ha guardado ningún contacto")
    else:
        menu_filtar_contactos()
        opcion = pedir_opcion([1, 2, 3, 4])
        if opcion == 1:
            opcion_1_busqueda_de_contactos_por_nombre(mi_agenda)
        elif opcion == 2:
            buscar_contacto_por_numero(mi_agenda)
        elif opcion == 3:
            opcion_3_busqueda_de_contactos_por_etiquetas(mi_agenda)
        else:
            return


def opcion_1_busqueda_de_contactos_por_nombre(mi_agenda: Agenda):
    contacto = mi_agenda.comprobar_si_un_contacto_existe()
    if contacto:
        print(contacto)
    else:
        print("\nEl contacto no existe")


def buscar_contacto_por_numero(mi_agenda: Agenda):
    numero = pedir_telefono()
    contacto_buscado = mi_agenda.buscar_contacto_por_numero(numero)
    if contacto_buscado:
        print(contacto_buscado)
    else:
        print("\nContacto no existe")


def opcion_3_busqueda_de_contactos_por_etiquetas(mi_agenda: Agenda):
    etiqueta = pedir_etiqueta()
    lista_de_contactos_con_la_etiqueta = mi_agenda.buscar_contactos_por_etiqueta(
        etiqueta
    )
    if lista_de_contactos_con_la_etiqueta:
        for i, contacto in enumerate(lista_de_contactos_con_la_etiqueta, start=1):
            print(f"\n{i}. {contacto}")
    else:
        print("\nNo se encuentran contactos con esa etiqueta")


def gestionar_mostrar_contactos(mi_agenda: Agenda):
    if not mi_agenda.lista_de_contactos:
        print("\nAún no ha guardado ningún contacto")
    else:
        menu_mostrar_tipo_de_contacto()
        opcion = pedir_opcion([1, 2, 3, 4])

        if opcion == 1:
            mi_agenda.mostrar_agenda()
        elif opcion == 2:
            mi_agenda.mostrar_contactos_personales()
        elif opcion == 3:
            mi_agenda.mostrar_contactos_laborales()
        else:
            return


def gestionar_agregar_contactos(mi_agenda: Agenda):
    menu_tipo_de_contacto()
    opcion = pedir_opcion([1, 2, 3])
    if opcion == 3:
        return
    nombre = pedir_nombre()
    comprobar_nombre_repetido = mi_agenda.comprobar_nombre(nombre)
    if comprobar_nombre_repetido:
        print("\nYa existe un contacto con ese nombre")
        return
    telefono = pedir_telefono()
    telefono_format = formatear_numero_de_telefono(telefono)
    comprobar_telefono_repetido = mi_agenda.comprobar_telefono(telefono_format)
    if comprobar_telefono_repetido:
        print("\nYa existe un contacto con ese número de teléfono")
        return
    if opcion == 1:
        contacto = pedir_datos_del_contacto_familiar(nombre, telefono)
        mi_agenda.agregar_contacto(contacto)
        mi_agenda.guardar_json()
        print(f"\nContacto {contacto.nombre} agregado correctamente")
    elif opcion == 2:
        contacto = pedir_datos_del_contacto_laboral(nombre, telefono)
        mi_agenda.agregar_contacto(contacto)
        mi_agenda.guardar_json()
        print(f"\nContacto {contacto.nombre} agregado correctamente")


def gestionar_eliminar_contacto(mi_agenda: Agenda):
    if not mi_agenda.lista_de_contactos:
        print("\nAún no ha guardado ningún contacto")
    else:
        contacto = mi_agenda.comprobar_si_un_contacto_existe()
        if contacto is not None:
            eliminado = mi_agenda.eliminar_contactos_por_nombre(contacto)
            if eliminado:
                print(f"\nSe ha eliminado el contacto {contacto.nombre}")
                return
            else:
                print("\nRegresando al menú principal")
                return
        print("\nContacto no existe")


def gestionar_eliminar_todos_los_contactos(mi_agenda: Agenda):
    if not mi_agenda.lista_de_contactos:
        print("\nAún no ha guardado ningún contacto")
    else:
        eliminado = mi_agenda.eliminar_contactos()
        if eliminado:
            print("\nSe han eliminado todos los contactos")
        else:
            print("\nRegresando al menú principal")


def gestionar_exportacion_a_csv(mi_agenda: Agenda):
    if not mi_agenda.lista_de_contactos:
        print("\nAún no ha guardado ningún contacto")
    else:
        exportado = mi_agenda.exportar_csv()
        if exportado:
            print(
                "\nSe han exportado los datos correctamente al archivo llamado 'Agenda de contactos.csv'"
            )
        else:
            print("\nOtro programa tiene abierto el archivo .csv, ciérrelo primero.")


def pedir_datos_del_contacto_familiar(nombre, telefono):
    telefono_formateado = formatear_numero_de_telefono(telefono)
    parentesco = pedir_parentesco()
    cumpleaños = pedir_fecha_cumple()
    correo = pedir_correo_electronico()
    mi_contacto_familiar = ContactoPersonal(
        nombre, telefono_formateado, correo, cumpleaños, parentesco
    )
    return mi_contacto_familiar


def pedir_datos_del_contacto_laboral(nombre, telefono):
    telefono_formateado = formatear_numero_de_telefono(telefono)
    empresa = pedir_empresa()
    cargo = pedir_cargo()
    correo = pedir_correo_electronico()
    mi_contacto_laboral = ContactoLaboral(
        nombre, telefono_formateado, correo, empresa, cargo
    )
    return mi_contacto_laboral