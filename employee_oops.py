class employee:
    def __init__(self,name,id,salary):
     self.name = name
     self.id = id
     self.salary = salary

    def getinfo(self):
        print(f"employee name:{self.name} id:{self.id} salary:{self.salary}")

rian = employee("rian","239","20000")
shrey =employee("shrey","245","38888")
rian.getinfo()
shrey.getinfo()

