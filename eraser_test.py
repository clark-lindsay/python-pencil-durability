from eraser import *

def test_erases_the_word_it_is_given():
    eraser = Eraser()
    assert eraser.erase('Bill', 'Buffalo Bill') == 'Buffalo     '

def test_erases_only_the_last_occurence_of_given_word():
    eraser = Eraser()
    firstErase =  eraser.erase('chuck', 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?') 
    secondErase = eraser.erase('chuck', firstErase)
    thirdErase = eraser.erase('chuck', secondErase)

    assert firstErase == 'How much wood would a woodchuck chuck if a woodchuck could       wood?'
    assert secondErase == 'How much wood would a woodchuck chuck if a wood      could       wood?'
    assert thirdErase == 'How much wood would a woodchuck       if a wood      could       wood?'

def test_eraser_does_not_erase_once_it_has_0_durability():
    eraser = Eraser(3)
    assert eraser.erase('Bill', 'Buffalo Bill') == 'Buffalo B   '

def test_erasing_whitespace_does_not_lower_durability():
    eraser = Eraser(10)
    assert eraser.erase('these words', 'this word and these words') == 'this word and            '

def test_reverse():
    assert reverse('word') == 'drow'
    assert reverse('text with spaces \n') == '\n secaps htiw txet'

def test_count_whitespace_chars():
    assert count_whitespace_chars('nospaces') == 0
    assert count_whitespace_chars('text with spaces \n') == 4