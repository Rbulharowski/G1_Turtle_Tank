# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

#Definition of RGB module pin
LED_R = 22
LED_G = 27
LED_B = 24
class Led:
    #Set the GPIO port to BCM encoding mode
    GPIO.setmode(GPIO.BCM)

    #Ignore warning information
    GPIO.setwarnings(False)
    def __init__(self):
        global On 
        On = False
        #Set the GPIO port to BCM encoding mode.
        GPIO.setmode(GPIO.BCM)

        #RGB pins are initialized into output mode
        GPIO.setup(LED_R, GPIO.OUT)
        GPIO.setup(LED_G, GPIO.OUT)
        GPIO.setup(LED_B, GPIO.OUT)

    def toggleRed(self):
        global On
        if On:
            On = False
            GPIO.output(LED_R, GPIO.LOW)
            GPIO.output(LED_G, GPIO.LOW)
            GPIO.output(LED_B, GPIO.LOW)
        else:
            On = True
            GPIO.output(LED_R, GPIO.HIGH)
            GPIO.output(LED_G, GPIO.LOW)
            GPIO.output(LED_B, GPIO.LOW)


#Display 7 color LED
if __name__=='__main__':
    led = Led()
    while True:
        led.toggleRed()
        time.sleep(1)