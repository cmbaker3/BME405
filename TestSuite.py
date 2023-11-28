import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import numpy as np
from scipy.io.wavfile import write

# using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = 10
GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Hardware SPI Configuration
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#Sample Rate Setup
samplerate = 4000
lst = []
button = False
fileName = 0

while True:
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pressed")
        time.sleep(1)
        button = True
    
    while button == True:
        #sound is the data needed, storing sound in array
        sound = mcp.read_adc(1)
        print(sound)
        lst.append(sound)
        time.sleep(0.00025)

        if GPIO.input(10) == GPIO.HIGH:
            print("I am done recording data, button pressed again")
            time.sleep(1)
            button = False
            print("About to print")
            print(lst)

            # Convert the list to a NumPy array and scale to 16-bit integer range
            array = np.array(lst, dtype=np.int16)

            # Write the array to a WAV file
            write(f"example{fileName}.wav", samplerate, array)

            print("Example %s printed" % str(fileName))
            lst = []
            fileName += 1
            #fileName = fileName + 1
