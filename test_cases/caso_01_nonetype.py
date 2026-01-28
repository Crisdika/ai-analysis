"""Caso 01: Possível NoneType não tratado."""


def buscar_usuario(user_id):
    """Busca usuário no banco de dados."""
    usuarios = {"1": "João", "2": "Maria"}
    return usuarios.get(user_id)


def exibir_nome_usuario(user_id):
    """Exibe o nome do usuário em maiúsculas."""
    usuario = buscar_usuario(user_id)
    # PROBLEMA: usuario pode ser None, causando AttributeError
    print(usuario.upper())


def processar_resposta(response):
    """Processa resposta da API."""
    data = response.get("data")
    # PROBLEMA: data pode ser None
    return data["items"]


if __name__ == "__main__":
    exibir_nome_usuario("999")
