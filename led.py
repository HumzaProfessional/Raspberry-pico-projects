from machine import Pin
import time

led = Pin(25, Pin.OUT) # 25 is the pin the led's negative terminal is connnected to. Pin.OUT is any ground pin.

led.on() # Led turns on for the first time

time.sleep(.25) # Led stay on for .25 seconds
led.off() # Led turns off
time.sleep(.25) # Led stays off for .25 seconds
led.on() # Led turns on again
time.sleep(.25)
led.off()
time.sleep( .25)
led.on()
print('This is Raspberry PICO')



