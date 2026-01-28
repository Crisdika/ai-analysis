"""Caso 03: Retorno implícito None não intencional."""


def buscar_produto(produto_id):
    """Busca um produto pelo ID."""
    produtos = {
        "1": {"nome": "Notebook", "preco": 3000},
        "2": {"nome": "Mouse", "preco": 50},
    }

    if produto_id in produtos:
        return produtos[produto_id]
    # PROBLEMA: retorna None implicitamente se produto não existir


def validar_email(email):
    """Valida formato do email."""
    if "@" in email and "." in email:
        return True
    elif not email:
        return False
    # PROBLEMA: retorna None implicitamente para emails inválidos com conteúdo


def calcular_desconto(valor, tipo_cliente):
    """Calcula desconto baseado no tipo de cliente."""
    if tipo_cliente == "vip":
        return valor * 0.2
    if tipo_cliente == "regular":
        return valor * 0.1
    # PROBLEMA: retorna None para outros tipos de cliente


if __name__ == "__main__":
    produto = buscar_produto("999")
    print(f"Produto: {produto}")
