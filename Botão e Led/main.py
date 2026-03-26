from machine import Pin 
import time

entrada = Pin(14, Pin.IN)
saida_led = Pin(22, Pin.OUT)

while True:
    if entrada.value() == 0:
     saida_led.value(1)
    else:
     saida_led.value(0)

