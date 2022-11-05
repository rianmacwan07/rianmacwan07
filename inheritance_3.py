class students(object):
    def __innit__(self,id,name):
       self.id=id
       self.name=name

    def display(self):
        print(self.name)
        print(self.id)

    def details(self):
        print("my name is {}".format(self.name))
        print("id {}".format(self.id))

class classes(students):
    def __innit__(self, id, name,marks,lname):
        self.marks=marks
        self.lname=lname

        students.__innit__(self,name,id)

    def details(self):
         print("my name is {}".format(self.name))
         print("id {}".format(self.id))
         print("lname {}".format(self.lname))

a=students("rian",1,100,"macwan")

a.details()
a.display()

        
