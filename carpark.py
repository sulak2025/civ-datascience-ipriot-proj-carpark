from datetime import datetime
import random

class Carpark:
    def __init__(self, total_bays):
        self.total_bays = total_bays
        self.parking_bays = [None] * total_bays
        self.log = []

    def incoming_car(self, car):
        for i in range(self.total_bays):
            if self.parking_bays[i] is None:
                car.enter()
                self.parking_bays[i] = car
                self.log.append((datetime.now(), 'ENTRY', car.license_plate))
                return True
        return False  # Car park full

    def outgoing_car(self, license_plate):
        for i, parked_car in enumerate(self.parking_bays):
            if parked_car and parked_car.license_plate == license_plate:
                parked_car.exit()
                self.log.append((datetime.now(), 'EXIT', license_plate))
                self.parking_bays[i] = None
                return True
        return False  # Car not found

    def available_bays(self):
        return sum(1 for bay in self.parking_bays if bay is None)

    def current_cars(self):
        return [car for car in self.parking_bays if car is not None]

    def get_current_temperature(self):
    # In practice, read from file or weather API
        return round(random.uniform(18.0, 35.0), 1)