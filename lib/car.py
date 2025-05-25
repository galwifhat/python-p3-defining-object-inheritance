from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    
veh2 = Car(5,6)
print(veh2.go())
print(veh2.fill_up_tank())