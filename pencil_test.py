from pencil import Pencil

def test_writes_text_it_is_given():
    pencil = Pencil()
    assert pencil.write('word') == 'word'
    assert pencil.write('z') == 'z'
    assert pencil.write('a sentence with whitespace') == 'a sentence with whitespace'

def test_pencil_tip_degrades_when_writing_letters():
    pencil = Pencil(3)
    assert pencil.write('word') == 'wor '

def test_pencil_tip_degrades_when_writing_non_alpha_numerics():
    pencil = Pencil(5)
    assert pencil.write('!@#$%^&*()') == '!@#$%     '