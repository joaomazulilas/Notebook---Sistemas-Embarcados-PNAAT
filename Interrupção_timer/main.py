from machine import Pin, Timer
import time

led = Pin(21, Pin.OUT)

def pisca_led(timer_obj):
  led.value(not led.value())

timer = Timer(0)

timer.init(period=200, mode=Timer.PERIODIC, callback=pisca_led)

print("INICIANDO CONTAGEM")
contador = 0
while True:
  contador += 1
  print("Contagem:", contador)
  time.sleep(1)

