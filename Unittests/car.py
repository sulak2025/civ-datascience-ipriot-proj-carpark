from datetime import datetime

class Car:
    def __init__(self, license_plate, model):
        self.license_plate = license_plate
        self.model = model
        self.entry_time = None
        self.exit_time = None

    def enter(self):
        self.entry_time = datetime.now()

    def exit(self):
        self.exit_time = datetime.now()

    def get_parking_duration(self):
        if self.entry_time and self.exit_time:
            return self.exit_time - self.entry_time
        return None