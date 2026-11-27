import pytest
from clases import Agenda, ContactoLaboral, ContactoPersonal
from datetime import datetime
from logica import modificar_etiquetas, gestionar_edicion_de_contactos
from utilidades import pedir_nombre
from unittest.mock import patch

@pytest.fixture
def agenda_de_prueba(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    mi_agenda = Agenda()
    fecha_valida = datetime.strptime("04/06/2000", "%d/%m/%Y").date()
    ana = ContactoLaboral("Ana", "123", "ewrf@.", "ergv", "ergf")
    pedro = ContactoPersonal("Pedro", "34456", "ertvg@.", fecha_valida, "primo")
    juan = ContactoLaboral("Juan", "+53 5-365-4891", "erctf@tg.vo", "bhrd", "ervg")
    mi_agenda.lista_de_contactos.extend([ana, pedro, juan])
    return mi_agenda

def test_modificar_etiquetas_si_tiene_etiquetas(agenda_de_prueba):
    agenda_de_prueba.añadir_etiqueta("Ana", "etiqueta de prueba")
    with patch ("logica.pedir_opcion", return_value=1):
        with patch("logica.pedir_etiqueta", return_value= "otra etiqueta de prueba"):
            assert modificar_etiquetas(agenda_de_prueba, "Ana") == True
            
def test_modificar_etiquetas_si_no_tiene_etiquetas(agenda_de_prueba):
    with patch("logica.pedir_opcion", return_value=1):
        with patch("logica.pedir_etiqueta", return_value= "otra etiqueta de prueba"):
            assert modificar_etiquetas(agenda_de_prueba, "Pedro") == False
            
def test_gestionar_edicion_de_nombre_de_contacto_que_existe(agenda_de_prueba):
    with patch("logica.pedir_nombre", return_value="Ana"):
        with patch("logica.pedir_opcion", return_value=1):
            with patch("logica.pedir_nombre", return_value="Francisco"):
                assert gestionar_edicion_de_contactos(agenda_de_prueba) == True
    
