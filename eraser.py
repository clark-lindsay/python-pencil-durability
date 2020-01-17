class Eraser:
    def __init__(self, durability = 100):
        self.durability = durability

    def erase(self, toErase, text):
        reversedText = reverse(text)
        reversedToErase = reverse(toErase)[:self.durability + count_whitespace_chars(toErase)]
        replaceWith = ' ' * len(reversedToErase)

        self.durability -= len(replaceWith)
        return reverse(reversedText.replace(reversedToErase, replaceWith, 1))

def reverse(text):
    return text[::-1]

def count_whitespace_chars(text):
    return len([char for char in list(text) if char.isspace()])