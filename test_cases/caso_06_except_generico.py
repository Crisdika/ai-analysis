"""Caso 06: except: ou except Exception: genérico."""


def dividir(a, b):
    """Divide dois números."""
    try:
        return a / b
    except:  # PROBLEMA: except genérico sem especificar exceção
        return 0


def ler_arquivo(caminho):
    """Lê conteúdo de um arquivo."""
    try:
        with open(caminho, "r") as f:
            return f.read()
    except Exception:  # PROBLEMA: except Exception muito genérico
        return None


def conectar_banco():
    """Conecta ao banco de dados."""
    try:
        # Simula conexão
        connection = {"status": "connected"}
        return connection
    except:  # PROBLEMA: except genérico
        pass  # PROBLEMA ADICIONAL: pass silencioso


def processar_json(data):
    """Processa dados JSON."""
    import json
    try:
        return json.loads(data)
    except Exception as e:  # PROBLEMA: captura exceção genérica
        print("Erro")
        return {}


def fazer_requisicao(url):
    """Faz requisição HTTP."""
    try:
        import urllib.request
        return urllib.request.urlopen(url).read()
    except:  # PROBLEMA: esconde erros de rede, timeout, SSL, etc.
        return None


if __name__ == "__main__":
    print(dividir(10, 0))
