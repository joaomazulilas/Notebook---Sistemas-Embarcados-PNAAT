from machine import Pin, ADC
import time

# --- Configuração do ADC ---
# O LDR está conectado ao pino 34
adc_ldr = ADC(Pin(34))
# Configura a atenuação para ler a faixa completa de 0-3.3V
adc_ldr.atten(ADC.ATTN_11DB)

# --- Loop Principal ---
while True:
    # 1. Lê o valor bruto do ADC (0-4095)
    valor_adc = adc_ldr.read()

    # 2. Converte o valor bruto para uma porcentagem (Mapeamento)
    # A leitura mínima em escuridão total não é 0, e a máxima com luz total
    # pode não ser 4095. Vamos usar um mapeamento simples.
    # No Wokwi, os valores costumam ir de ~300 (escuro) a 4095 (claro).
    # Para simplificar, vamos mapear a faixa 0-4095 para 0-100%.
    
    # Fórmula de mapeamento: saida = ((entrada - entrada_min) * (saida_max - saida_min)) / (entrada_max - entrada_min) + saida_min
    # Mapeando [0, 4095] para [0, 100]
    percentual_luz = (valor_adc / 4095) * 100

    # Exibe os resultados no monitor serial
    print(f"Valor ADC: {valor_adc:<4} | Luminosidade: {percentual_luz:.1f} %")
    
    # Aguarda um pouco antes da próxima leitura
    time.sleep(0.5)
