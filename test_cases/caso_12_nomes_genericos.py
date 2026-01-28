"""Caso 12: Nomes extremamente genéricos (data, temp, obj)."""


def processar(data):  # PROBLEMA: nome genérico 'data'
    """Processa dados."""
    temp = []  # PROBLEMA: nome genérico 'temp'

    for item in data:
        obj = item.copy()  # PROBLEMA: nome genérico 'obj'
        obj["processado"] = True
        temp.append(obj)

    return temp


def calcular(x, data2):  # PROBLEMA: nomes genéricos 'x' e 'data2'
    """Calcula algo."""
    result = 0  # PROBLEMA: nome genérico 'result'

    for d in data2:  # PROBLEMA: nome genérico 'd'
        result += d * x

    return result


def fazer_algo(obj1, obj2):  # PROBLEMA: nomes genéricos
    """Faz algo com dois objetos."""
    temp1 = obj1.get("valor", 0)  # PROBLEMA: nomes genéricos
    temp2 = obj2.get("valor", 0)

    data = {"soma": temp1 + temp2}  # PROBLEMA: 'data' genérico
    return data


class Processador:
    def __init__(self):
        self.data = []  # PROBLEMA: atributo genérico
        self.temp = None  # PROBLEMA: atributo genérico

    def run(self, input):  # PROBLEMA: 'input' é builtin e genérico
        """Executa processamento."""
        output = []  # PROBLEMA: nome genérico

        for item in input:
            val = item * 2  # PROBLEMA: nome genérico 'val'
            output.append(val)

        return output


def handler(event, ctx):  # PROBLEMA: 'ctx' muito abreviado
    """Handler de evento."""
    info = event.get("info")  # PROBLEMA: 'info' genérico
    stuff = ctx.get("stuff")  # PROBLEMA: 'stuff' genérico

    return {"data": info, "extra": stuff}


if __name__ == "__main__":
    data = [{"valor": 1}, {"valor": 2}]
    print(processar(data))
