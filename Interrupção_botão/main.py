from machine import Pin
import time

led = Pin(21, Pin.OUT)
botao = Pin(14, Pin.IN)

botao_precionado = False

def funcao_interrupcao_botao(pino_que_interrompeu):
  global botao_precionado
  if botao_precionado == False:
    botao_precionado = True
    print("INTERRUPÇÃO, BOTÃO PRECIONADO")


botao.irq(trigger=Pin.IRQ_FALLING, handler=funcao_interrupcao_botao)
print("INICIANDO")
contador = 0
while True:
  contador += 1
  print("Loop principal rodando... Contagem:", contador)
  time.sleep(1)

  if botao_precionado:
    print("Loop principal viu a bandeira! Processando o evento do botão...")
    if led.value() == 1:
     led.value(0)
    else:
      led.value(1)
    
    botao_precionado = False