class Eraser:
    def __init__(self, durability=100):
        self.durability = durability

    def erase(self, toErase, text):
        self._erase_preconditions(toErase, text)
        reversedText = reverse(text)
        reversedToErase = reverse(toErase)[:self.durability + count_whitespace_chars(toErase)]
        replaceWith = ' ' * len(reversedToErase)
        self.durability -= len(replaceWith)

        editedText = reverse(reversedText.replace(reversedToErase, replaceWith, 1))
        self._erase_postconditions(text, editedText)
        return editedText

    def _erase_preconditions(self, toErase, text):
        if type(toErase) is not str:
            raise ValueError('expected toErase to be of type "str"')
        if type(text) is not str:
            raise ValueError('expected text to be of type "str"')

    def _erase_postconditions(self, text, editedText):
        if len(editedText) > len(text):
            raise ValueError('erased text became longer than original text')


# should these two functions be broken out into their own modules?
def reverse(text):
    return text[::-1]


def count_whitespace_chars(text):
    return len([char for char in list(text) if char.isspace()])
