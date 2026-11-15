import csv
import json
from datetime import date, datetime


class Contacto:
    def __init__(self, nombre, telefono, correo_electronico):
        self.nombre = nombre
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.etiquetas = []

    def __str__(self):
        return f"Nombre: {self.nombre} Teléfono: {self.telefono} Dirección de correo electrónica: {self.correo_electronico}"

    def añadir_etiqueta(self, contacto):
        etiqueta = pedir_etiqueta()
        contacto.etiquetas.append(etiqueta)


class ContactoPersonal(Contacto):
    def __init__(self, nombre, telefono, correo_electronico, cumpleaños, parentesco):
        super().__init__(nombre, telefono, correo_electronico)

        self.cumpleaños = cumpleaños
        self.parentesco = parentesco

    def __str__(self):
        return f"Nombre: {self.nombre}. Teléfono: {self.telefono}. Dirección de correo electrónica: {self.correo_electronico}. Fecha de cumpleaños: {self.cumpleaños}. Parentesco: {self.parentesco}. Etiquetas: {self.etiquetas}"

    def devolver_tipo(self):
        tipo = self.__class__.__name__
        return tipo

    def es_el_cumple(self):
        hoy = date.today()
        return hoy.day == self.cumpleaños.day and hoy.month == self.cumpleaños.month


class ContactoLaboral(Contacto):
    def __init__(self, nombre, telefono, correo_electronico, empresa, cargo):
        super().__init__(nombre, telefono, correo_electronico)
        self.empresa = empresa
        self.cargo = cargo

    def __str__(self):
        return f"Nombre: {self.nombre}. Teléfono: {self.telefono}. Dirección de correo electrónica: {self.correo_electronico}. Empresa: {self.empresa}. Cargo: {self.cargo}. Etiquetas: {self.etiquetas}"

    def devolver_tipo(self):
        tipo = self.__class__.__name__
        return tipo


