class Eraser:
    def erase(self, toErase, text):
        reversedText = reverse(text)
        reversedToErase = reverse(toErase)
        replaceWith = ' ' * len(toErase)

        return reverse(reversedText.replace(reversedToErase, replaceWith, 1))

def reverse(text):
    return text[::-1]