# Desafio Pytest - Squad Sarah Gilbert

## 📚 Sobre o Projeto

Este projeto é parte do **Bootcamp Womakerscode** e tem como objetivo aplicar testes automatizados utilizando a biblioteca **pytest** para garantir a qualidade do código e a confiabilidade das funcionalidades.

## 🛠️ O que foi feito

- **✨ Implementação de Testes**: Criação de testes automatizados com pytest.
- **📂 Estrutura de Testes**: Organização e uso de fixtures para facilitar a execução dos testes.
- **📝 Documentação**: Registros detalhados do processo e resultados.

## 🧪 O que é o Pytest?

**pytest** é uma biblioteca poderosa para testes em Python, que oferece:

- **✅ Simplicidade e Legibilidade**: Testes claros e concisos.
- **🔍 Descoberta Automática**: Encontra testes automaticamente.
- **📦 Fixtures**: Organização eficiente de dados de teste.
- **📊 Relatórios Detalhados**: Resultados claros e compreensíveis.

### Exemplos de Uso

```python
def test_soma():
    assert soma(2, 3) == 5
```

```python
@pytest.fixture
def dados_de_teste():
    return {'usuario': 'teste', 'senha': '1234'}
```

## 📦 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone <URL do repositório>
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd <diretório do projeto>
   ```
3. Ative o ambiente virtual:
   ```bash
   source venv/Scripts/activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute os testes:
   ```bash
   pytest
   ```
---
