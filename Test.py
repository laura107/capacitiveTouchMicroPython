from machine import ADC, Pin
import time

# Define the GPIO pin where the analog touch sensor is connected
touch_sensor_pin = 26

# Initialize the ADC pin
touch_sensor = ADC(Pin(touch_sensor_pin))

# Function to map the ADC value to a pressure level (0 to 100)
def map_value(value, from_low, from_high, to_low, to_high):
    return (value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low

while True:
    # Read the raw ADC value (0-65535)
    raw_value = touch_sensor.read_u16()
    
    # Convert the raw value to a pressure level (0-100)
    pressure = map_value(raw_value, 0, 65535, 0, 100)
    
    # Print the pressure level
    print(f"Pressure: {pressure:.2f}")
    
    # Wait for a short period before reading again
    time.sleep(0.1)
