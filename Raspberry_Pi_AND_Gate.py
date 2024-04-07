import time
import RPi.GPIO as GPIO
from adc_module import read_analog_values

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)  # D pulse 1
GPIO.setup(22, GPIO.OUT)  # D pulse 2
GPIO.setup(23, GPIO.OUT)  # Pin 23 as output for AND gate result

def generate_pulse(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)  # Pulse duration
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        analog_value_1, analog_value_2 = read_analog_values()
        
        threshold_1 = 50  # mV
        
        if analog_value_1 > threshold_1:
            generate_pulse(21)  # Generate D pulse on pin 21

        if analog_value_2 > threshold_1:
            generate_pulse(22)  # Generate D pulse on pin 22

        # AND gate
        if analog_value_1 > threshold_1 and analog_value_2 > threshold_1:
            GPIO.output(23, GPIO.HIGH)  # Output 1
        else:
            GPIO.output(23, GPIO.LOW)  # Output 0

        time.sleep(0.1)  

except KeyboardInterrupt:
    GPIO.cleanup()
