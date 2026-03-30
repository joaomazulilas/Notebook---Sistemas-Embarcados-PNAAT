from machine import Pin
import time

# --- Configuração dos Pinos ---
trigger_pin = Pin(12, Pin.OUT)
echo_pin = Pin(14, Pin.IN)

print("Sensor Ultrassônico iniciado. Medindo distância...")

# --- Loop Principal ---
while True:
    # --- Passo 1: Enviar o pulso de Trigger ---
    # Garante que o pino de trigger comece em nível baixo
    trigger_pin.value(0)
    time.sleep_us(2)
    # Envia um pulso de 10 microssegundos para o pino de trigger
    trigger_pin.value(1)
    time.sleep_us(10)
    trigger_pin.value(0)

    # --- Passo 2: Medir a duração do pulso de Echo ---
    # A precisão aqui é fundamental, por isso usamos 'ticks_us' para microssegundos.
    
    # Espera o pino de echo subir para ALTO (início da medição)
    # Adicionamos um limite para não travar o programa se não houver eco
    timeout_start = time.ticks_us()
    while echo_pin.value() == 0:
        # Se esperar demais, desiste
        if time.ticks_diff(time.ticks_us(), timeout_start) > 10000:
            break
            
    # Se o loop acima não estourou o timeout
    if echo_pin.value() == 1:
        # Marca o tempo de início do pulso
        tempo_inicio = time.ticks_us()

        # Espera o pino de echo descer para BAIXO (fim da medição)
        while echo_pin.value() == 1:
            # Se o pulso for longo demais (objeto muito longe ou sem objeto), desiste
            if time.ticks_diff(time.ticks_us(), tempo_inicio) > 23200: # ~4 metros
                break

        # Marca o tempo de fim do pulso
        tempo_fim = time.ticks_us()

        # Calcula a duração do pulso em microssegundos
        duracao = time.ticks_diff(tempo_fim, tempo_inicio)

        # --- Passo 3: Calcular a distância ---
        # Distância (cm) = (duração * velocidade do som em cm/µs) / 2
        distancia_cm = (duracao * 0.0343) / 2

        # Exibe o resultado no monitor serial
        print(f"Distância: {distancia_cm:.2f} cm")
    else:
        print("Erro: Eco não detectado.")

    # Aguarda um pouco antes da próxima medição
    time.sleep(0.5)
