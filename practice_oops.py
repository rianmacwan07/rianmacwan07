class programmer:
    company="microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getinfo(self):
        print(f"the name of the programmer is {self.name} and product is {self.product}")

rian=programmer("rian","facebook")
tommy=programmer("tommy","github")
rian.getinfo()
tommy.getinfo()