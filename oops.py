class railwayform:
    formtype="railwayform"
    def printdata(self):
        print(f"name is{self.name}")
        print(f"rain is{self.train}")

riansapplication=railwayform()
riansapplication.name="rian"
riansapplication.train="rajdhani express"
riansapplication.printdata()
class remote():
    pass
class player:
    def moveright(self):
        pass
    def moveleft(self):
        pass
    def movetop(self):
        pass
remote1=remote()
player1=player()
if(remote.isleftpressed()):
    player1.moveleft()

'''class employee():
    company="facebook"
    def getsalary(self):
     print("salary is 100k")
rian=employee()
rian.salary=10000
rian.getsalary()
shrey=employee()
shrey.salary=10000
shrey.getsalary()
print("salary is 500k")
daksh=employee()
daksh.salary=1000'''
