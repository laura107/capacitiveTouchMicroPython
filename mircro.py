from machine import ADC, Pin
import time

# Define the GPIO pin where the analog touch sensor is connected
touch_sensor_pin = 26

# Initialize the ADC pin
touch_sensor = ADC(Pin(touch_sensor_pin))

# Calibrated minimum and maximum values
# Replace these values with your actual calibrated values
min_value = 2000  # Example value when no pressure is applied
max_value = 60000  # Example value when maximum pressure is applied

# Function to map the ADC value to a pressure level (0 to 100)
def map_value(value, from_low, from_high, to_low, to_high):
    return (value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low

while True:
    # Read the raw ADC value (0-65535)
    raw_value = touch_sensor.read_u16()
    
    # Ensure raw_value is within the min_value and max_value range
    if raw_value < min_value:
        raw_value = min_value
    elif raw_value > max_value:
        raw_value = max_value
    
    # Convert the raw value to a pressure level (0-100)
    pressure = map_value(raw_value, min_value, max_value, 0, 100)
    
    # Print the pressure level
    print(f"Pressure: {pressure:.2f}")
    
    # Wait for a short period before reading again
    time.sleep(0.1)
