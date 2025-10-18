class BMW:
    def drive(self):
        print("Driving a BMW")

class Ferrari:
    def drive(self):
        print("Driving a Ferrari")

def drive_car(car):
    car.drive()

bmw_car = BMW()
ferrari_car = Ferrari()

drive_car(bmw_car)
drive_car(ferrari_car)