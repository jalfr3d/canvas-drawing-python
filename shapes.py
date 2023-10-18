class Rectangle:
    """A rectangle shape that can be drawn ona a canvas object"""
    def __init__(self, x, y, height, width, color):
        self.color = color
        self.height = height
        self.width = width
        self.y = y
        self.x = x

    def draw(self, canvas):
        """Draws itself into the canvas"""
        # Change a slice of the array with new values
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:
    """A square shape that can be drawn on a Canvas object"""
    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw(self, canvas):
        """Draws itselft into the canvas"""
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color
