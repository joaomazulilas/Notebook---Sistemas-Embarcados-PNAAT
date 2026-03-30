from machine import Pin, I2C, ADC
import time 
import ssd1306
import dht


led_limite = 25
dht = dht.DHT22(Pin(27))
led = Pin(25, Pin.OUT)
potenc_pin = 34
potenc_adc = ADC(potenc_pin)
potenc_adc.atten(ADC.ATTN_11DB)
i2c = I2C(0, scl=Pin(19), sda=Pin(18))


display_larg = 128
display_altu = 64
oled = ssd1306.SSD1306_I2C(display_larg, display_altu, i2c)


while True:
  dht.measure()

  temperature = dht.temperature()
  humidity = dht.humidity()

  print(f"Temperatura:{temperature}°C, Umidade:{humidity}%")

  potenc_valor = potenc_adc.read()
  led_limite = ((potenc_valor - 0) * (80 - -40) / (4096 - 0) + (-40))
  
  if temperature >= led_limite:
   led.value(1)
  else:
   led.value(0)



  oled.fill(0)
  oled.text("Temp: " + str(temperature) + " C", 0, 0)
  oled.text("Hum: " + str(humidity) + " %", 0, 16)
  oled.text("Limit: " + str(led_limite) + " C", 0, 40)
  oled.show()

  time.sleep(1)


