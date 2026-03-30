from machine import Pin
import time

led = Pin(2, Pin.OUT)

print("O progama iniciou!")
print("Coloque 'liga' ou 'desliga' para alterar o estado do led")



while True:
  estado_led = input()
  estado_led_tratado = estado_led.strip().lower()
  if estado_led_tratado == "liga":
    led.value(1)
    print("LED LIGADO")
  elif estado_led_tratado == "desliga":
    led.value(0)
    print("LED DESLIGADO")
  else:
    print("Error")

