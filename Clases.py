import csv
import json
import shutil
from datetime import date, datetime

from utilidades import (
    confirmacion_borrar_contactos,
    formatear_numero_de_telefono,
    pedir_etiqueta,
    pedir_fecha_cumple,
    pedir_opcion_añadir_etiqueta,
)


class Contacto:
    def __init__(self, nombre, telefono, correo_electronico):
        self.nombre = nombre
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.etiquetas = []

    def __str__(self):
        return f"Nombre: {self.nombre} Teléfono: {self.telefono} Dirección de correo electrónica: {self.correo_electronico}"

    def devolver_tipo(self):
        tipo = self.__class__.__name__
        return tipo

    def añadir_etiqueta(self):
        etiqueta = pedir_etiqueta()
        self.etiquetas.append(etiqueta)


class ContactoPersonal(Contacto):
    def __init__(self, nombre, telefono, correo_electronico, cumpleaños, parentesco):
        super().__init__(nombre, telefono, correo_electronico)

        self.cumpleaños = cumpleaños
        self.parentesco = parentesco

    def __str__(self):
        cumpleaños_formateado = self.cumpleaños.strftime("%d/%m")
        etiquetas_formateadas = (
            ", ".join(self.etiquetas) if self.etiquetas else "Ninguna"
        )
        return f"Nombre: {self.nombre}. Teléfono: {self.telefono}. Dirección de correo electrónica: {self.correo_electronico}. Fecha de cumpleaños: {cumpleaños_formateado}. Parentesco: {self.parentesco}. Etiquetas: {etiquetas_formateadas}"

    def es_el_cumple(self):
        hoy = date.today()
        return hoy.day == self.cumpleaños.day and hoy.month == self.cumpleaños.month


class ContactoLaboral(Contacto):
    def __init__(self, nombre, telefono, correo_electronico, empresa, cargo):
        super().__init__(nombre, telefono, correo_electronico)
        self.empresa = empresa
        self.cargo = cargo

    def __str__(self):
        etiquetas_formateadas = (
            ", ".join(self.etiquetas) if self.etiquetas else "Ninguna"
        )
        return f"Nombre: {self.nombre}. Teléfono: {self.telefono}. Dirección de correo electrónica: {self.correo_electronico}. Empresa: {self.empresa}. Cargo: {self.cargo}. Etiquetas: {etiquetas_formateadas}"


