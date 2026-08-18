import unittest
from sensor_factory import SensorFactory, CTSensor, VoltageSensor


class TestSensorFactory(unittest.TestCase):

    def test_create_ct_sensor(self):
        """Test Case 1: Verify CT Sensor instantiation and data output."""
        sensor = SensorFactory.create_sensor("ct", "S01", "Lab Main CT", 30.0)
        self.assertIsInstance(sensor, CTSensor)
        self.assertEqual(sensor.read_data(), "[CT Sensor S01] Lab Main CT - Max Current: 30.0A")

    def test_create_voltage_sensor(self):
        """Test Case 2: Verify Voltage Sensor instantiation and data output."""
        sensor = SensorFactory.create_sensor("voltage", "S02", "Busbar Voltage", 240.0)
        self.assertIsInstance(sensor, VoltageSensor)
        self.assertEqual(sensor.read_data(), "[Voltage Sensor S02] Busbar Voltage - Max Voltage: 240.0V")

    def test_invalid_sensor_type(self):
        """Test Case 3: Verify ValueError is raised for invalid sensor types."""
        with self.assertRaises(ValueError):
            SensorFactory.create_sensor("temperature", "S03", "Ambient Temp", 100.0)


# --- Sample Output Runs ---
if __name__ == "__main__":
    print("=== Test Case 1: Creating CT Sensor via Factory ===")
    s1 = SensorFactory.create_sensor("ct", "S01", "Lab Main CT", 30.0)
    print(s1.read_data())

    print("\n=== Test Case 2: Creating Voltage Sensor via Factory ===")
    s2 = SensorFactory.create_sensor("voltage", "S02", "Busbar Voltage", 240.0)
    print(s2.read_data())

    print("\n=== Test Case 3: Error Handling for Unsupported Sensor ===")
    try:
        s3 = SensorFactory.create_sensor("temperature", "S03", "Ambient Temp", 100.0)
    except ValueError as e:
        print(f"Error caught: {e}")