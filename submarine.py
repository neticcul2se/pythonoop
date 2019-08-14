class Submarine:
    def __init__(self,price):
        self.captain = 'pravit'
        self.sub_name = 'Uncle I'
        self.price = price
        self.kilo = 0

    def Missile(self):
        print("we are Department of Missile")

    def Calcommission(self):
        
        percent = self.price * (10/1000)
        print('Loong you got: {} Million baht'.format(percent))
    def Goto(self,enemypoint,distance):
        print(f"Let's go to {enemypoint} distance :{distance} KM")
        self.kilo= self.kilo+distance
    def Fuel(self):
        deisel = 20
        

kongtabreuw = Submarine(20000)
print(kongtabreuw.captain)
print(kongtabreuw.sub_name)
print('----------------')
print(kongtabreuw.kilo)
kongtabreuw.Goto('China',70000)
print(kongtabreuw.kilo)



kongtabreuw.Calcommission()
print('--------sub no.2 --------')
kongtabbok = Submarine(30000)
kongtabbok.captain='srevara'
print(kongtabbok.captain)



        
