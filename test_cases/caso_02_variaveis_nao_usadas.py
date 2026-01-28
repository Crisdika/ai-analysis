"""Caso 02: Variáveis criadas e não utilizadas."""


def calcular_total(itens):
    """Calcula o total dos itens."""
    total = 0
    contador = 0  # PROBLEMA: variável nunca utilizada
    desconto = 0.1  # PROBLEMA: variável nunca utilizada

    for item in itens:
        preco = item["preco"]
        quantidade = item["quantidade"]
        nome = item["nome"]  # PROBLEMA: variável nunca utilizada
        total += preco * quantidade

    return total


def processar_pedido(pedido):
    """Processa um pedido."""
    cliente = pedido["cliente"]  # PROBLEMA: variável nunca utilizada
    items = pedido["items"]
    status = "processando"  # PROBLEMA: variável nunca utilizada

    return calcular_total(items)


if __name__ == "__main__":
    pedido = {
        "cliente": "João",
        "items": [{"nome": "Produto A", "preco": 10, "quantidade": 2}]
    }
    print(processar_pedido(pedido))
