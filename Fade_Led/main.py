import machine
import time

pin_led = machine.Pin(2)
led_pwm = machine.PWM(pin_led)

led_pwm.freq(1000)

while True:
    
    for duty_cycle in range(1024):
        led_pwm.duty(duty_cycle)
        time.sleep_ms(1)  
    time.sleep_ms(200)
    
    for duty_cycle in range(1023, -1, -1):
        led_pwm.duty(duty_cycle)
        time.sleep_ms(1)  
    time.sleep_ms(200)


