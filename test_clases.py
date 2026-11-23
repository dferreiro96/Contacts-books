from datetime import date, datetime

import pytest

from clases import Agenda, Contacto, ContactoLaboral, ContactoPersonal


@pytest.fixture
def agenda_de_prueba(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    mi_agenda = Agenda()
    fecha_valida = datetime.strptime("04/06/2000", "%d/%m/%Y").date()
    ana = ContactoLaboral("Ana", "123", "ewrf@.", "ergv", "ergf")
    pedro = ContactoPersonal("Pedro", "34456", "ertvg@.", fecha_valida, "primo")
    mi_agenda.lista_de_contactos.extend([ana, pedro])
    return mi_agenda

@pytest.fixture
def contacto_de_prueba1(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    c = ContactoPersonal("Ana", "1234", "dfsg@.", date.today(), "prima")
    return c

@pytest.fixture
def contacto_de_prueba2(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    fecha_valida = datetime.strptime("04/06/2000", "%d/%m/%Y").date()
    d = ContactoPersonal("Pedro", "1234", "dfsg@.", fecha_valida, "primo")
    return d
      
def test_buscar_contacto_por_nombre(agenda_de_prueba):
    assert agenda_de_prueba.buscar_contacto_por_nombre("Ana") is not None
    assert agenda_de_prueba.buscar_contacto_por_nombre("Juan") is None
    
def test_cumple_de_hoy(contacto_de_prueba1, contacto_de_prueba2):
    assert contacto_de_prueba1.es_el_cumple() == True
    assert contacto_de_prueba2.es_el_cumple() == False
    
def test_comprobar_si_un_contacto_existe(agenda_de_prueba):
    assert agenda_de_prueba.comprobar_si_un_contacto_existe("Ana") is not None
    assert agenda_de_prueba.comprobar_si_un_contacto_existe("Francisco") is None
    
def test_comprobar_nombre(agenda_de_prueba):
    assert agenda_de_prueba.comprobar_nombre("Ana") is True
    assert agenda_de_prueba.comprobar_nombre("Julio") is False
    
def test_comprobar_telefono(agenda_de_prueba):
    assert agenda_de_prueba.comprobar_telefono("123") is True
    assert agenda_de_prueba.comprobar_telefono("8974363") is False
    
def test_comprobar_correo(agenda_de_prueba):
    assert agenda_de_prueba.comprobar_correo("ewrf@.") is True
    assert agenda_de_prueba.comprobar_correo("ghbrtsh@ewrft.com") is False
    
def test_añadir_etiquetas(agenda_de_prueba):
    assert agenda_de_prueba.añadir_etiqueta("Ana", "esposa") == True
    assert agenda_de_prueba.añadir_etiqueta("Mateo", "esposa") == False
    
def test_comprobar_si_un_contacto_tiene_etiqueta_en_especifico(agenda_de_prueba):
    assert agenda_de_prueba.comprobar_si_un_contacto_tiene_etiqueta_en_especifico("Ana", "ertgfewv") == False
    assert agenda_de_prueba.comprobar_si_un_contacto_tiene_etiqueta_en_especifico("Ana", "esposa") == False
    
def test_buscar_contacto_por_numero(agenda_de_prueba):
    assert agenda_de_prueba.buscar_contacto_por_numero(12345) is None
    assert agenda_de_prueba.buscar_contacto_por_numero(123) is not None
    
def test_modificar_nombre(agenda_de_prueba):
    contacto = agenda_de_prueba.buscar_contacto_por_nombre("Ana")
    assert agenda_de_prueba.modificar_nombre(contacto, "María") == True
    assert contacto.nombre == "María"
    assert agenda_de_prueba.modificar_nombre(contacto, "Pedro") == False
    
def test_modificar_telefono(agenda_de_prueba):
    contacto = agenda_de_prueba.buscar_contacto_por_nombre("Ana")
    assert agenda_de_prueba.modificar_telefono(contacto, "123") == False
    assert agenda_de_prueba.modificar_telefono(contacto, "5673425") == True
    
def test_modificar_correo_electronico(agenda_de_prueba):
    contacto = agenda_de_prueba.buscar_contacto_por_nombre("Ana")
    assert agenda_de_prueba.modificar_correo_electronico(contacto, "ewrf@.") == False
    assert agenda_de_prueba.modificar_telefono(contacto, "sretgf@werfw.com") == True