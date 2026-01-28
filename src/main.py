def teste(lista=[]):  # mutable default argument
    data = "algo"  # variável genérica
    try:
        x = None
        print(x.upper())  # possível NoneType
    except:  # bare except
        pass  # silent pass