from machine import Pin, PWM
import time 

pino_servo = 25
frequencia = 50

pwm_servo = PWM(Pin(pino_servo), freq=frequencia)

def rotaçao(angulo):
  if 0 <= angulo <= 180:
    transform_duty = int(1638 + (angulo / 180) * (8140 - 1638))
    pwm_servo.duty_u16(transform_duty)
  else:
   print("ERROR")


print("INICIANDO SERVO MOTOR")

while True:
  rotaçao(0)
  time.sleep(2)

  rotaçao(90)
  time.sleep(2)

  rotaçao(180)
  time.sleep(2)
