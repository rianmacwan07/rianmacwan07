


class animal:
    def intro(self):
        print("this is an animal")
    
    def walk(self):
        print("animals can walk")

class lion(animal):
    def walk(self):
        print("lion can walk")

class tiger(animal):
    def walk(self):
        print("tiger can also walk")

a = animal()
a_lion = lion()
a_tiger = tiger()

a.intro()
a.walk()

a_lion.intro()
a_lion.walk()

a_tiger.intro()
a_tiger.walk()
