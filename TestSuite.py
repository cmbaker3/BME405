# Team Members: Chur Tam, Cathy Zhu
# Github Repo: git@github.com:Churachi/lab07.git

import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)

# Hardware SPI Configuration
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


while True:
    # For 5s, read output of sound sensor in 100 ms intervals (0.25 ms)
    for i in range(0,50):
        sound = mcp.read_adc(1)
        print(sound)            
        time.sleep(0.00025)
