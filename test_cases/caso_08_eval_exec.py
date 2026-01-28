"""Caso 08: Uso de eval ou exec."""


def calcular_expressao(expressao):
    """Calcula uma expressão matemática."""
    # PROBLEMA: uso de eval com input não sanitizado
    return eval(expressao)


def executar_comando(codigo):
    """Executa código dinâmico."""
    # PROBLEMA: uso de exec é perigoso
    exec(codigo)


def processar_filtro(campo, operador, valor):
    """Processa um filtro dinâmico."""
    # PROBLEMA: construção de código com eval
    expressao = f"registro['{campo}'] {operador} {valor}"
    registro = {"idade": 25, "salario": 5000}
    return eval(expressao)


def carregar_configuracao(config_str):
    """Carrega configuração de uma string."""
    # PROBLEMA: eval para parsear configuração
    return eval(config_str)


class Calculadora:
    def calcular(self, formula):
        """Calcula fórmula dinâmica."""
        # PROBLEMA: eval em método de classe
        return eval(formula)


if __name__ == "__main__":
    # Isso pode executar código malicioso!
    resultado = calcular_expressao("2 + 2")
    print(resultado)
