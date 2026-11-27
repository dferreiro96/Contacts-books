from unittest.mock import patch

import pytest

from utilidades import confirmacion_borrar_contactos, formatear_numero_de_telefono


def test_formatear_numero_de_telefono():
    assert formatear_numero_de_telefono ("53654891") == "+53 5-365-4891"
    assert formatear_numero_de_telefono("123") == ("123")


@pytest.mark.parametrize("respuesta", ["s", "si", "sí", "S", "SI", "SÍ"])
def test_confirmacion_si(respuesta):
    with patch("builtins.input", return_value=respuesta):
        assert confirmacion_borrar_contactos("algo") is True

@pytest.mark.parametrize("respuesta", ["n", "no", "N", "NO"])
def test_confirmacion_no(respuesta):
    with patch("builtins.input", return_value=respuesta):
        assert confirmacion_borrar_contactos("algo") is False