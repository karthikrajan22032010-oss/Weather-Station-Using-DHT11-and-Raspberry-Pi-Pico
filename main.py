import utime as time
time.sleep(2)  # Critical delay for power-on initialization

from machine import SoftI2C, Pin
from pico_i2c_lcd import I2cLcd
from dht import DHT11

# Initialize I2C LCD on GP26/GP27
i2c = SoftI2C(scl=Pin(27), sda=Pin(26), freq=100000)
lcd = I2cLcd(i2c, 0x3F, 2, 16)

# Initialize DHT11 on GP15
sensor_pin = Pin(15, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(sensor_pin)

lcd.clear()
lcd.move_to(0, 0)
lcd.putstr("Weather Station")
lcd.move_to(0, 1)
lcd.putstr("Starting...")
time.sleep(2)

while True:
    try:
        time.sleep(2)
        sensor.measure()
        t = sensor.temperature
        h = sensor.humidity
        
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Temp : " + str(t) + " C")
        lcd.move_to(0, 1)
        lcd.putstr("Humi : " + str(h) + " %")
        
    except Exception:
        time.sleep(1)