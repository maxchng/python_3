class calculator:
    """Calculator Class"""
    def __init__(self, object):
        """Constructor for calculator"""
        self.object = object

    def __add__(self, object) -> None:
        """Addition"""
        self.object = [num + object for num in self.object]
        print(self.object)

    def __mul__(self, object) -> None:
        """Multiplication"""
        self.object = [num * object for num in self.object]
        print(self.object)

    def __sub__(self, object) -> None:
        """Subtraction"""
        self.object = [num - object for num in self.object]
        print(self.object)

    def __truediv__(self, object) -> None:
        """Division"""
        if object == 0:
            print("Don't Divide by Zero!!")
        else:
            self.object = [num / object for num in self.object]
            print(self.object)
