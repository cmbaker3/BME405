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
    #Blink the LED 5 times with on/off intervals of 500ms
    for i in range (0,5):
        GPIO.output(11,1)
        time.sleep(0.5)
        GPIO.output(11,0)
        time.sleep(0.5)

    # For 5s, read output of light sensor in 100 ms intervals
    # Print the raw value along with the text "bright" or "dark"
    for i in range(0,50):
        light = mcp.read_adc(0)
        if light > 100:
            brightness = "light"
        else: 
            brightness = "dark"
        print (brightness, light)
        time.sleep(0.1)

    #Blink the LED 4 times with on/off intervals of 200 ms
    for i in range(0,4):
        GPIO.output(11,1)
        time.sleep(0.2)
        GPIO.output(11,0)
        time.sleep(0.2)

    # For 5s, read output of sound sensor in 100 ms intervals
    # Turn LED on for 100s if sound sensor is tapped
    for i in range(0,50):
        sound = mcp.read_adc(1)
        print(sound)
        if sound<300:
            GPIO.output(11,1)
            time.sleep(0.1)
            GPIO.output(11,0)
        else:
            time.sleep(0.1)
