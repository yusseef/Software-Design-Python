import string
import random

# Reduce coupling by make all the car info a dynamic variables 
class VehicleInfo:
    brand : str
    catalogue_price : int
    electric : bool

    
    def __init__(self, brand, catalogue_price, electric):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price
    

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")
    

class Vehicle:
    id : str
    license_plate : str
    info = VehicleInfo

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info
    
    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:
    vehicle_info = {}

    def add_vehicle_info(self, brand, catalogue_price, electric):
        #Dictionary of vehicle info
        self.vehicle_info[brand] = VehicleInfo(brand, catalogue_price, electric)

    def __init__(self):
        self.add_vehicle_info('Tesla 3D', 20000, True)
        self.add_vehicle_info('Nissan gtr', 5000, False)
        self.add_vehicle_info('Volkswagen ID3', 700000, True)
        self.add_vehicle_info('BMW 5', 20000, False)

    

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    # By logic why we don't put a method
    # that creating a vehicle inside our vehicleregistry instead of app ? REDUCING COUPLING
   
    def create_vehicle(self, brand):
        # generate a vehicle id of length 12
        vehicle_id = self.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = self.generate_vehicle_license(vehicle_id)

        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])

class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        # Creata a vehicle registry 
        vehicle = registry.create_vehicle(brand)


        # print out the vehicle registration information
        vehicle.print()

app = Application()
app.register_vehicle("Volkswagen ID3")