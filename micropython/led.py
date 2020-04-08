from pyb import LED

led = LED(1)  # available LED（1），LED（2）

led.toggle()  # invert the LED state
led.on()      # switch on the LED  
led.off()     # switch off the LED
led.intensity([value])  # value between 0 and 255