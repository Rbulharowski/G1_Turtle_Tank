import time
import RPi.GPIO as GPIO



from PCA9685 import PCA9685
class Servo:
    def __init__(self):
        self.PwmServo = PCA9685()
        #self.PwmServo = PCA9685(0x40, debug=True)
        #self.PwmServo.setPWMFreq(50)
        self.PwmServo.setServoPulse(8,0)
        self.PwmServo.setServoPulse(9,0)
    def setServoPwm(self,channel,pos):
        if channel=='0':
            self.PwmServo.setServoPulse(8,2.5 + 10 * pos/180)
        elif channel=='1':
            self.PwmServo.setServoPulse(9,2.5 + 10 * pos/180)
        elif channel=='2':
            self.PwmServo.setServoPulse(10,2.5 + 10 * pos/180)
        elif channel=='3':
            self.PwmServo.setServoPulse(11,2.5 + 10 * pos/180)
        elif channel=='4':
            self.PwmServo.setServoPulse(12,2.5 + 10 * pos/180)
        elif channel=='5':
            self.PwmServo.setServoPulse(13,2.5 + 10 * pos/180)
        elif channel=='6':
            self.PwmServo.setServoPulse(14,2.5 + 10 * pos/180)
        elif channel=='7':
            self.PwmServo.setServoPulse(15,2.5 + 10 * pos/180)

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

    

    
       



    
