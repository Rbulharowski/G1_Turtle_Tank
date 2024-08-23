import time
import RPi.GPIO as GPIO
from Command import COMMAND as cmd

GPIO.setwarnings(False)
Buzzer_Pin = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buzzer_Pin, GPIO.OUT)

class Buzzer:
    def __init__(self):
        GPIO.output(Buzzer_Pin, True)
    
    def run(self, command):
        if command != "0":
            #Turn on the buzzer
            GPIO.output(Buzzer_Pin, False)
        else:
            #Turn off the buzzer
            GPIO.output(Buzzer_Pin, True)

if __name__ == '__main__':
    try:
        buzzer = Buzzer()
        buzzer.run('1')
        time.sleep(3)
        buzzer.run('0')
    finally:
        GPIO.cleanup()  # Reset GPIO pins to a safe state