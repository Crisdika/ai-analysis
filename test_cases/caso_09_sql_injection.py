"""Caso 09: SQL construído via string sem parametrização."""


def buscar_usuario_por_nome(nome):
    """Busca usuário pelo nome."""
    # PROBLEMA: SQL injection vulnerável
    query = f"SELECT * FROM usuarios WHERE nome = '{nome}'"
    print(f"Executando: {query}")
    return query


def deletar_registro(tabela, id_registro):
    """Deleta um registro de uma tabela."""
    # PROBLEMA: SQL injection em DELETE
    query = "DELETE FROM " + tabela + " WHERE id = " + str(id_registro)
    return query


def buscar_produtos(categoria, preco_max):
    """Busca produtos por categoria e preço."""
    # PROBLEMA: concatenação de string em SQL
    query = "SELECT * FROM produtos WHERE categoria = '" + categoria + "'"
    query += " AND preco <= " + str(preco_max)
    return query


def atualizar_email(user_id, novo_email):
    """Atualiza email do usuário."""
    # PROBLEMA: f-string em SQL
    query = f"UPDATE usuarios SET email = '{novo_email}' WHERE id = {user_id}"
    return query


def login(username, password):
    """Realiza login do usuário."""
    # PROBLEMA: SQL injection crítico em autenticação
    query = f"SELECT * FROM usuarios WHERE username = '{username}' AND password = '{password}'"
    return query


if __name__ == "__main__":
    # Demonstra vulnerabilidade
    buscar_usuario_por_nome("'; DROP TABLE usuarios; --")
