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
                "\nError: Fecha no válida. Asegúrate de usar el formato DD/MM y que la fecha exista."
            )


def pedir_parentesco():
    while True:
        parentesco = input("\nParentesco del contacto: ").strip()
        solo_letras = parentesco.replace(" ", "").isalpha()
        if solo_letras:
            return parentesco
        else:
            print("\nNo puede introducir números o caracteres especiales aquí\n")

def pedir_opcion_añadir_etiqueta():
    while True:
        añadir_etiqueta = (
            input("\nDesea añadir una etiqueta al contacto (s/n)?: ")
            .lower()
            .strip()
        )
        if añadir_etiqueta in ("s", "si", "sí"):  
            return True
        elif añadir_etiqueta in ("no", "n"):
            return False
        else:
            print("\nOpción inválida")