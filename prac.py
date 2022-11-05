for i in range(1,10):
    print(i)

a=['rian','shrey','jeremy']
b=['sanjay','enrique','monika']
for x in a:
    for y in b:
        print(y,x)

# functions

def myfunction():
    print('hello world')
myfunction() 

def func(fname):
    print(fname + ' macwan')
func('rian')
func('sanjay')
func('monika')
def myfunc(fname,lname):
    print(fname + ' '+ lname)
myfunc('rian','macwan')

def my_functio(*kids):
  print("The youngest child is " + kids[1])

my_functio("Emil", "Tobias", "Linus")

def my_funct(**kid):
  print("His last name is " + kid["fname"])

my_funct(fname = "Tobias", lname = "Refsnes")


def count(country='india'):
    print("i am from " + country)
count('america')
count('austrilia')
count()
count('europe')
x = lambda a : a + 10
print(x(5))
def name(self,name,rollno):
    self.name=name
    self.rollno=rollno
