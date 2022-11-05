class calculator:
    def __init__(self,num):
         self.number = num 

    def square(self):
        print(f"the value of {self.number} square is {self.number**2}")


    def squareroot(self):
        print(f"squreroot of {self.number} is {self.number**0.5}")
    def cube(self):
        print(f"the cube of {self.number} is {self.number**3}")
    
    @staticmethod
    def greet():
        print("hello")
a=calculator(8)
a.greet()
a.square()
a.squareroot()
a.cube()