import pencil

def test_writes_text_it_is_given():
    yellow_pencil = pencil.Pencil()
    assert yellow_pencil.write('word') == 'word'
    assert yellow_pencil.write('z') == 'z'
    assert yellow_pencil.write('a sentence with whitespace') == 'a sentence with whitespace'