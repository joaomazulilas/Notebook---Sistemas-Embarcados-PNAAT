from machine import Pin, ADC
from math import log
import time

adc_pin = ADC(Pin(34))
adc_pin.atten(ADC.ATTN_11DB)

R_DIVISOR = 10000
R_NOMINAL = 10000
TEMP_NOMINAL_K = 298.15
BETA = 3950

while True:
  valor_adc = adc_pin.read()
  tensao = (valor_adc / 4095) * 3.3
    
  if tensao == 3.3:
     resistencia_ntc = 0.00001
  else:
     resistencia_ntc = (tensao * R_DIVISOR) / (3.3 - tensao)

    # Fórmula: 1/T = 1/T₀ + (1/β) * ln(R/R₀)
    # Reorganizando: T = 1 / ( (1/T₀) + (1/β) * ln(R/R₀) )
  temp_kelvin = 1 / ( (1 / TEMP_NOMINAL_K) + (1 / BETA) * log(resistencia_ntc / R_NOMINAL) )
    
    # Converte de Kelvin para Celsius
  temp_celsius = temp_kelvin - 273.15

  print(f"Valor ADC: {valor_adc} | Resistência: {resistencia_ntc:.0f} Ohms | Temperatura: {temp_celsius:.2f} °C")
    
    # Aguarda um segundo antes da próxima leitura
  time.sleep(1)