class Car:
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
    def display(self):
        print(f"{self.year} {self.name} {self.model}")
class ElectricCar(Car):
    def __init__(self,name,model,year,battery):
        self.name = name
        self.model = model
        self.year = year
        self.battery = battery
    def ElcDisplay(self):
        print(f"Battery Capacity:{self.battery} kWh")
class GasCar(Car):
    def __init__(self,name,model,year,fuel):
        self.name = name
        self.model = model
        self.year = year
        self.fuel = fuel
    def Gasdisplay(self):
        print(f"Fuel Efficiency:{self.fuel} kWh")
cartype = input("Enter Car Type (Electric/Gas): ")
name = input("Enter Name: ")
model = input("Enter Model: ")
year = int(input("Enter Year: "))
if cartype.upper() == "ELECTRIC":
    battery = int(input("Enter Battery Capacity {kWh}: "))
    elc = ElectricCar(name,model,year,battery)
    print("Car Information:")
    elc.display()
    elc.ElcDisplay()
if cartype.upper() == "GAS":
    gas = int(input("Enter Fuel Efficiency (MPG): "))
    gc = GasCar(name,model,year,gas)
    print("Car Information:")
    gc.display()
    gc.Gasdisplay()
 




