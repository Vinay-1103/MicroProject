class Calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"Square of a number {self.n*self.n}")

    def cube(self):
        print(f"Cube of a number {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"SquareRoot of a number {self.n**1/2}")


a=Calculator(4)
a.square()
a.squareroot()
a.cube()