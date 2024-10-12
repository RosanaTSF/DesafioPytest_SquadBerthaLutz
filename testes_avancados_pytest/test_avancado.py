import pytest
import os

# Função que converte strings em booleanos
def str_to_bool(string):
    if string.lower() in ['yes', 'y', '1']:
        return True
    elif string.lower() in ['no', 'n', '0']:
        return False

# Testes parametrizados para a função str_to_bool
@pytest.mark.parametrize("string", ['Y', 'y', '1', 'YES'])
def test_str_to_bool_true(string):
    assert str_to_bool(string) is True

@pytest.mark.parametrize("string", ['N', 'n', '0', 'NO'])
def test_str_to_bool_false(string):
    assert str_to_bool(string) is False

# Fixture para criar um arquivo temporário
@pytest.fixture
def tmpfile(tmpdir):
    def write():
        file = tmpdir.join("done")
        file.write("1")
        return file.strpath
    return write

# Classe de teste usando a fixture
class TestFile:
    def test_done_file(self, tmpfile):
        path = tmpfile()  # Usando a fixture para obter o caminho do arquivo
        # Criar o arquivo e verificar o conteúdo
        with open(path, 'w') as _f:
            _f.write("1")
        
        # Ler o conteúdo do arquivo
        with open(path) as _f:
            contents = _f.read()
        
        assert contents == "1"
