from numb3rs import validate
import random

def num():
    return random.randint(0, 255)

def other():
    return random.randint(255, 1000)

def test():
    for _ in range(5):
        assert validate(f'{num()}.{num()}.{num()}.{num()}') == True

def test2():
    for _ in range(5):
        assert validate(f'{other()}.{other()}.{other()}.{other()}') == False

def test3():
    assert validate('cat') == False

def test4():
    assert validate(f'{num()}.{other()}.{other()}.{other()}') == False
