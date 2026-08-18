from abc import ABC, abstractmethod


class Sensor(ABC):
    """Abstract Base Class for sensors."""
    def __init__(self, sensor_id: str, name: str):
        self.sensor_id = sensor_id
        self.name = name

    @abstractmethod
    def read_data(self) -> str:
        pass


class CTSensor(Sensor):
    """Implementation for Current Transformer (CT) Sensors."""
    def __init__(self, sensor_id: str, name: str, current_rating: float):
        super().__init__(sensor_id, name)
        self.current_rating = current_rating

    def read_data(self) -> str:
        return f"[CT Sensor {self.sensor_id}] {self.name} - Max Current: {self.current_rating}A"


class VoltageSensor(Sensor):
    """Implementation for Voltage Sensors."""
    def __init__(self, sensor_id: str, name: str, max_voltage: float):
        super().__init__(sensor_id, name)
        self.max_voltage = max_voltage

    def read_data(self) -> str:
        return f"[Voltage Sensor {self.sensor_id}] {self.name} - Max Voltage: {self.max_voltage}V"


class SensorFactory:
    """Encapsulate sensor object creation."""
    @staticmethod
    def create_sensor(sensor_type: str, sensor_id: str, name: str, capacity: float) -> Sensor:
        sensor_type_clean = sensor_type.strip().lower()
        if sensor_type_clean == "ct":
            return CTSensor(sensor_id, name, capacity)
        elif sensor_type_clean == "voltage":
            return VoltageSensor(sensor_id, name, capacity)
        else:
            raise ValueError(f"Unknown sensor type: '{sensor_type}'")