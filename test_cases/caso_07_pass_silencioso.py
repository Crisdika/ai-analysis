"""Caso 07: pass silencioso em fluxo crítico."""


def processar_pagamento(valor, cartao):
    """Processa um pagamento."""
    try:
        # Simula processamento
        if valor <= 0:
            raise ValueError("Valor inválido")
        return {"status": "sucesso", "valor": valor}
    except ValueError:
        pass  # PROBLEMA: pass silencioso em fluxo de pagamento


def salvar_dados_usuario(usuario):
    """Salva dados do usuário no banco."""
    try:
        # Simula salvamento
        if not usuario.get("email"):
            raise KeyError("Email obrigatório")
        return True
    except KeyError:
        pass  # PROBLEMA: pass silencioso perde dados sem aviso


def enviar_notificacao(mensagem, destinatario):
    """Envia notificação para o usuário."""
    try:
        # Simula envio
        if not destinatario:
            raise ValueError("Destinatário inválido")
        print(f"Enviando: {mensagem}")
    except:
        pass  # PROBLEMA: falha silenciosa em notificação importante


def validar_token(token):
    """Valida token de autenticação."""
    try:
        if not token or len(token) < 10:
            raise ValueError("Token inválido")
        return True
    except ValueError:
        pass  # PROBLEMA: falha de segurança silenciosa


if __name__ == "__main__":
    processar_pagamento(-100, "1234")
    print("Continuou sem erro!")
