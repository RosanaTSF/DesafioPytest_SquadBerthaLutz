import pytest

def test_divisao():
    assert 10 / 2 == 5
    assert 9 / 3 == 3
    assert -10 / 2 == -5
    assert 10 / -2 == -5
    assert 10 / 4 == 2.5

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        10 / 0