class Agenda:
    def __init__(self):
        self.lista_de_contactos = self.descargar_datos()

    def comprobar_si_un_contacto_existe(self, nombre):
        for c in self.lista_de_contactos:
            if c.nombre == nombre:
                return c

    def comprobar_nombre(self, nombre):
        return bool(
            any(nombre == contacto.nombre for contacto in self.lista_de_contactos)
        )

    def comprobar_telefono(self, telefono):
        return bool(
            any(telefono == contacto.telefono for contacto in self.lista_de_contactos)
        )

    def comprobar_correo(self, correo):
        return bool(
            any(
                correo == contacto.correo_electronico
                for contacto in self.lista_de_contactos
            )
        )

    def agregar_contacto(self, contacto: Contacto):
        self.lista_de_contactos.append(contacto)
        retorno = pedir_opcion_añadir_etiqueta()
        if retorno:
          contacto.añadir_etiqueta()
          self.guardar_json()


    def añadir_etiqueta(self, nombre, etiqueta):
        for c in self.lista_de_contactos:
            if c.nombre == nombre:
                c.etiquetas.append(etiqueta)
                self.guardar_json()
                return True
        return False

    def comprobar_si_un_contacto_tiene_etiqueta_en_especifico(self, nombre, etiqueta):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre and etiqueta in contacto.etiquetas:
                return True
        return False

    def buscar_contacto_por_nombre(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                return contacto
        return None

    def buscar_contacto_por_numero(self, telefono):
        str_telefono = str(telefono)
        if len(str_telefono) == 8:
            telefono_formateado = (
                f"+53 {str_telefono[:1]}-{str_telefono[1:4]}-{str_telefono[4:]}"
            )
        else:
            telefono_formateado = str(telefono)

        for contacto in self.lista_de_contactos:
            if contacto.telefono == telefono_formateado:
                return contacto
        return None

    def buscar_contactos_por_etiqueta(self, etiqueta):
        lista_con_etiquetas = []
        for contacto in self.lista_de_contactos:
            if etiqueta in contacto.etiquetas:
                lista_con_etiquetas.append(contacto)
        lista_con_etiquetas.sort(key=lambda x: x.nombre)
        return lista_con_etiquetas if lista_con_etiquetas else None

    def eliminar_contactos(self):
        retorno = confirmacion_borrar_contactos(
            "\n¿Está seguro que desea eliminar TODOS los contactos (s/n)?: "
        )
        if retorno:
            self.eliminar_todos_los_contactos()
            self.guardar_json()
            return True
        return False

    def eliminar_contactos_por_nombre(self, contacto):
        retorno = confirmacion_borrar_contactos(
            "\n¿Está seguro que desea eliminar el contacto (s/n)?: "
        )
        if retorno:
            self.lista_de_contactos.remove(contacto)
            self.guardar_json()
            return True
        return False

    def modificar_nombre(self, contacto, nuevo_nombre):
        repetido = self.comprobar_nombre(nuevo_nombre)
        if not repetido:
            contacto.nombre = nuevo_nombre
            self.guardar_json()
            return True
        return False

    def modificar_telefono(self, contacto, nuevo_numero):
        nuevo_numero_formateado = formatear_numero_de_telefono(nuevo_numero)
        repetido = self.comprobar_telefono(nuevo_numero_formateado)
        if not repetido:
            contacto.telefono = nuevo_numero_formateado
            self.guardar_json()
            return True
        return False

    def modificar_correo_electronico(self, contacto, nuevo_email):
        repetido = self.comprobar_correo(nuevo_email)
        if not repetido:
            contacto.correo_electronico = nuevo_email
            self.guardar_json()
            return True
        return False

    def modificar_fecha_de_cumpleaños(self, nombre):
        for contacto in self.lista_de_contactos:
            if isinstance(contacto, ContactoPersonal) and contacto.nombre == nombre:
                nuevo_fecha_de_cumpleaños = pedir_fecha_cumple()
                contacto.cumpleaños = nuevo_fecha_de_cumpleaños
                self.guardar_json()
                return True
        return False

    def mostrar_agenda(self):
        print("\nLa lista de contactos es la siguiente: \n")
        ordenados = sorted(self.lista_de_contactos, key=lambda x: x.nombre)
        for i, contacto in enumerate(ordenados, start=1):
            print(f"\n{i}. {contacto}")

    def eliminar_todos_los_contactos(self):
        self.lista_de_contactos.clear()

    def mostrar_contactos_laborales(self):
        contactos_laborales = []
        encontrado = False
        for contacto in self.lista_de_contactos:
            if isinstance(contacto, ContactoLaboral):
                encontrado = True
                contactos_laborales.append(contacto)
        if encontrado:
            ordenados = sorted(contactos_laborales, key=lambda x: x.nombre)
            print("\nLista de contactos laborales: ")
            for i, contacto in enumerate(ordenados, start=1):
                print(f"\n{i}. {contacto}")
        else:
            print("\nNo se encontraron contactos laborales")

    def mostrar_contactos_personales(self):
        encontrado = False
        contactos_personales = []
        for contacto in self.lista_de_contactos:
            if isinstance(contacto, ContactoPersonal):
                encontrado = True
                contactos_personales.append(contacto)
        if encontrado:
            ordenados = sorted(contactos_personales, key=lambda x: x.nombre)
            print("\nLista de contactos familiares: ")
            for i, contacto in enumerate(ordenados, start=1):
                print(f"\n{i}. {contacto}")
        else:
            print("\nNo se encontraron contactos familiares")

    def mostrar_etiquetas_de_un_contacto(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                etiquetas = contacto.etiquetas
                for i, est in enumerate(etiquetas, start=1):
                    print(f"{i}. {est}")
                return etiquetas, len(etiquetas)

    def comprobar_si_un_contacto_tiene_etiquetas(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre and contacto.etiquetas:
                etiquetas = contacto.etiquetas
                return etiquetas

    def convertir_a_diccionario(self):
        lista_de_diccionarios = []
        for contacto in self.lista_de_contactos:
            diccionario = contacto.__dict__.copy()
            diccionario["Tipo"] = contacto.devolver_tipo()
            if isinstance(contacto, ContactoPersonal):
                diccionario["cumpleaños"] = contacto.cumpleaños.strftime("%d/%m")
            lista_de_diccionarios.append(diccionario)
        return lista_de_diccionarios

    def guardar_json(self):
        datos = self.convertir_a_diccionario()
        with open("Datos.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

    def exportar_csv(self):
        try:
            with open(
                "Agenda de contactos.csv", "w", encoding="utf-8-sig", newline=""
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
                        cumpleaños = contacto.cumpleaños.strftime("%d/%m")
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
                return True
        except PermissionError:
            return False

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
                            cumpleaños + "/2000", "%d/%m/%Y"
                        ).date()
                        nuevo_contacto_personal = ContactoPersonal(
                            nombre, telefono, correo, fecha_del_cumpleaños, parentesco
                        )
                        nuevo_contacto_personal.etiquetas = etiquetas
                        lista_reconstituida.append(nuevo_contacto_personal)
                return lista_reconstituida

        except (KeyError, TypeError, ValueError):
            shutil.copy("Datos.json", "Datos.back")
            print(
                "\nLos datos están corruptos. Se guardó una copia de seguridad en Datos.back"
            )
            return []
        except FileNotFoundError:
            print("\nNo existen datos previos. Se creará una nueva lista de contactos")
            return []

    def revisar_cumpleaños(self):
        for contacto in self.lista_de_contactos:
            if isinstance(contacto, ContactoPersonal) and contacto.es_el_cumple():
                print(
                    f"\nHoy es el cumpleaños de {contacto.nombre}. Envíale felicidades !!"
                )