import pytest
from tarea_1 import CalProm

def test_sumar():
    #Basic Test
    assert CalProm(2.5,3.3,4.2) == 3.75
    #2 numeros iguales test
    assert CalProm(2.2,4.4,4.4) == 4.4
    #Numeros negativos y cero
    assert CalProm(-1,0,4) == 2