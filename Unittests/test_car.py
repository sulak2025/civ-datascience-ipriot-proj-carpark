import unittest
from samples_and_snippets.my_Carpark_Manager import MyCarparkManager

class TestMyCarparkManager(unittest.TestCase):
    def setUp(self):
        # Use a dummy callback to test display updates
        self.display_updated = False
        def dummy_update():
            self.display_updated = True
        self.manager = MyCarparkManager(update_display_callback=dummy_update)

    def test_incoming_car_adds_car(self):
        self.manager.incoming_car("ABC123")
        self.assertIn("ABC123", self.manager._cars_in_lot)
        self.assertTrue(self.display_updated)

    def test_outgoing_car_removes_car(self):
        self.manager.incoming_car("XYZ789")
        self.display_updated = False  # Reset flag
        self.manager.outgoing_car("XYZ789")
        self.assertNotIn("XYZ789", self.manager._cars_in_lot)
        self.assertTrue(self.display_updated)

    def test_temperature_reading_updates_temperature(self):
        self.manager.temperature_reading(25.5)
        self.assertEqual(self.manager.temperature, 25.5)
        self.assertTrue(self.display_updated)

    def test_available_spaces(self):
        initial_spaces = self.manager.available_spaces
        self.manager.incoming_car("CAR1")
        self.assertEqual(self.manager.available_spaces, initial_spaces - 1)
        self.manager.outgoing_car("CAR1")
        self.assertEqual(self.manager.available_spaces, initial_spaces)

    def test_invalid_temperature_input(self):
        self.display_updated = False
        self.manager.temperature_reading("not_a_number")
        # Should not update temperature or call display
        self.assertFalse(self.display_updated)

if __name__ == '__main__':
    unittest.main()