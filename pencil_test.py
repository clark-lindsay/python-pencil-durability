from pencil import Pencil

def test_writes_text_it_is_given():
    pencil = Pencil()
    assert pencil.write('word') == 'word'
    assert pencil.write('z') == 'z'
    assert pencil.write('a sentence with whitespace') == 'a sentence with whitespace'

def test_point_degrades_one_point_for_lowercase_letters():
    pencil = Pencil(3)
    assert pencil.write('word') == 'wor '

def test_point_degrades_two_points_for_capital_letters():
    pencil = Pencil(4)
    assert pencil.write('Text') == 'Tex '

def test_can_write_a_capital_with_only_one_point_of_durability_remaining():
    pencil = Pencil(4)
    assert pencil.write('texT') == 'texT'

def test_point_degrades_one_point_for_non_alpha_numerics():
    pencil = Pencil(5)
    assert pencil.write('!@#$%^&*()') == '!@#$%     '

def test_writing_spaces_does_not_degrade_point():
    pencil = Pencil(5)
    assert pencil.write('\n   string') == '\n   strin '

def test_writing_whitespace_escape_chars_does_not_degrade_point():
    pencil = Pencil(5)
    assert pencil.write('\n\t\v\f\r   string') == '\n\t\v\f\r   strin '

def test_can_be_sharpened_to_regain_point_durability():
    pencil = Pencil(5)
    assert pencil.write('string') == 'strin '
    pencil.sharpen()
    assert pencil.write('text') == 'text'

def test_once_sharpened_to_length_0_it_does_not_restore_point_durability():
    pencil = Pencil(5, 1)
    assert pencil.write('Texts') == 'Text '
    pencil.sharpen()
    assert pencil.write('Texts') == 'Text '
    pencil.sharpen()
    assert pencil.write('Texts') == '     '