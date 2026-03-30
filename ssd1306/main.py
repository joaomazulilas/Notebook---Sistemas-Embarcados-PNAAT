from machine import Pin, I2C
import ssd1306
import time 

i2c = I2C(0, scl=Pin(21), sda=Pin(22))

oled_largura = 128
oled_altura = 64

oled = ssd1306.SSD1306_I2C(oled_largura, oled_altura, i2c)

print("INICIANDO DISPLAY")

oled.fill(0)
oled.text("Status do Sis.:", 0, 0)
oled.text("Operando...", 10, 16)
oled.text("Contador:", 0, 40)

oled.show()
time.sleep(2)
contador = 0

while True:
  oled.fill(0)
  oled.text("Status do Sis.:", 0, 0)
  oled.text("Operando...", 10, 16)
  oled.text("Contador:", 0, 40)

  oled.text(str(contador), 0, 50)
  oled.show()
  contador = contador + 1
  time.sleep(1)