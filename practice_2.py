from tkinter import Y


class people:
    def __init__(self,age):
        self.age = age
    
    def say(self):
        print("hello my name is", self.age)

a=people('rian')
a.say()

class person:
    def __init__(self,friends):
        self.friends=friends

    def name(self):
         print("hey how are you",self.friends)

a1=person('rian')
a2=person('enrique')
a3=person('daksh')
a1.name()
a2.name()
a3.name()   

class check:
    def __init__(self):
        print("This is Constructor")
 
a = check()
print("Worked fine")


class sum:
    def num(self,x,y):
        self.x=x
        self.y=y
        

        
    def addition(self,add):
       add=self.x+self.y
       print(add)

        

    def subtraction(self,sub):
        sub=self.x-self.y
        print(sub)
        
    def multiplication(self,mul):
        mul=self.x*self.y
        print(mul)
    
b=sum(10,20)
b.num()
b.addition()
b.subtraction()
b.multiplication()
