"""Caso 04: Uso de mutáveis como valor default em funções."""


def adicionar_item(item, lista=[]):  # PROBLEMA: lista mutável como default
    """Adiciona item à lista."""
    lista.append(item)
    return lista


def criar_usuario(nome, permissoes={}):  # PROBLEMA: dict mutável como default
    """Cria um novo usuário."""
    permissoes["leitura"] = True
    return {"nome": nome, "permissoes": permissoes}


def registrar_log(mensagem, logs=[]):  # PROBLEMA: lista mutável como default
    """Registra uma mensagem de log."""
    logs.append(mensagem)
    print(f"Logs atuais: {logs}")
    return logs


class Carrinho:
    def __init__(self, itens=[]):  # PROBLEMA: lista mutável como default
        """Inicializa o carrinho."""
        self.itens = itens

    def adicionar(self, item):
        self.itens.append(item)


if __name__ == "__main__":
    # Demonstra o problema
    lista1 = adicionar_item("a")
    lista2 = adicionar_item("b")
    print(f"Lista 1: {lista1}")  # Vai mostrar ['a', 'b'] - não esperado!
    print(f"Lista 2: {lista2}")  # Vai mostrar ['a', 'b']
