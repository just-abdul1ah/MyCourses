import pytest
from fuel import convert, gauge

def test_convert():
    assert convert('2/4') == 50

def test_string():
    with pytest.raises(ValueError):
        convert('cat/dog')

def test_invalid():
    with pytest.raises(ZeroDivisionError):
        convert('-1/0')

def test_invalidx():
    with pytest.raises(ValueError):
        convert('4/2')

def test_empty():
    assert gauge(0) == 'E'

def test_1():
    assert gauge(1) == 'E'

def test_full():
    assert gauge(100) == 'F'

def test_99():
    assert gauge(99) == 'F'

def test_half():
    assert gauge(50) == '50%'
