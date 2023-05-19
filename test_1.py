import pytest
from tarea_1 import CalProm

def test_sumar():
    
    assert CalProm(1.0,2.0,3.0) == 2.5
    assert CalProm(1.0,3.0,2.0) == 2.5
    assert CalProm(2.0,1.0,3.0) == 2.5
    assert CalProm(2.0,3.0,1.0) == 2.5
    assert CalProm(3.0,2.0,1.0) == 2.5
    assert CalProm(3.0,1.0,2.0) == 2.5