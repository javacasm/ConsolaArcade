from pyb import ADC, Pin

adc = ADC(Pin('LIGHT'))
adc.read()