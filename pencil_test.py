from pencil import Pencil

def test_writes_text_it_is_given():
    pencil = Pencil()
    assert pencil.write('word') == 'word'
    assert pencil.write('z') == 'z'
    assert pencil.write('a sentence with whitespace') == 'a sentence with whitespace'

def test_pencil_tip_degrades_with_use():
    pencil = Pencil(3)
    assert pencil.write('word') == 'wor '