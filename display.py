class Display:
    def __init__(self):
        pass

    def update_display(self, available_bays, temperature):
        print(f"Available Bays: {available_bays}")
        print(f"Current Temperature: {temperature}°C")