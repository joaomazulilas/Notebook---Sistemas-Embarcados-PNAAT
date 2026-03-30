from machine import Pin
import time

pin_rele = Pin(15, Pin.OUT)

print("INICIANDO TRABALHO COM RELÉ")

while True:
  print("LIGANDO")
  pin_rele.value(0)
  time.sleep(5)

  print("DESLIGANDO")
  pin_rele.value(1)
  time.sleep(5)
