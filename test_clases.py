import pytest
from clases import Agenda, Contacto

def test_buscar_contacto_por_nombre_si_existe():
    mi_agenda = Agenda
    contacto_juan = Contacto("Juan", "1234", "ksks@.")
    mi_agenda.lista_de_contactos = [contacto_juan]
    
    resultado = mi_agenda.buscar_contacto_por_nombre("juan")
    