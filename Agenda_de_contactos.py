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
        etiquetas_formateadas = (", ".join(self.etiquetas) if self.etiquetas else "Ninguna")
        return f"Nombre: {self.nombre}. Teléfono: {self.telefono}. Dirección de correo electrónica: {self.correo_electronico}. Empresa: {self.empresa}. Cargo: {self.cargo}. Etiquetas: {etiquetas_formateadas}"

    def devolver_tipo(self):
        tipo = self.__class__.__name__
        return tipo


class Agenda:
    def __init__(self):
        self.lista_de_contactos = self.descargar_datos()

    def comprobar_si_un_contacto_existe(self, nombre):
        for c in self.lista_de_contactos:
            if c.nombre == nombre:
                return c
            
        

    def comprobar_nombre(self, nombre):
        return bool(any(nombre == contacto.nombre for contacto in self.lista_de_contactos))

    def comprobar_telefono(self, telefono):
        return bool(any(telefono == contacto.telefono for contacto in self.lista_de_contactos))
    
    def comprobar_correo(self, correo):
        return bool(any(correo == contacto.correo_electronico for contacto in self.lista_de_contactos))
    
    def agregar_contacto(self, nuevo_contacto: Contacto):
        self.lista_de_contactos.append(nuevo_contacto)
        nuevo_contacto.añadir_etiqueta()
        print(f"\nNuevo contacto añadido: {nuevo_contacto}\n")
        return True

    def añadir_etiqueta(self, nombre, etiqueta):
        for c in self.lista_de_contactos:
            if c.nombre == nombre:
                c.etiquetas.append(etiqueta)
                self.guardar_json()


    def comprobar_si_un_contacto_tiene_etiqueta_en_especifico(self, nombre, etiqueta):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre and etiqueta in contacto.etiquetas:
                return bool

    def buscar_contacto_por_nombre(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                return contacto

    def buscar_contacto_por_numero(self, telefono):
        str_telefono = str(telefono)
        if len(str_telefono) == 8:
            telefono_formateado = (
                f"+53 {str_telefono[:1]}-{str_telefono[1:4]}-{str_telefono[4:]}"
            )
        else:
            telefono_formateado = telefono
            
        for contacto in self.lista_de_contactos:
            if contacto.telefono == telefono_formateado:
                return f"\n{contacto}"
        return False

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

    def eliminar_contactos(self):
        retorno = confirmacion_borrar_contactos("\n¿Está seguro que desea eliminar TODOS los contactos (s/n)?: ")
        if retorno:
            self.eliminar_todos_los_contactos()
            self.guardar_json()
            return bool


    def eliminar_contactos_por_nombre(self, contacto):
        retorno = confirmacion_borrar_contactos("\n¿Está seguro que desea eliminar el contacto (s/n)?: ")
        if retorno:
            self.lista_de_contactos.remove(contacto)
            self.guardar_json()
            return bool
                
    
    def modificar_nombre(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                nuevo_nombre = pedir_nombre()
                repetido = self.comprobar_nombre(nuevo_nombre)
                if not repetido:
                    contacto.nombre = nuevo_nombre
                    self.guardar_json()
                    return nuevo_nombre

    def modificar_telefono(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                nuevo_numero = pedir_telefono()
                nuevo_numero_formateado = formatear_numero_de_telefono(nuevo_numero)
                repetido = self.comprobar_telefono(nuevo_numero_formateado)
                if not repetido:
                    contacto.telefono = nuevo_numero_formateado
                    self.guardar_json()
                    return bool

    def modificar_correo_electronico(self, nombre):
        for contacto in self.lista_de_contactos:
            if contacto.nombre == nombre:
                nuevo_email = pedir_correo_electronico()
                repetido = self.comprobar_correo(nuevo_email)
                if not repetido:
                    contacto.correo_electronico = nuevo_email
                    self.guardar_json()
                    return bool

    def modificar_fecha_de_cumpleaños(self, nombre):
        for contacto in self.lista_de_contactos:
            if isinstance(contacto, ContactoPersonal) and contacto.nombre == nombre:               
                    nuevo_fecha_de_cumpleaños = pedir_fecha_cumple()
                    contacto.cumpleaños = nuevo_fecha_de_cumpleaños
                    self.guardar_json()
                    return bool


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
            if contacto.devolver_tipo() == "ContactoLaboral":
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
            if contacto.devolver_tipo() == "ContactoPersonal":
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
                return bool(etiquetas)
            
   
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

        except json.JSONDecodeError:
            print("\nLos datos están corruptos. Se creará una nueva lista de contactos")
            return []
        except FileNotFoundError, KeyError, TypeError:
            print("\nNo existen datos previos. Se creará una nueva lista de contactos")
            return []

    def revisar_cumpleaños(self):
        for contacto in self.lista_de_contactos:
            if isinstance(contacto, ContactoPersonal) and contacto.es_el_cumple():
                print(
                    f"\nHoy es el cumpleaños de {contacto.nombre}. Envíale felicidades !!"
                )

def confirmacion_borrar_contactos(mensaje):
            while True:
                seguro = (
                    input(mensaje)
                    .strip()
                    .lower()
                )
                if seguro in ("s", "si", "sí"):
                    return True
                elif seguro in ("n", "no"):
                    return False
                else:
                    print("\nNo válido")


def editar_etiquetas(mi_agenda: Agenda, nombre):
    etiqueta = pedir_etiqueta()
    resultado = mi_agenda.comprobar_si_un_contacto_tiene_etiqueta_en_especifico(nombre, etiqueta)
    if resultado:
        print("\nEl contacto ya tiene esa etiqueta")
        return
    mi_agenda.añadir_etiqueta(nombre, etiqueta)
    print(f"\nSe ha añadido la etiqueta al contacto {nombre}")
    print("\nEtiquetas del contacto\n")
    mi_agenda.mostrar_etiquetas_de_un_contacto(nombre)

def tiene_etiquetas(mi_agenda: Agenda, nombre):
    print(f"\nEtiquetas actuales de {nombre}\n")
    mi_agenda.mostrar_etiquetas_de_un_contacto(nombre)
    if mi_agenda.mostrar_etiquetas_de_un_contacto(nombre) is not None:
        menu_editar_etiquetas()
        opcion = pedir_opcion([1, 2])
        if opcion == 1:
            editar_etiquetas(mi_agenda, nombre)               
        else:
            eliminar_etiquetas(mi_agenda, nombre)
            
def no_tiene_etiquetas(mi_agenda: Agenda, nombre):
    print(f"\n{nombre} no tiene etiquetas actualmente." )
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
    print(
        f"\nHa eliminado la etiqueta '{eliminado}' del contacto {nombre}"
    )
    print(f"\nEtiquetas actuales de {nombre}\n")
    mi_agenda.mostrar_etiquetas_de_un_contacto(
        nombre
    )

def pedir_nombre():
    return input("\nNombre del contacto: ").title().strip()


def pedir_etiqueta():
    return input("\nEtiqueta para el contacto: ").strip()


def pedir_empresa():
    return input("\nNombre de la empresa: ").strip()


def pedir_cargo():
    return input("\nCargo que ocupa: ").strip()


def pedir_telefono():
    while True:
        teléfono = (
            input("\nIntroduzca el número telefónico: ")
            .strip()
            .replace(" ", "")
            .replace("-", "")
        )
        if not teléfono.isdigit():
            print("\nSolo números")
            continue
        return teléfono


def pedir_correo_electronico():
    while True:
        email = input("\nDirección de correo electrónico: ")
        if "@" in email and "." in email.split("@")[-1]:
            return email
        else:
            print(
                "\nDirección de correo no válida. Debe contener '@' y un dominio válido."
            )


def pedir_fecha_cumple():
    while True:
        fecha_str = input("\nIntroduce la fecha de cumpleaños del contacto (DD/MM): ")

        try:
            fecha_valida = datetime.strptime(fecha_str + "/2000", "%d/%m/%Y").date()
            return fecha_valida
        except ValueError:
            print(
                "\nError: Fecha no válida. Asegúrate de usar el formato DD/MM/AA y que la fecha exista."
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
    print("4. Editar contacto")    
    print("5. Eliminar contacto")
    print("6. Eliminar todos los contactos")
    print("7. Exportar datos a Excel")
    print("8. Salir")


def menu_tipo_de_contacto():
    print("\n____AÑADIR CONTACTO_____\n")
    print("1. Contacto familiar")
    print("2. Contacto laboral")
    print("3. Salir")


def menu_mostrar_tipo_de_contacto():
    print("\n____Mostrar contactos_____\n")
    print("1. Todos los contactos")
    print("2. Contactos familiares")
    print("3. Contactos laborales")
    print("4. Salir")


def menu_filtar_contactos():
    print("\n____Buscar contactos____\n")
    print("1. Buscar por nombre")
    print("2. Buscar por número de teléfono")
    print("3. Buscar por etiqueta")
    print("4. Salir")


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
    print("6. Salir")


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

def modificar_correo(mi_agenda: Agenda, nombre):
    nuevo_correo = mi_agenda.modificar_correo_electronico(nombre)
    if nuevo_correo:
        print("\nHa editado la dirección de correo electrónico correctamente.")
    else:
        print("\nYa existe un contacto con esa dirección de correo electrónico")
    
def modificar_nombre(mi_agenda: Agenda, nombre):
    nuevo_nombre = mi_agenda.modificar_nombre(nombre)
    if nuevo_nombre is not None:
        print(f"\nHa editado el nombre correctamente, ahora se llama {nuevo_nombre}")
    else:
        print("\nYa existe un contacto con ese nombre")
        
def modificar_telefono(mi_agenda: Agenda, nombre):
    nuevo_telefono = mi_agenda.modificar_telefono(nombre)
    if nuevo_telefono:
        print("\nHa editado el número de teléfono correctamente.")
    else:
        print("\nYa existe un contacto con ese número de teléfono")

def modificar_etiquetas(mi_agenda: Agenda, nombre):
    tiene_etiqueta = mi_agenda.comprobar_si_un_contacto_tiene_etiquetas(nombre )
    if tiene_etiqueta:
        tiene_etiquetas(mi_agenda, nombre)
    no_tiene_etiquetas(mi_agenda, nombre)
        
        
def gestionar_edicion_de_contactos(mi_agenda: Agenda):  
    nombre = buscar_contacto_por_nombre(mi_agenda)
    if nombre is not None:
        menu_editar_por()
        opcion = pedir_opcion([1, 2, 3, 4, 5, 6])
        match opcion:
            case 1:
                modificar_nombre(mi_agenda, nombre)
            case 2:
                modificar_telefono(mi_agenda, nombre)
            case 3:
                modificar_correo(mi_agenda, nombre)
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
           contacto = buscar_contacto_por_nombre(mi_agenda) 
           if contacto:
               print(contacto)
           else:
               print("\nEl contacto no existe")             
        elif opcion == 2:
            buscar_contacto_por_numero(mi_agenda)
        elif opcion == 3:
            etiqueta = pedir_etiqueta()
            mi_agenda.buscar_contactos_por_etiqueta(etiqueta)
        else:
            return
        
def buscar_contacto_por_numero(mi_agenda: Agenda):
    numero = pedir_telefono()
    contacto_buscado = mi_agenda.buscar_contacto_por_numero(
        numero
    )
    if contacto_buscado:
        print(contacto_buscado)
    else:
        print("\nContacto no existe")
                    
def buscar_contacto_por_nombre(mi_agenda: Agenda):
    nombre = pedir_nombre()
    contacto_buscado = mi_agenda.buscar_contacto_por_nombre(
        nombre
    )
    if contacto_buscado is not None:
        return contacto_buscado.nombre

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
    nombre = pedir_nombre()
    comprobar_nombre_repetido = mi_agenda.comprobar_nombre(nombre)
    if comprobar_nombre_repetido:
        print("\nYa existe un contacto con ese nombre")
        return
    telefono = pedir_telefono()
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
    else:
        return       

def gestionar_eliminar_contacto(mi_agenda: Agenda):
    if not mi_agenda.lista_de_contactos:
        print("\nAún no ha guardado ningún contacto")
    else:
        nombre = pedir_nombre()
        contacto = mi_agenda.comprobar_si_un_contacto_existe(nombre)
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
            print( "\nSe han exportado los datos correctamente al archivo llamado 'Agenda de contactos.csv'" )
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

    
def programa():
    mi_agenda = None
    try:
        print("\nBienvenido a su agenda de contactos")
        mi_agenda = Agenda()
        if mi_agenda.lista_de_contactos:
            print("\nDatos cargados correctamente")
            mi_agenda.revisar_cumpleaños()
        while True:
            menu()
            opcion = pedir_opcion([1, 2, 3, 4, 5, 6, 7, 8])
            match opcion:
                case 1:
                    gestionar_agregar_contactos(mi_agenda)
                case 2:
                    gestionar_mostrar_contactos(mi_agenda)
                case 3:
                    gestionar_busqueda_de_contactos(mi_agenda)
                case 4:
                    gestionar_edicion_de_contactos(mi_agenda)
                case 5:
                   gestionar_eliminar_contacto(mi_agenda)
                case 6:
                    gestionar_eliminar_todos_los_contactos(mi_agenda)   
                case 7:
                    gestionar_exportacion_a_csv(mi_agenda)
                case 8:
                    return
    except KeyboardInterrupt:
        print("\nSaliendo de emergencia por orden del usuario. \nGuardando datos")
        if mi_agenda is not None:
            mi_agenda.guardar_json()
            print("\nDatos guardados")
        else:
            print("No se pudo guardar porque la agenda no llegó a iniciarse.")
            
    except Exception as e:
        print(f"\n[!] Ocurrió un error inesperado: {e}")
        if mi_agenda is not None:
            print("Guardando datos...")
            mi_agenda.guardar_json()
            print("Datos guardados")
        else:
            print("No se pudo guardar porque la agenda no llegó a iniciarse.")
def main():
    programa()
    print("\nHa salido satisfactoriamente del programa.\n")


if __name__ == "__main__":
    main()
