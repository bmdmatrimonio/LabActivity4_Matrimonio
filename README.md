# Lab Activity 4: Design Patterns and Unit Testing

## Design Pattern Justification
This project utilizes the **Factory Method Pattern**. 

### Why this pattern fits:
1. **Decoupling Creation Logic:** The client code does not need to know the specific concrete classes (`CTSensor` or `VoltageSensor`) or their instantiation details. It simply requests a sensor from `SensorFactory`.
2. **Scalability:** Adding a new sensor type (e.g., `PowerSensor`) requires adding a new class and updating the factory method without altering existing object-handling code.
3. **Encapsulation:** Object creation parameters and conditional checks are encapsulated within `SensorFactory.create_sensor()`.

## How to Run the Application & Unit Tests

1. Open your terminal or WSL Ubuntu environment.
2. Navigate to the project directory:
   cd lab_activity_4
3. Run the automated unit tests:
   python3 test_sensors.py