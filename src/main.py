"""Módulo principal da aplicação."""


def hello():
    """Função de boas-vindas."""
    print("Olá! Bem-vindo ao projeto Python!")


# ========================
# CENÁRIOS DE TESTE - Problemas que devem ser detectados no PR
# ========================


# CENÁRIO 1: NoneType não tratado
def scenario_1_nonetype_error():
    """Risco: Possível erro de NoneType"""
    user_data = get_user_from_database()
    return user_data.name  # Vai quebrar se user_data for None


# CENÁRIO 2: Variável criada e não utilizada
def scenario_2_unused_variable():
    """Erro: Variável criada mas nunca usada"""
    result = calculate_total()
    final_value = result * 1.1  # Variável não é usada
    return result


# CENÁRIO 3: Mutável como valor default
def scenario_3_mutable_default(items=[]):
    """Erro clássico: mutável como argumento padrão"""
    items.append("novo")
    return items


# CENÁRIO 4: datetime.now() sem timezone
def scenario_4_datetime_without_tz():
    """Risco: datetime sem timezone em contexto crítico"""
    from datetime import datetime
    timestamp = datetime.now()  # Sem timezone
    return process_payment(timestamp)


# CENÁRIO 5: Except genérico
def scenario_5_generic_except():
    """Risco: Tratamento de erro muito amplo"""
    try:
        result = process_critical_data()
        return result
    except:  # Captura tudo
        return None


# CENÁRIO 6: Except Exception genérico
def scenario_6_generic_exception():
    """Risco: Tratamento genérico de Exception"""
    try:
        data = fetch_external_api()
        return data
    except Exception:  # Muito genérico
        return {}


# CENÁRIO 7: Lógica condicional confusa
def scenario_7_confusing_logic(status, paid, active, verified, role):
    """Risco: Lógica difícil de seguir"""
    if (status == "active" and paid or not active and verified) or (role == "admin" and not paid or verified and status != "pending"):
        return True
    return False


# CENÁRIO 8: Pass silencioso em fluxo crítico
def scenario_8_silent_pass():
    """Risco: Pass esconde erro em fluxo importante"""
    if validate_payment():
        process_order()
    else:
        pass  # Falha silenciosa


# CENÁRIO 9: Uso de eval
def scenario_9_eval_usage(user_input):
    """Risco: Uso de eval com input externo"""
    result = eval(user_input)  # Perigoso
    return result


# CENÁRIO 10: Uso de exec
def scenario_10_exec_usage(code_string):
    """Risco: Uso de exec"""
    exec(code_string)  # Pode executar código malicioso


# CENÁRIO 11: SQL sem parametrização
def scenario_11_sql_injection(user_id):
    """Risco: SQL construído com string (SQL Injection)"""
    import sqlite3
    conn = sqlite3.connect('database.db')
    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL Injection
    conn.execute(query)


# CENÁRIO 12: Função excessivamente longa
def scenario_12_too_long_function(data):
    """Risco: Função nova muito longa e difícil de entender"""
    result = []
    for item in data:
        if item.is_valid():
            processed = item.process()
            if processed:
                if processed.status == "active":
                    if processed.verified:
                        if processed.paid:
                            calculated = processed.amount * 1.1
                            if calculated > 100:
                                final = calculated - 10
                                result.append(final)
                            else:
                                final = calculated
                                result.append(final)
                        else:
                            result.append(0)
                    else:
                        result.append(None)
                else:
                    result.append(None)
            else:
                continue
        else:
            if item.can_retry():
                retry_item(item)
            else:
                log_error(item)
    return result


# CENÁRIO 13: Muitos níveis de if/else aninhados
def scenario_13_nested_conditionals(user, account, payment):
    """Risco: Muitos níveis de aninhamento"""
    if user:
        if user.is_active:
            if account:
                if account.verified:
                    if payment:
                        if payment.valid:
                            if payment.amount > 0:
                                return True
    return False


# CENÁRIO 14: Nomes extremamente genéricos
def scenario_14_generic_names():
    """Risco: Nomes muito genéricos no código novo"""
    data = fetch_something()
    temp = data.process()
    obj = transform(temp)
    return obj


# CENÁRIO 15: Retorno None não intencional
def scenario_15_implicit_none(value):
    """Erro: Função pode retornar None sem intenção"""
    if value > 10:
        return value * 2
    # Retorna None implicitamente quando value <= 10


# CENÁRIO 16: Combinação de múltiplos problemas
def scenario_16_multiple_issues(user_input, items=[]):
    """Múltiplos problemas em uma função"""
    temp = user_input  # Nome genérico
    try:
        result = eval(temp)  # eval perigoso
    except:  # except genérico
        pass  # pass silencioso
    items.append(result)
    unused_var = calculate_something()  # Variável não usada
    return items


# CENÁRIO 17: Datetime em operação financeira
def scenario_17_financial_datetime(amount):
    """Risco: datetime sem timezone em contexto financeiro"""
    from datetime import datetime
    transaction_time = datetime.now()  # Sem timezone em transação financeira
    return {
        "amount": amount,
        "timestamp": transaction_time,
        "status": "completed"
    }


# CENÁRIO 18: None não tratado em cadeia de chamadas
def scenario_18_none_chain():
    """Risco: Cadeia de chamadas sem verificar None"""
    user = get_user()
    profile = user.get_profile()  # user pode ser None
    return profile.email


# ========================
# Funções auxiliares
# ========================
def get_user_from_database(): return None
def calculate_total(): return 100
def process_payment(ts): return True
def process_critical_data(): return {}
def fetch_external_api(): return {}
def validate_payment(): return False
def process_order(): pass
def fetch_something(): return type('obj', (), {'process': lambda: None})()
def transform(x): return x
def calculate_something(): return 42
def get_user(): return None
def retry_item(item): pass
def log_error(item): pass


if __name__ == "__main__":
    hello()
