from clases import Agenda
from logica import (
    gestionar_agregar_contactos,
    gestionar_busqueda_de_contactos,
    gestionar_edicion_de_contactos,
    gestionar_eliminar_contacto,
    gestionar_eliminar_todos_los_contactos,
    gestionar_exportacion_a_csv,
    gestionar_mostrar_contactos,
)
from menus import menu
from utilidades import pedir_opcion


def main():
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
                    break
        print("\nHa salido satisfactoriamente del programa.\n")
                
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
            



if __name__ == "__main__":
    main()