class Agenda:
    def __init__(self):
        self.lista_de_contactos = self.descargar_datos()

    def comprobar_nombre(self, nombre):
        if any(nombre == contacto.nombre for contacto in self.lista_de_contactos):
            print("\nEse contacto ya está en la Agenda.")
            return True
        else:
            return

    def agregar_contacto(self, nuevo_contacto):
        self.lista_de_contactos.append(nuevo_contacto)
        nuevo_contacto.añadir_etiqueta(nuevo_contacto)
        print(f"\nNuevo contacto añadido: {nuevo_contacto}\n")
        return True

    def añadir_etiqueta(self, nombre):
        etiqueta = pedir_etiqueta()
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                contacto.etiquetas.append(etiqueta)

    def buscar_contacto_por_nombre(self, nombre):
        encontrado = False
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                return f"\n{contacto}"
        if not encontrado:
            print("\nContacto no existe")
            return

    def buscar_contacto_por_numero(self, telefono):
        encontrado = False
        for contacto in self.lista_de_contactos:
            if contacto.telefono == telefono:
                return f"\n{contacto}"
        if not encontrado:
            return "\nContacto no existe"

    def buscar_contactos_por_etiqueta(self, etiqueta):
        lista_con_etiquetas = []
        encontrado = False
        for contacto in self.lista_de_contactos:
            if etiqueta in contacto.etiquetas:
                lista_con_etiquetas.append(contacto)
                encontrado = True
        lista_con_etiquetas.sort(key=lambda x: x.nombre)
        for i, contacto in enumerate(lista_con_etiquetas, start=1):
            print(f"\n{i}. {contacto}")
        if not encontrado:
            print("\nNo se encuentran contactos con esa etiqueta")

    def eliminar_contacto_por_nombre(self, nombre):
        encontrado = False
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                print(f"\nSe ha eliminado el contacto {contacto.nombre}.")
                self.lista_de_contactos.remove(contacto)
                encontrado = True
                return
        if not encontrado:
            print("\nContacto no existe")

    def eliminar_contacto_por_numero(self, numero):
        encontrado = False
        for contacto in self.lista_de_contactos:
            if contacto.telefono == numero:
                encontrado = True
                self.lista_de_contactos.remove(contacto)
                print(f"\nSe ha eliminado el contacto {contacto}.")
        if not encontrado:
            return (
                f"\nNo se encontró ningún contacto con el número de teléfono {numero}."
            )

    def modificar_nombre(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                nuevo_nombre = pedir_nombre()
                print(
                    f"\nHa editado el nombre correctamente. Antes se llamaba {contacto.nombre}, ahora se llama {nuevo_nombre}"
                )
                contacto.nombre = nuevo_nombre

    def modificar_telefono(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                nuevo_numero = pedir_telefono()
                contacto.telefono = nuevo_numero
                print("Ha editado el número correctamente.")

    def modificar_correo_electronico(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                nuevo_email = pedir_correo_electronico()
                contacto.correo_electronico = nuevo_email
                print("Ha cambiado el correo electrónico correctamente.")

    def modificar_fecha_de_cumpleaños(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                nuevo_fecha_de_cumpleaños = pedir_fecha_cumple()
                contacto.cumpleaños = nuevo_fecha_de_cumpleaños
                print("Ha editado la fecha de cumpleaños correctamente.")

    def mostrar_agenda(self):
        print("\nLa lista de contactos es la siguiente: \n")
        ordenados = sorted(self.lista_de_contactos, key=lambda x: x.nombre)
        for i, contacto in enumerate(ordenados, start=1):
            print(f"\n{i}. {contacto}")

    def eliminar_todos_los_contactos(self):
        self.lista_de_contactos.clear()
        print("\nSe han eliminado todos los contactos de la agenda\n")

    def mostrar_contactos_laborales(self):
        contactos_laborales = []
        for contacto in self.lista_de_contactos:
            if contacto.devolver_tipo() == "ContactoLaboral":
                contactos_laborales.append(contacto)
        ordenados = sorted(contactos_laborales, key=lambda x: x.nombre)
        for i, contacto in enumerate(ordenados, start=1):
            print(f"\n{i}. {contacto}")

    def mostrar_contactos_personales(self):
        contactos_personales = []
        for contacto in self.lista_de_contactos:
            if contacto.devolver_tipo() == "ContactoPersonal":
                contactos_personales.append(contacto)
        ordenados = sorted(contactos_personales, key=lambda x: x.nombre)
        for i, contacto in enumerate(ordenados, start=1):
            print(f"\n{i}. {contacto}")

    def mostrar_etiquetas_de_un_contacto(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                etiquetas = contacto.etiquetas
                if etiquetas:
                    print(f"\nEtiquetas actuales de {contacto.nombre}\n")
                    for i, est in enumerate(etiquetas, start=1):
                        print(f"{i}. {est}")
                    return etiquetas, len(etiquetas)

    def comprobar_si_un_contacto_tiene_etiquetas(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                etiquetas = contacto.etiquetas
                return bool(etiquetas)

    def convertir_a_diccionario(self):
        lista_de_diccionarios = []
        for contacto in self.lista_de_contactos:
            diccionario = contacto.__dict__.copy()
            diccionario["Tipo"] = contacto.devolver_tipo()
            if isinstance(contacto, ContactoPersonal):
                diccionario["cumpleaños"] = contacto.cumpleaños.strftime("%d-%m-%Y")
            lista_de_diccionarios.append(diccionario)
        return lista_de_diccionarios

    def guardar_json(self):
        datos = self.convertir_a_diccionario()
        with open("Datos.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

    def exportar_csv(self):
        with open(
            "Agenda de contactos.csv", "w", encoding="utf-8", newline=""
        ) as archivo:
            columnas = [
                "Nombre",
                "Número de teléfono",
                "Dirección de correo electrónico",
                "Empresa",
                "Cargo",
                "Cumpleaños",
                "Parentesco",
                "Etiquetas",
            ]
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            for contacto in self.lista_de_contactos:
                etiquetas_texto = ", ".join(contacto.etiquetas)
                if isinstance(contacto, ContactoLaboral):
                    cumpleaños = "-"
                    parentesco = "-"
                else:
                    cumpleaños = contacto.cumpleaños
                    parentesco = contacto.parentesco

                if isinstance(contacto, ContactoPersonal):
                    empresa = "-"
                    cargo = "-"
                else:
                    empresa = contacto.empresa
                    cargo = contacto.cargo
                escritor.writerow(
                    {
                        "Nombre": contacto.nombre,
                        "Número de teléfono": contacto.telefono,
                        "Dirección de correo electrónico": contacto.correo_electronico,
                        "Empresa": empresa,
                        "Cargo": cargo,
                        "Cumpleaños": cumpleaños,
                        "Parentesco": parentesco,
                        "Etiquetas": etiquetas_texto,
                    }
                )
            print(
                "\nSe han exportado los datos correctamente al archivo llamado 'Agenda de contactos.csv'\n"
            )

    def descargar_datos(self):
        lista_reconstituida = []
        try:
            with open("Datos.json", "r", encoding="utf-8") as archivo:
                datos_descargados = json.load(archivo)
                for diccionario in datos_descargados:
                    nombre = diccionario["nombre"]
                    telefono = diccionario["telefono"]
                    correo = diccionario["correo_electronico"]
                    empresa = diccionario.get("empresa", "-")
                    cargo = diccionario.get("cargo", "-")
                    cumpleaños = diccionario.get("cumpleaños", "-")
                    parentesco = diccionario.get("parentesco", "-")
                    etiquetas = diccionario.get("etiquetas", [])

                    if diccionario["Tipo"] == "ContactoLaboral":
                        nuevo_contacto = ContactoLaboral(
                            nombre, telefono, correo, empresa, cargo
                        )
                        nuevo_contacto.etiquetas = etiquetas
                        lista_reconstituida.append(nuevo_contacto)
                    else:
                        fecha_del_cumpleaños = datetime.strptime(
                            cumpleaños, "%d-%m-%Y"
                        ).date()
                        nuevo_contacto_personal = ContactoPersonal(
                            nombre, telefono, correo, fecha_del_cumpleaños, parentesco
                        )
                        nuevo_contacto_personal.etiquetas = etiquetas
                        lista_reconstituida.append(nuevo_contacto_personal)
                return lista_reconstituida

        except json.JSONDecodeError:
            print("\nLos datos están corruptos. Se creará una nueva lista de contactos")
            return []
        except FileNotFoundError:
            print("\nNo existen datos previos. Se creará una nueva lista de contactos")
            return []

    def revisar_cumpleaños(self):
        hay_cumple = False
        for contacto in self.lista_de_contactos:
            if isinstance(contacto, ContactoPersonal) and contacto.es_el_cumple():
                print(
                    f"\nHoy es el cumpleaños de {contacto.nombre} Envíale felicidades !!"
                )
                hay_cumple = True
        if not hay_cumple:
            print("\nNo hay cumpleaños hoy")


def pedir_nombre():
    return input("\nNombre del contacto: ").title().strip()


def pedir_etiqueta():
    return input("\nEtiqueta para el contacto: ").strip()


def pedir_empresa():
    return input("\nNombre de la empresa: ").strip().title()


def pedir_cargo():
    return input("\nCargo que ocupa: ").strip().title()


def pedir_telefono():
    while True:
        try:
            teléfono = int(input("\nIntroduzca el número telefónico: "))
            return teléfono
        except ValueError:
            print("Solo números.")


def pedir_correo_electronico():
    while True:
        email = input("\nDirección de correo electrónico: ")
        if "@" in email:
            return email
        else:
            print("\nDirección de correo no válida. Debe contener '@'.")


def pedir_fecha_cumple():
    while True:
        fecha_str = input(
            "\nIntroduce la fecha de cumpleaños del contacto (DD-MM-AAAA): "
        )
        try:
            fecha_valida = datetime.strptime(fecha_str, "%d-%m-%Y").date()
            return fecha_valida
        except ValueError:
            print(
                "\nError: Fecha no válida. Asegúrate de usar el formato DD-MM-AA y que la fecha exista."
            )


def pedir_parentesco():
    while True:
        parentesco = input("\nParentesco del contacto: ").strip()
        solo_letras = parentesco.replace(" ", "").isalpha()
        if solo_letras:
            return parentesco
        else:
            print("\nNo puede introducir números o caracteres especiales aquí\n")


def menu():
    print("\n____MENU____\n")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Eliminar todos los contactos")
    print("6. Exportar datos a Excel")
    print("7. Salir")


def menu_tipo_de_contacto():
    print("\n____AÑADIR CONTACTO_____\n")
    print("1. Contacto familiar")
    print("2. Contacto laboral")


def menu_mostrar_tipo_de_contacto():
    print("\n____Mostrar contactos_____\n")
    print("1. Todos los contactos")
    print("2. Contactos familiares")
    print("3. Contactos laborales")


def menu_filtar_contactos():
    print("\n____Buscar contactos____\n")
    print("1. Buscar por nombre")
    print("2. Buscar por número de teléfono")
    print("3. Buscar por etiqueta")


def menu_eliminar_contacto():
    print("\n____Eliminar contacto_____\n")
    print("1. Eliminar por nombre")
    print("2. Eliminar por número de teléfono")


def menu_editar():
    print("\n____MENÚ_____\n")
    print("1. Editar contacto")
    print("2. Regresar al menú principal")


def menu_editar_por():
    print("\n____Editar contacto_____\n")
    print("1. Editar nombre")
    print("2. Editar número de teléfono")
    print("3. Editar correo electrónico")
    print("4. Editar fecha de cumpleaños")
    print("5. Editar etiquetas")


def menu_editar_etiquetas():
    print("\n____Editar etiquetas_____\n")
    print("1. Añadir etiqueta")
    print("2. Eliminar etiqueta")


def menu_añadir_etiquetas():
    print("\n____Editar etiquetas_____\n")
    print("1. Añadir etiqueta")


def pedir_opcion(opciones):
    while True:
        try:
            opcion = int(input("\nOpción: "))
            if opcion in opciones:
                return opcion
            else:
                print("\nOpción no válida")
        except ValueError:
            print("\nIntroduza un número válido")


def formatear_numero_de_telefono(telefono):
    str_telefono = str(telefono)
    if len(str_telefono) == 8:
        return f"+53 {str_telefono[:1]}-{str_telefono[1:4]}-{str_telefono[4:]}"
    else:
        return telefono


def programa():
    print("\nBienvenido a su agenda de contactos")
    mi_agenda = Agenda()
    if mi_agenda.lista_de_contactos:
        print("\nDatos cargados correctamente")
    while True:
        menu()
        opcion = pedir_opcion([1, 2, 3, 4, 5, 6, 7])
        match opcion:
            case 1:
                menu_tipo_de_contacto()
                seleccion = pedir_opcion([1, 2])
                nombre = pedir_nombre()
                resultado = mi_agenda.comprobar_nombre(nombre)
                if resultado:
                    continue

                telefono = pedir_telefono()
                telefono_formateado = formatear_numero_de_telefono(telefono)
                correo = pedir_correo_electronico()

                if seleccion == 1:
                    parentesco = pedir_parentesco()
                    cumpleaños = pedir_fecha_cumple()
                    mi_contacto = ContactoPersonal(
                        nombre, telefono_formateado, correo, cumpleaños, parentesco
                    )
                    print(f"\nContacto {mi_contacto.nombre} agregado correctamente")

                else:
                    empresa = pedir_empresa()
                    cargo = pedir_cargo()
                    mi_contacto = ContactoLaboral(
                        nombre, telefono_formateado, correo, empresa, cargo
                    )
                    print(f"\nContacto {mi_contacto.nombre} agregado correctamente")

                mi_agenda.agregar_contacto(mi_contacto)
                if mi_agenda.agregar_contacto:
                    mi_agenda.guardar_json()

            case 2:
                if not mi_agenda.lista_de_contactos:
                    print("\nAún no ha guardado ningún contacto")
                else:
                    menu_mostrar_tipo_de_contacto()
                    opcion = pedir_opcion([1, 2, 3])
                    if opcion == 1:
                        mi_agenda.mostrar_agenda()
                    elif opcion == 2:
                        mi_agenda.mostrar_contactos_personales()
                    else:
                        mi_agenda.mostrar_contactos_laborales()
            case 3:
                if not mi_agenda.lista_de_contactos:
                    print("\nAún no ha guardado ningún contacto")
                else:
                    menu_filtar_contactos()
                    opcion = pedir_opcion([1, 2, 3])
                    if opcion == 1:
                        nombre = pedir_nombre()
                        contacto_buscado = mi_agenda.buscar_contacto_por_nombre(nombre)
                        if contacto_buscado:
                            print(contacto_buscado)
                            menu_editar()
                            opcion = pedir_opcion([1, 2])
                            if opcion == 2:
                                continue
                            menu_editar_por()
                            opcion = pedir_opcion([1, 2, 3, 4, 5])
                            match opcion:
                                case 1:
                                    mi_agenda.modificar_nombre(nombre)
                                    mi_agenda.guardar_json()
                                case 2:
                                    mi_agenda.modificar_telefono(nombre)
                                    mi_agenda.guardar_json()
                                case 3:
                                    mi_agenda.modificar_correo_electronico(nombre)
                                    mi_agenda.guardar_json()
                                case 4:
                                    mi_agenda.modificar_fecha_de_cumpleaños(nombre)
                                    mi_agenda.guardar_json()
                                case 5:
                                    tiene_etiquetas = mi_agenda.comprobar_si_un_contacto_tiene_etiquetas(
                                        nombre
                                    )
                                    if tiene_etiquetas:
                                        lista, cantidad_de_etiquetas = (
                                            mi_agenda.mostrar_etiquetas_de_un_contacto(
                                                nombre
                                            )
                                        ) # type: ignore
                                        menu_editar_etiquetas()
                                        opcion = pedir_opcion([1, 2])
                                        if opcion == 1:
                                            mi_agenda.añadir_etiqueta(nombre)
                                            mi_agenda.guardar_json()
                                            print(
                                                f"\nSe ha añadido la etiqueta al contacto {nombre}"
                                            )
                                            mi_agenda.mostrar_etiquetas_de_un_contacto(
                                                nombre
                                            )
                                            continue

                                        else:
                                            print("\nSeleccione la etiqueta a eliminar")
                                            mi_agenda.mostrar_etiquetas_de_un_contacto(
                                                nombre
                                            )
                                            opcion = pedir_opcion(
                                                range(1, cantidad_de_etiquetas + 1)
                                            )
                                            eliminado = lista.pop(opcion - 1)
                                            mi_agenda.guardar_json()
                                            print(
                                                f"\nHa eliminado la etiqueta '{eliminado}' del contacto {nombre}"
                                            )
                                            continue
                                    print(f"\n{nombre} no tiene etiquetas actualmente.")
                                    menu_añadir_etiquetas()
                                    opcion = pedir_opcion([1])
                                    if opcion == 1:
                                        mi_agenda.añadir_etiqueta(nombre)
                                        mi_agenda.guardar_json()
                                        print(
                                            f"\nSe ha añadido la etiqueta al contacto {nombre}"
                                        )
                                        mi_agenda.mostrar_etiquetas_de_un_contacto(
                                            nombre
                                        )

                    elif opcion == 2:
                        telefono = pedir_telefono()
                        print(mi_agenda.buscar_contacto_por_numero(telefono))
                    else:
                        etiqueta = pedir_etiqueta()
                        mi_agenda.buscar_contactos_por_etiqueta(etiqueta)
            case 4:
                if not mi_agenda.lista_de_contactos:
                    print("\nAún no ha guardado ningún contacto")
                else:
                    menu_eliminar_contacto()
                    opcion = pedir_opcion([1, 2])
                    if opcion == 1:
                        nombre = pedir_nombre()
                        mi_agenda.eliminar_contacto_por_nombre(nombre)

                    else:
                        numero = pedir_telefono()
                        mi_agenda.eliminar_contacto_por_numero(numero)
                    mi_agenda.guardar_json()

            case 5:
                if not mi_agenda.lista_de_contactos:
                    print("\nAún no ha guardado ningún contacto")
                else:
                    mi_agenda.eliminar_todos_los_contactos()
                    mi_agenda.guardar_json()

            case 6:
                if not mi_agenda.lista_de_contactos:
                    print("\nAún no ha guardado ningún contacto")
                else:
                    mi_agenda.exportar_csv()

            case 7:
                return


def main():
    programa()
    print("\nHa salido satisfactoriamente del programa.\n")


if __name__ == "__main__":
    main()
