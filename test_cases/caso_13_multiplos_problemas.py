"""Caso 13: Arquivo com múltiplos problemas combinados."""


def processar_dados_usuario(data, cache={}):  # PROBLEMA: mutável como default + nome genérico
    """Processa dados do usuário."""
    from datetime import datetime

    # PROBLEMA: variável não utilizada
    temp = []

    try:
        # PROBLEMA: datetime.now() sem timezone
        timestamp = datetime.now()

        usuario = data.get("usuario")
        # PROBLEMA: possível NoneType
        nome = usuario.upper()

        # PROBLEMA: SQL injection
        query = f"SELECT * FROM logs WHERE usuario = '{nome}'"

        if nome in cache:
            if cache[nome]:
                if cache[nome].get("ativo"):
                    if cache[nome].get("verificado"):  # PROBLEMA: muitos níveis aninhados
                        return cache[nome]

        result = {"nome": nome, "query": query, "timestamp": timestamp}
        cache[nome] = result

    except:  # PROBLEMA: except genérico
        pass  # PROBLEMA: pass silencioso

    # PROBLEMA: retorno None implícito


def executar_formula(formula):
    """Executa fórmula matemática."""
    # PROBLEMA: uso de eval
    return eval(formula)


if __name__ == "__main__":
    processar_dados_usuario({"usuario": "teste"})
