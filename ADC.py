from gpiozero import MCP3008

adc = MCP3008()

def read_analog_values():
    # Read analog values from channels 0 and 1
    analog_value_1 = adc.value  # Channel 0
    analog_value_2 = adc.channel[1].value  # Channel 1
    
    voltage_1 = analog_value_1 * 3.3 #Vref on the ADC
    voltage_2 = analog_value_2 * 3.3
    return voltage_1, voltage_2
