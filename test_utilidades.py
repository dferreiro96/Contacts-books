from utilidades import formatear_numero_de_telefono


def test_formatear_numero_de_telefono():
    assert formatear_numero_de_telefono ("53654891") == "+53 5-365-4891"
    assert formatear_numero_de_telefono("123") == ("123")