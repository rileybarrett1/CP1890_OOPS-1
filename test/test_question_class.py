class Rectangle:

    # setting my intial height and width to 0
    def __init__(self):
        self.width = 0
        self.height = 0

    @property
    def area(self): return self
    @area.setter

    # setting the area
    @area.setter
    def area(self,value):
        self.width = int()
        self.height = int()
        self.width, self.height = self.area

    # setting the perimeter
    @property
    def perimeter(self):
        return 2*self.width+2*self.height

    def _is_square(self):
        if self.width == 0 or self.height == 0:
            return False
        elif self.width != self.height:
            return False
        else:
            return True
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height}'

