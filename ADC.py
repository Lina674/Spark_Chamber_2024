from gpiozero import MCP3008

adc = MCP3008()

def read_analog_values():
    # Read analog values from channels 0 and 1
    analog_value_1 = adc.value  # Channel 0
    analog_value_2 = adc.channel[1].value  # Channel 1
    return analog_value_1, analog_value_2
