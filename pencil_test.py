from pencil import Pencil

def test_writes_text_it_is_given():
    pencil = Pencil()
    assert pencil.write('word') == 'word'
    assert pencil.write('z') == 'z'
    assert pencil.write('a sentence with whitespace') == 'a sentence with whitespace'

def test_point_degrades_when_writing_letters():
    pencil = Pencil(3)
    assert pencil.write('word') == 'wor '

def test_point_degrades_when_writing_non_alpha_numerics():
    pencil = Pencil(5)
    assert pencil.write('!@#$%^&*()') == '!@#$%     '

def test_writing_spaces_does_not_degrade_point():
    pencil = Pencil(5)
    assert pencil.write('\n   string') == '\n   strin '

def test_writing_whitespace_escape_chars_does_not_degrade_point():
    pencil = Pencil(5)
    assert pencil.write('\n\t\v\f\r   string') == '\n\t\v\f\r   strin '