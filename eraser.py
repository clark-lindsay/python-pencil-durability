class Eraser:
    def __init__(self, durability=100):
        self.durability = durability

    def erase(self, toErase, text):
        self._erase_preconditions(toErase, text)
        reversedText = reverse(text)
        reversedToErase = reverse(toErase)[:self.durability + count_whitespace_chars(toErase)]
        replaceWith = ' ' * len(reversedToErase)
        self.durability -= len(replaceWith)

        return reverse(reversedText.replace(reversedToErase, replaceWith, 1))

    def _erase_preconditions(self, toErase, text):
        if type(toErase) is not str:
            raise ValueError('expected toErase to be of type "str"')
        if type(text) is not str:
            raise ValueError('expected text to be of type "str"')


def reverse(text):
    return text[::-1]


def count_whitespace_chars(text):
    return len([char for char in list(text) if char.isspace()])
