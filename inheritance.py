


class employee:
    company="google"
     
    def showdetails(self):
        print("this is an emplyoee")

class programmer(employee):
    language ="python"
    def getlanguage(self):
        print(f"the language is {self.employee}")
e=employee()
a=programmer(employee)
e.showdetails()
a.getlanguage()

