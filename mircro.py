from machine import Pin
import time

# Define the GPIO pin where the touch sensor is connected
touch_sensor_pin = 15

# Initialize the touch sensor pin as an input
touch_sensor = Pin(touch_sensor_pin, Pin.IN)

while True:
    # Read the state of the touch sensor
    touch_state = touch_sensor.value()

    # Print the touch state
    if touch_state:
        print("Touched")
    else:
        print("Not Touched")
    
    # Wait for a short period before reading again
    time.sleep(0.1)
