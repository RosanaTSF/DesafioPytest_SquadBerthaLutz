import pytest

# Usando pytest.mark.parametrize para múltiplos cenários
@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 6),   # caso normal
    (4, 5, 20),  # outro caso
    (0, 10, 0),  # multiplicação por zero
    (-1, 7, -7), # número negativo
    (-2, -3, 6)  # multiplicação de negativos
])
def test_multiplicacao(a, b, esperado):
    assert a * b == esperado
