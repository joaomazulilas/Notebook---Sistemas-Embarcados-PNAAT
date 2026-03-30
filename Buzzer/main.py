from machine import Pin, PWM
import time

pino_buzzer = 25

pwm_buzzer = PWM(Pin(pino_buzzer))

NOTAS = {
    'F#4': 370, 'G4': 392, 'A4': 440, 'B4': 494, 
    'C5': 523, 'D5': 587
}
SILENCIO = 0

# --- A Melodia ---
# Uma lista de tuplas, onde cada tupla é (nota, duração_em_ms)
melodia = [
    (NOTAS['G4'], 250), (NOTAS['A4'], 250), (NOTAS['B4'], 250), (NOTAS['C5'], 250),
    (NOTAS['D5'], 500), (NOTAS['C5'], 250), (NOTAS['B4'], 500), (NOTAS['A4'], 250),
    (NOTAS['G4'], 500), (NOTAS['B4'], 250), (NOTAS['A4'], 500), (NOTAS['G4'], 250),
    (NOTAS['F#4'], 500), (NOTAS['G4'], 500)
]

def tocar(frequencia, duraçao_ms):
  if frequencia > 0:
   pwm_buzzer.freq(frequencia)
   pwm_buzzer.duty_u16(int(65535 * 0.5))

  time.sleep_ms(duraçao_ms)

  pwm_buzzer.duty_u16(0)
  time.sleep_ms(50)

print("Iniciando a melodia...")
for nota, duracao in melodia:
    tocar(nota, duracao)

print("Melodia finalizada.")
# Desliga o PWM ao final
buzzer.deinit()


