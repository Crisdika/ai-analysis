"""Caso 14: Código limpo sem problemas - para testar resposta positiva."""

from datetime import datetime, timezone
from typing import Optional


def buscar_usuario(user_id: str) -> Optional[dict]:
    """Busca usuário no banco de dados."""
    usuarios = {"1": {"nome": "João"}, "2": {"nome": "Maria"}}
    return usuarios.get(user_id)


def exibir_nome_usuario(user_id: str) -> None:
    """Exibe o nome do usuário em maiúsculas."""
    usuario = buscar_usuario(user_id)
    if usuario is not None:
        print(usuario["nome"].upper())
    else:
        print("Usuário não encontrado")


def calcular_total(itens: list) -> float:
    """Calcula o total dos itens."""
    total = 0.0
    for item in itens:
        preco = item["preco"]
        quantidade = item["quantidade"]
        total += preco * quantidade
    return total


def criar_usuario(nome: str, permissoes: Optional[dict] = None) -> dict:
    """Cria um novo usuário."""
    if permissoes is None:
        permissoes = {}
    permissoes["leitura"] = True
    return {"nome": nome, "permissoes": permissoes}


def registrar_transacao(valor: float) -> dict:
    """Registra uma transação financeira."""
    timestamp = datetime.now(timezone.utc)
    return {
        "valor": valor,
        "data": timestamp,
        "id": f"TXN-{timestamp.timestamp()}"
    }


def ler_arquivo(caminho: str) -> Optional[str]:
    """Lê conteúdo de um arquivo."""
    try:
        with open(caminho, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
        return None
    except PermissionError:
        print(f"Sem permissão para ler: {caminho}")
        return None


def buscar_usuario_seguro(nome: str) -> str:
    """Busca usuário de forma segura."""
    # Usando parametrização (exemplo conceitual)
    query = "SELECT * FROM usuarios WHERE nome = %s"
    return query


if __name__ == "__main__":
    exibir_nome_usuario("1")
