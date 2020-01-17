class Eraser:
    def erase(self, toErase, text):
        editedText = text[::-1].replace(toErase[::-1], ' ' * len(toErase), 1)
        return editedText[::-1]