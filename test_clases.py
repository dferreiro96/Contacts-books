from datetime import date

import pytest

from clases import Agenda, Contacto, ContactoLaboral, ContactoPersonal


@pytest.fixture
def agenda_de_prueba():
    mi_agenda = Agenda()
    ana = ContactoLaboral("Ana", "123", "ewrf@.", "ergv", "ergf")
    pedro = ContactoPersonal("Pedro", "34456", "ertvg@.", "02/05/2000", "primo")
    mi_agenda.lista_de_contactos.extend([ana, pedro])
    return mi_agenda

@pytest.fixture
def contacto_de_prueba1():
    c = ContactoPersonal("Ana", "1234", "dfsg@.", date.today(), "prima")
    return c

@pytest.fixture
def contacto_de_prueba2():
    d = ContactoPersonal("Pedro", "1234", "dfsg@.", "04/08/2000", "primo")
    return d
    
      
def test_buscar_contacto_por_nombre_si_existe(agenda_de_prueba):
    assert agenda_de_prueba.buscar_contacto_por_nombre("Ana") is not None
    assert agenda_de_prueba.buscar_contacto_por_nombre("Juan") is None
    
def test_cumple_de_hoy(contacto_de_prueba1, contacto_de_prueba2):
    assert contacto_de_prueba1.es_el_cumple() == True
    assert contacto_de_prueba2.es_el_cumple() == False
    
def test_comprobar_si_un_contacto_existe():
    