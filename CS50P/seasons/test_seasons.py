from seasons import calculate
import pytest

def test_1():
    assert round(calculate('2003-01-30')) == 10578240

def test_2():
    with pytest.raises(Exception):
        calculate('2003-30-01')

def test_3():
    with pytest.raises(Exception):
        calculate('30-01-2003')

def test_4():
    assert round(calculate('2022-03-12')) == 525600

def test_5():
    assert round(calculate('2021-03-12')) == 1051200

def test_6():
    with pytest.raises(Exception):
        calculate('cat')