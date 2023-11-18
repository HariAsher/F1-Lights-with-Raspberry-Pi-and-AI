import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins connected to the LEDs
led_pins = [17, 18, 27, 22, 23]  # Replace these with the pins you've connected to
buzzer_pin = 20  # Replace with the pin you've connected the buzzer to

# Set up each pin as an output
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # Ensure all LEDs are off to start with

GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.output(buzzer_pin, GPIO.LOW)  # Ensure buzzer is off to start with

# Function to buzz for a specified duration
def buzz(duration):
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(buzzer_pin, GPIO.LOW)

# Function for race start lights out sequence
def race_start_sequence():
    for pin in led_pins:
        GPIO.output(pin, GPIO.HIGH)  # Turn on LED
        buzz(0.5)  # Half second buzz for each light
        time.sleep(1)  # Wait for 1 second

    time.sleep(1)  # Wait for an additional second with all lights on

    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)  # Turn off all LEDs

    print("Race Start Lights Out!")

# Function for formation lap lights sequence
def formation_lap_sequence():
    for pin in led_pins:
        GPIO.output(pin, GPIO.HIGH)  # Turn on LED
        buzz(0.5)  # Half second buzz for each light
        time.sleep(1)  # Wait for 1 second

    for pin in reversed(led_pins):
        GPIO.output(pin, GPIO.LOW)  # Turn off LED in reverse order
        time.sleep(1)  # Wait for 1 second

    print("Formation Lap Lights Out!")

# Execute the sequences
try:
    while True:
        choice = input("Press 'r' for Race Start or 'f' for Formation Lap or 'q' to quit: ")

        if choice == 'r':
            race_start_sequence()
        elif choice == 'f':
            formation_lap_sequence()
        elif choice == 'q':
            break

except KeyboardInterrupt:
    pass

# Cleanup the GPIO on exit
GPIO.cleanup()