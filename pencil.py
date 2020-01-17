class Pencil:
    def __init__(self, point_durability = 100):
        self.point_durability = point_durability

    def write(self, text):
        written_text = ''
        for char in text:
            written_text += self._write_char(char)
        return written_text

    def _write_char(self, char):
        if self.point_durability > 0:
            if not char.isspace():
                if char.isupper():
                    self.point_durability -= 2
                else:   
                    self.point_durability -= 1
            return char
        else:
            return ' '