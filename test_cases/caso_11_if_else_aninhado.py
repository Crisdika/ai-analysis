"""Caso 11: Muitos níveis de if/else aninhados."""


def calcular_preco_final(produto, cliente, cupom):
    """Calcula preço final com muitos níveis de aninhamento."""
    # PROBLEMA: muitos níveis de if/else aninhados
    if produto:
        if "preco" in produto:
            preco = produto["preco"]
            if preco > 0:
                if cliente:
                    if "tipo" in cliente:
                        if cliente["tipo"] == "vip":
                            if cupom:
                                if cupom["ativo"]:
                                    if cupom["tipo"] == "percentual":
                                        return preco * 0.7  # 30% off
                                    else:
                                        return preco - cupom["valor"]
                                else:
                                    return preco * 0.8
                            else:
                                return preco * 0.8
                        else:
                            if cupom:
                                if cupom["ativo"]:
                                    return preco * 0.9
                                else:
                                    return preco
                            else:
                                return preco
                    else:
                        return preco
                else:
                    return preco
            else:
                return 0
        else:
            return 0
    else:
        return 0


def validar_acesso(usuario, recurso, permissao):
    """Valida acesso com lógica confusa."""
    # PROBLEMA: lógica condicional muito aninhada
    if usuario:
        if usuario.get("ativo"):
            if usuario.get("permissoes"):
                if recurso in usuario["permissoes"]:
                    if permissao in usuario["permissoes"][recurso]:
                        if not usuario.get("bloqueado"):
                            if usuario.get("verificado"):
                                return True
                            else:
                                if permissao == "leitura":
                                    return True
                                else:
                                    return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    produto = {"preco": 100}
    cliente = {"tipo": "vip"}
    cupom = {"ativo": True, "tipo": "percentual"}
    print(calcular_preco_final(produto, cliente, cupom))
