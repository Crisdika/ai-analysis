"""Caso 05: Uso de datetime.now() sem timezone quando relevante."""

from datetime import datetime


def registrar_transacao(valor):
    """Registra uma transação financeira."""
    # PROBLEMA: datetime.now() sem timezone em contexto financeiro
    timestamp = datetime.now()
    return {
        "valor": valor,
        "data": timestamp,
        "id": f"TXN-{timestamp.timestamp()}"
    }


def agendar_evento(nome, dias_para_frente):
    """Agenda um evento para daqui a X dias."""
    from datetime import timedelta
    # PROBLEMA: datetime.now() sem timezone para agendamento
    data_evento = datetime.now() + timedelta(days=dias_para_frente)
    return {"nome": nome, "data": data_evento}


def calcular_tempo_restante(data_limite):
    """Calcula tempo restante até a data limite."""
    # PROBLEMA: comparação com datetime.now() sem timezone
    agora = datetime.now()
    return data_limite - agora


def log_auditoria(acao, usuario):
    """Registra log de auditoria."""
    # PROBLEMA: datetime.now() sem timezone em log de auditoria
    return {
        "acao": acao,
        "usuario": usuario,
        "timestamp": datetime.now().isoformat()
    }


if __name__ == "__main__":
    print(registrar_transacao(100.00))
