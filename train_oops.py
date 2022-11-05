


class train:
    def __init__(self,name,fare,seats):
        self.name= name
        self.fare= fare
        self.seats=seats
    def getstatus(self):
        print(f"the name of the train is {self.name}")
        print(f"the seats of the train is {self.seats}")
       
    
    def fareinfo(self):
        print(f"the name of the train is {self.fare}")
intercity=train("intercity express:14015",90,300)
intercity.getstatus()
intercity.fareinfo()