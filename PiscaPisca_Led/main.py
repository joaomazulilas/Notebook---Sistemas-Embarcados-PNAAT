from machine import Pin 
import time

led = Pin(22, Pin.OUT)

while True:
   led.value(1)
   time.sleep(1)
   led.value(0)
   time.sleep(1)
