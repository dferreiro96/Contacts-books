#agenda de contactos. pedir nombres y telefonos hasta que el usuario escriba "fin"
# Guardar en diccionario y mostrar al final.
#Funciones a añadir: agregar_contacto, buscar_contacto, eliminar_contacto, mostrar_agenda
#main() con menú

def agregar_contacto():
    
jugar = True
while jugar:
    dicc={}
    print("\nEsta es una agenda de contactos. Binvenido")
    while True:
        try:
            total_de_contactos= int(input("\nCuántos contactos desea guardar?: "))
        except ValueError:
            print("Introduzca un número")
            continue
        if total_de_contactos <1:
            print("Debe introducir un número mayor de 1")
            continue
        break

    for i in range (1, total_de_contactos+1):
        nombre=input(f"\nIntroduzca el nombre número {i} o la palabra 'fin' para salir del programa: ").strip() .title()
        if nombre== "Fin":
            print("\nHa salido del programa.")
            jugar= False
            break
        else:
            teléfono= input("Introduzca el número telefónico: ")
            dicc[nombre]= teléfono
            
    if dicc=={}:
        jugar= False
        break
        
    print("\n\tSu agenda es la siguiente: ")
    print()
    for i, (nombre, teléfono) in enumerate (dicc.items(), start=1):
        print(f"{i}. {nombre}: {teléfono}")
    
    
    # Preguntar si quiere repetir
    while True:
        s = input("\n¿Crear otra agenda? (s/n): ").lower().strip()
        if s in ("s", "si", "sí"):
            break
        elif s in ("n", "no"):
            print("Hasta pronto")
            jugar = False
            
        else:
            print("Carácter inválido")