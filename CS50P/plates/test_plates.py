from plates import is_valid

def test_numbers_only():
    assert is_valid('112233') == False

def test_letters_only():
    assert is_valid('AAAAAa') == True

def test_valid():
    assert is_valid('AA0000') == False

def test_number_between():
    assert is_valid('AA22JJ') == False

def test_long():
    assert is_valid('AsD1234') == False

def test_alphanumeric():
    assert is_valid('AA@J22') == False