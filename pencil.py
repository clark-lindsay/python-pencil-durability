class Pencil:
    def __init__(self, point_durability = 100):
        self.point_durability = point_durability

    def write(self, text):
        written_text = ''
        for char in text:
            if self.point_durability > 0 and not char.isspace():
                written_text = written_text + char
                self.point_durability -= 1
            else:
                written_text = written_text + ' '
        return written_text