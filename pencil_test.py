import pencil

def test_writes_text_it_is_given():
    yellow_pencil = pencil.Pencil()
    assert yellow_pencil.write('word') == 'word'