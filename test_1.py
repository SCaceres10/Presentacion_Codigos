import pytest
from tarea_1 import f

def test_sumar():
    # no inicia con CA
    assert f(["perro","ayuda","adios","camello","hamaca"]) == ["CAMELLO"]
    # Ninguno con CA
    assert f(["teclado","pelota","ciclo","maquina","IA"]) == []
    #2 Varios con CA
    assert f(["casa","carro","perro","paseo","cabeza"]) == ["CASA","CARRO","CABEZA"]