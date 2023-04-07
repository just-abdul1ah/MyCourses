from twttr import shorten

def test_uppercase():
    assert shorten('TWITTER') == 'TWTTR'

def test_lowercase():
    assert shorten('tesla') == 'tsl'

def test_number():
    assert shorten('101') == '101'

def test_punctuation():
    assert shorten('Tesla, motors') == 'Tsl, mtrs'
