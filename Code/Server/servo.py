import time
import RPi.GPIO as GPIO

#Definition of servo pin
ServoPin0 = 23
ServoPin1 = 11

#from PCA9685 import PCA9685

class Servo:
    #Set the GPIO port to BCM encoding mode
    GPIO.setmode(GPIO.BCM)

    #Ignore warning information
    GPIO.setwarnings(False)

    def __init__(self):
        #Ignore warning information
        GPIO.setwarnings(False)
        global pwm_servo0
        global pwm_servo1
        GPIO.setup(ServoPin0, GPIO.OUT)
        GPIO.setup(ServoPin1, GPIO.OUT)

        #Set the servo frequency to 50 Hz
        pwm_servo0 = GPIO.PWM(ServoPin0, 50)
        pwm_servo1 = GPIO.PWM(ServoPin1, 50)
        pwm_servo0.start(0)
        pwm_servo1.start(0)

        #self.PwmServo = PCA9685(1)
        setServoPulse(8,0)
        setServoPulse(9,0)

    def setServoPwm(self,channel,pos):
        if channel=='0':
            setServoPulse(8,10-(pos/20))
        elif channel=='1':
            setServoPulse(9,(-1 + 10 * pos/180))
            print((2.5 + 10 * pos/180))
        elif channel=='2':
            setServoPulse(10,2.5 + 10 * pos/180)
        elif channel=='3':
            setServoPulse(11,2.5 + 10 * pos/180)
        elif channel=='4':
            setServoPulse(12,2.5 + 10 * pos/180)
        elif channel=='5':
            setServoPulse(13,2.5 + 10 * pos/180)
        elif channel=='6':
            setServoPulse(14,2.5 + 10 * pos/180)
        elif channel=='7':
            setServoPulse(15,2.5 + 10 * pos/180)

def setServoPulse(channel, pulse):
    if(channel == 8):
      pwm_servo0.ChangeDutyCycle(pulse)
      time.sleep(0.1)
      pwm_servo0.ChangeDutyCycle(0)
    elif (channel == 9):
      pwm_servo1.ChangeDutyCycle(pulse)
      time.sleep(0.1)
      pwm_servo0.ChangeDutyCycle(0)

# Main program logic follows:
if __name__ == '__main__':
    print("Now servos will rotate to 90°.") 
    print("If they have already been at 90°, nothing will be observed.")
    print("Please keep the program running when installing the servos.")
    print("After that, you can press ctrl-C to end the program.")
    pwm=Servo()

    while True:
        counting = 5
        while (counting < 100):
            pwm.setServoPwm('1',counting)
            time.sleep(0.7)
            counting += 10
    #    try :
            #pwm.setServoPwm('0',90)
            #pwm.setServoPwm('1',90)
    #    except KeyboardInterrupt:
    #        print ("\nEnd of program")
    #        break

    

    
       



    
