from machine import Pin, PWM
import time

frequencia = 1000

pwm_r = PWM(Pin(27), freq=frequencia)
pwm_g = PWM(Pin(25), freq=frequencia)
pwm_b = PWM(Pin(26), freq=frequencia)

cores = [
  (100, 0, 0),
  (0, 100, 0),
  (0, 0, 100),
]

def set_color(r_percent, g_percent, b_percent):
    duty_r = int(r_percent / 100 * 65535)
    duty_g = int(g_percent / 100 * 65535)
    duty_b = int(b_percent / 100 * 65535)

    pwm_r.duty_u16(duty_r)
    pwm_g.duty_u16(duty_g)
    pwm_b.duty_u16(duty_b)


print("Iniciando ciclo de cores do LED RGB...")

while True:
  for cor in cores:
    r, g, b = cor
    print(f"Definindo cor para: R={r}%, G={g}%, B={b}%")
    set_color(r, g, b)
    time.sleep(5)

