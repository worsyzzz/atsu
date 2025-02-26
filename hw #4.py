def logger(func):
    def wrapper(*args, **kwargs):
        print (f"Вызов функции: {func.__name__} с аргументами: {func.args}")
        return func(*args, **kwargs)


def greet(name):
    print(f"Hello {name}!")

greet("Алиса")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник {self.width}x{self.width}"

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

rect1 = Rectangle(3,4)
rect2 = Rectangle(2,5)
rect3 = rect1 + rect2

print(rect1)
print(rect2)
print(rect3)