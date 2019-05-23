#!/usr/bin/python3


class Square():

    size = 1

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.size * self.size

    def PermiterOfMySquare(self):
        return self.size * 4

    def __str__(self):
        return "{}/{}".format(self.size, self.size)

if __name__ == "__main__":

    s = Square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
