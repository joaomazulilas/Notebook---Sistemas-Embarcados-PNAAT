from machine import Pin, I2C
from MPU6050 import MPU6050 # Importa a classe da biblioteca que adicionamos
import time

# --- Configuração do Barramento I2C ---
# O ESP32 possui dois barramentos I2C. Usaremos o de ID=0.
# Pinos SCL=22 e SDA=21 são os padrões para ele em muitas placas.
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# --- Inicialização do Sensor ---
# Cria uma instância do sensor, passando o objeto i2c.
# O endereço do MPU6050 (0x68) é o padrão da biblioteca.
mpu = MPU6050(i2c)

print("Sensor MPU-6050 iniciado. Lendo dados inerciais...")

# --- Loop Principal ---
while True:
    try:
        # A biblioteca fornece um método que lê todos os sensores
        # e já retorna os valores convertidos em um dicionário.
        accel_data = mpu.read_accel_data(True)
        gyro_data = mpu.read_gyro_data()
        temperature = mpu.read_temperature()
        
        # Obtém os valores individuais do dicionário
        accel_x = accel_data["x"]
        accel_y = accel_data["y"]
        accel_z = accel_data["z"]

        giro_x = gyro_data["x"]
        giro_y = gyro_data["y"]
        giro_z = gyro_data["z"]

        # Imprime os dados de forma organizada
        print(f"Acel: X={accel_x:<6.2f} Y={accel_y:<6.2f} Z={accel_z:<6.2f} g | ", end="")
        print(f"Giro: X={giro_x:<6.2f} Y={giro_y:<6.2f} Z={giro_z:<6.2f} °/s | ", end="")
        print(f"Temp: {temperature:.2f} °C")

    except OSError as e:
        print("Erro ao ler o sensor:", e)
    
    time.sleep(0.5)
