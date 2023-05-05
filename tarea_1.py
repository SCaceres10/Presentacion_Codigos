
def f(entrada):   
    return list(filter(lambda cadena: cadena[:2] =="CA",list(map(str.upper,entrada))))