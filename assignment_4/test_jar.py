import pytest
from jar import Jar

def test_deposited():
    jar = Jar(10)
    jar.deposit(3)
    jar.deposit(4)
    assert jar.size == 7

def test_deposit_error():
    jar = Jar(2)
    with pytest.raises(ValueError):
        jar.deposit(4)

def test_withdrawn():
    jar = Jar(10)
    jar.deposit(6)
    jar.withdraw(4)
    assert jar.size == 2
    jar.deposit(8)
    jar.withdraw(1)
    jar.withdraw(9)
    assert jar.size == 0

def test_withdrawn_error():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(7)

def test_non_numeric():
    jar = Jar(10)
    with pytest.raises(TypeError):
        jar.deposit('hi')
    with pytest.raises(TypeError):
        jar.withdraw(None)

# pytest test_jar.py