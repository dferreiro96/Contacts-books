from Agenda_de_contactos import pedir_opcion
lista = [1,2,3,4,5]
print(len(lista))
opcion = pedir_opcion(range(1, len(lista)+1))
lista.remove(opcion)
print(lista)