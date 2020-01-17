from eraser import Eraser

def test_erases_the_word_it_is_given():
    eraser = Eraser()
    assert eraser.erase('Bill', 'Buffalo Bill') == 'Buffalo     '