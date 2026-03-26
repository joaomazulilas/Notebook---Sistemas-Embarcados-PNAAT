from machine import Pin, ADC
import time

saida_led1 = Pin(25, Pin.OUT)
saida_led2 = Pin(26, Pin.OUT)
saida_led3 = Pin(27, Pin.OUT)
entrada_potenciometro = ADC(Pin(34))

entrada_potenciometro.atten(ADC.ATTN_11DB)

while True:
 valor_lido = entrada_potenciometro.read()

 saida_led1.value(0)
 saida_led2.value(0)
 saida_led3.value(0)

 if valor_lido > 1365:
    saida_led1.value(1)
 
 if valor_lido > 2730:
    saida_led2.value(1)

 if valor_lido > 4000:
    saida_led3.value(1)
 
 time.sleep(0.1)





