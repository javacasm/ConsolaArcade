
from pyb import ADC, Pin

import math

def adc2temp(adcValue, res=10000, beta=3300, norm=25.0, normread=10000, zero=273.5):
    sensor = 4096.0*res/adcValue - res
    value = (1.0 / ((math.log(sensor / normread) / beta) + (1.0 / (norm + zero)))) - zero
    return value

adc = ADC(Pin('TEMP'))
adc.read()