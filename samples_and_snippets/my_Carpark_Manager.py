from interfaces import CarparkSensorListener, CarparkDataProvider
from datetime import datetime

class MyCarparkManager(CarparkSensorListener, CarparkDataProvider):
    MAX_SPACES = 100

    def __init__(self, update_display_callback=None):
        self._available_spaces = self.MAX_SPACES
        self._temperature = 22.0  # default temperature
        self._current_time = datetime.now()
        self._cars_in_lot = set()
        self._update_display = update_display_callback

    # ----------------------------
    # CarparkDataProvider methods
    # ----------------------------
    @property
    def available_spaces(self) -> int:
        return self.MAX_SPACES - len(self._cars_in_lot)

    @property
    def temperature(self) -> float:
        return self._temperature

    @property
    def current_time(self):
        return datetime.now().strftime("%H:%M:%S")

    def _log_event(self, event_type, license_plate):
        with open('carpark_log_SL.txt', 'a') as log_file:
            log_file.write(f"{datetime.now()} - {event_type}: {license_plate}\n")

     

    # ----------------------------
    # CarparkSensorListener methods
    # ----------------------------
    def incoming_car(self, license_plate: str):
        print(f"[INCOMING] Car with plate {license_plate}")
        self._log_event("INCOMING", license_plate)
        if self._available_spaces > 0 and license_plate not in self._cars_in_lot:
            self._cars_in_lot.add(license_plate)
            if hasattr(self, '_update_display') and self._update_display:
                self._update_display()
        else:
            print(f"[WARNING] Cannot park car {license_plate}: Full or already parked.")

    def outgoing_car(self, license_plate: str):
        print(f"[OUTGOING] Car with plate {license_plate}")
        self._log_event("OUTGOING", license_plate)
        if license_plate in self._cars_in_lot:
            self._cars_in_lot.remove(license_plate)
            if hasattr(self, '_update_display') and self._update_display:
                self._update_display()
        else:
            print(f"[WARNING] Unknown license plate: {license_plate}")

    def temperature_reading(self, temp: float):
        print(f"[TEMP UPDATE] New temperature: {temp:.1f}°C")
        self._temperature = temp

    def update_time(self):
        """Calling this periodically to keep time updated."""
        self._current_time = datetime.now()