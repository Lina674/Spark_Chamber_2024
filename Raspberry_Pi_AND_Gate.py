import time
import RPi.GPIO as GPIO

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)  # Pin 23 as output for AND gate result

# Function to generate digital pulse
def generate_pulse(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)  # Pulse duration
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        # Read analog signal 1 using ADC (example value)
        analog_value_1 = read_analog_value_1()

        threshold_1 = 50  # mV
        if analog_value_1 > threshold_1:
            generate_pulse(21)  # Generate pulse on pin 21

        analog_value_2 = read_analog_value_2()

        if analog_value_2 > threshold_1:
            generate_pulse(22)  # Generate pulse on pin 22

        # AND gate
        if analog_value_1 > threshold_1 and analog_value_2 > threshold_1:
            GPIO.output(23, GPIO.HIGH)  # Output 1
        else:
            GPIO.output(23, GPIO.LOW)  # Output 0

        time.sleep(0.1)  

except KeyboardInterrupt:
    GPIO.cleanup()
