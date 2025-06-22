class EntrySensor:
    def detect_entry(self, car, carpark):
        return carpark.add_car(car)

class ExitSensor:
    def detect_exit(self, license_plate, carpark):
        return carpark.remove_car(license_plate)