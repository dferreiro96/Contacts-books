import pytest
from clases import Agenda, ContactoLaboral, ContactoPersonal
from datetime import datetime
from logica import modificar_etiquetas
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

def test_modificar_etiquetas(agenda_de_prueba):
    agenda_de_prueba.añadir_etiqueta("Ana", "etiqueta de prueba")
    with patch ("logica.pedir_opcion", return_value=1):
        with patch("logica.pedir_etiqueta", return_value= "otra etiqueta de prueba"):
            assert modificar_etiquetas(agenda_de_prueba, "Ana") == True
