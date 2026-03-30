import dht
from machine import Pin
import time 

d = dht.DHT22(Pin(15))
print("Sensor DHT22 iniciado. Lendo temperatura e umidade...")

while True:
 try:
   d.measure()  

   temperature = d.temperature()
   humidity = d.humidity()

   print(f"Temperatura:{temperature}°C, Umidade:{humidity}%")

 except OSError as e:
   print("Erro ao ler sensor:", e)

 time.sleep(2)