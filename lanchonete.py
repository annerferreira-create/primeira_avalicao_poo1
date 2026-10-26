# Integrantes
#1: Anne Regina
#2: Dinara Dutra

cardapio = {
    "hamburguer": 25.0,
    "sanduiche": 18.0,
    "batata": 12.0,
    "suco": 8.0,
    "agua": 5.0
}

pedido = [
    {"produto": "HAMBURGUER", "quantidade": 2},
    {"produto": "batata", "quantidade": 1},
    {"produto": "Suco", "quantidade": 3},
    {"produto": "pizza", "quantidade": 1},
    {"produto": "agua", "quantidade": 0}
]
nome = "Felipe"
cupom = "SIM"

def validar_item(produto, quantidade, cardapio):
    """Retorna True se o produto existe no cardápio e a quantidade é maior que zero."""
    return produto in cardapio and quantidade > 0