class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value: int):
        if value <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value: int):
        if value <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self._height = value
