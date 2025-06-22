from Unittests.car import Car
from carpark import Carpark
from sensors import EntrySensor, ExitSensor
from display import Display
from weather import get_current_temperature

def main():
    carpark = Carpark(total_bays=10)
    entry_sensor = EntrySensor()
    exit_sensor = ExitSensor()
    display = Display()

    car1 = Car("1ABC123", "Toyota Corolla")
    car2 = Car("2XYZ456", "Tesla Model 3")

    # Simulate car entry
    entry_sensor.detect_entry(car1, carpark)
    entry_sensor.detect_entry(car2, carpark)

    # Update display
    temperature = get_current_temperature()
    display.update_display(carpark.available_bays(), temperature)

    # Simulate car exit
    exit_sensor.detect_exit("1ABC123", carpark)

    # Update display again
    temperature = get_current_temperature()
    display.update_display(carpark.available_bays(), temperature)

if __name__ == "__main__":
    main()