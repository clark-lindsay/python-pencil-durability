from eraser import Eraser

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