from jar import Jar
import pytest

def test_object():
    jar = Jar(15)
    assert jar.capacity == 15

def test_negative():
    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_deposit():
    jar = Jar(15)
    jar.deposit(5)
    assert jar.size == 5

def test_withdraw():
    jar = Jar(15)
    jar.deposit(10)
    jar.withdraw(2)
    assert jar.size == 8

def test_overload():
    jar = Jar(15)
    with pytest.raises(ValueError):
        jar.deposit(20)

def test_empty():
    jar = Jar(15)
    with pytest.raises(ValueError):
        jar.withdraw(1)

def test_print():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == '🍪'*5

