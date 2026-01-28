"""Caso 10: Funções novas excessivamente longas."""


def processar_pedido_completo(pedido):
    """Processa um pedido do início ao fim."""
    # PROBLEMA: função excessivamente longa com muitas responsabilidades

    # Validação do pedido
    if not pedido:
        return {"erro": "Pedido vazio"}

    if "cliente" not in pedido:
        return {"erro": "Cliente não informado"}

    if "itens" not in pedido:
        return {"erro": "Itens não informados"}

    if len(pedido["itens"]) == 0:
        return {"erro": "Pedido sem itens"}

    # Validação do cliente
    cliente = pedido["cliente"]
    if "nome" not in cliente:
        return {"erro": "Nome do cliente não informado"}

    if "email" not in cliente:
        return {"erro": "Email do cliente não informado"}

    if "@" not in cliente["email"]:
        return {"erro": "Email inválido"}

    # Cálculo do total
    total = 0
    for item in pedido["itens"]:
        if "preco" not in item:
            return {"erro": "Preço não informado"}
        if "quantidade" not in item:
            return {"erro": "Quantidade não informada"}
        subtotal = item["preco"] * item["quantidade"]
        total += subtotal

    # Aplicação de desconto
    desconto = 0
    if total > 1000:
        desconto = total * 0.1
    elif total > 500:
        desconto = total * 0.05
    elif total > 100:
        desconto = total * 0.02

    total_com_desconto = total - desconto

    # Cálculo de frete
    frete = 0
    if "endereco" in pedido:
        endereco = pedido["endereco"]
        if "estado" in endereco:
            estado = endereco["estado"]
            if estado == "SP":
                frete = 10
            elif estado == "RJ":
                frete = 15
            elif estado == "MG":
                frete = 20
            else:
                frete = 30

    total_final = total_com_desconto + frete

    # Geração do número do pedido
    import random
    numero_pedido = random.randint(10000, 99999)

    # Criação do registro
    registro = {
        "numero": numero_pedido,
        "cliente": cliente["nome"],
        "email": cliente["email"],
        "itens": pedido["itens"],
        "subtotal": total,
        "desconto": desconto,
        "frete": frete,
        "total": total_final,
        "status": "criado"
    }

    # Log do pedido
    print(f"Pedido {numero_pedido} criado")
    print(f"Cliente: {cliente['nome']}")
    print(f"Total: R$ {total_final:.2f}")

    # Envio de confirmação
    print(f"Enviando email para {cliente['email']}")

    # Atualização de estoque
    for item in pedido["itens"]:
        print(f"Atualizando estoque: {item.get('nome', 'item')} - {item['quantidade']}")

    return registro


if __name__ == "__main__":
    pedido = {
        "cliente": {"nome": "João", "email": "joao@email.com"},
        "itens": [{"nome": "Produto", "preco": 100, "quantidade": 2}],
        "endereco": {"estado": "SP"}
    }
    print(processar_pedido_completo(pedido))
