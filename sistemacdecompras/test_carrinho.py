import pytest
from carrinho import Carrinho


@pytest.fixture
def carrinho():
    return Carrinho()


# ── Soma correta ──────────────────────────────────────────────
def test_carrinho_vazio_retorna_zero(carrinho):
    assert carrinho.calcular_total() == 0

def test_adicionar_um_item(carrinho):
    carrinho.adicionar_item("Caneta", 2.50)
    assert carrinho.calcular_total() == 2.50

def test_soma_multiplos_itens(carrinho):
    carrinho.adicionar_item("Caneta", 2.50)
    carrinho.adicionar_item("Caderno", 15.00)
    carrinho.adicionar_item("Mochila", 80.00)
    assert carrinho.calcular_total() == 97.50

def test_soma_com_quantidade(carrinho):
    carrinho.adicionar_item("Caneta", 2.50, quantidade=4)
    assert carrinho.calcular_total() == 10.00


# ── Remoção de item ───────────────────────────────────────────
def test_remover_item(carrinho):
    carrinho.adicionar_item("Caneta", 2.50)
    carrinho.adicionar_item("Caderno", 15.00)
    carrinho.remover_item("Caneta")
    assert carrinho.calcular_total() == 15.00

def test_remover_item_inexistente_nao_quebra(carrinho):
    carrinho.adicionar_item("Caneta", 2.50)
    carrinho.remover_item("Borracha")   # não existe — não deve lançar erro
    assert carrinho.calcular_total() == 2.50

def test_remover_unico_item_deixa_carrinho_vazio(carrinho):
    carrinho.adicionar_item("Caneta", 2.50)
    carrinho.remover_item("Caneta")
    assert carrinho.calcular_total() == 0


# ── Aplicação de desconto ─────────────────────────────────────
def test_desconto_valido(carrinho):
    carrinho.adicionar_item("Caderno", 100.00)
    assert carrinho.aplicar_desconto(10) == 90.00

def test_desconto_maximo_20_porcento(carrinho):
    carrinho.adicionar_item("Caderno", 100.00)
    assert carrinho.aplicar_desconto(20) == 80.00

def test_desconto_acima_20_levanta_erro(carrinho):
    carrinho.adicionar_item("Caderno", 100.00)
    with pytest.raises(ValueError):
        carrinho.aplicar_desconto(21)

def test_desconto_negativo_levanta_erro(carrinho):
    carrinho.adicionar_item("Caderno", 100.00)
    with pytest.raises(ValueError):
        carrinho.aplicar_desconto(-5)

def test_desconto_zero_retorna_total_cheio(carrinho):
    carrinho.adicionar_item("Caderno", 100.00)
    assert carrinho.aplicar_desconto(0) == 100.00