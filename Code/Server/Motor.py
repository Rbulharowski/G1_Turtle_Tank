import time
from PCA9685 import PCA9685
import RPi.GPIO as GPIO

#Left Motor
IN1 = 20
IN2 = 21
ENA = 16

#Right Motor
IN3 = 19
IN4 = 26
ENB = 13

class Motor:
    #Set the GPIO port to BCM encoding mode
    GPIO.setmode(GPIO.BCM)

    #Ignore warning information
    GPIO.setwarnings(False)

    def __init__(self):
        global pwm_ENA
        global pwm_ENB
        GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)

        #Set the PWM pin and frequency is 2000hz
        pwm_ENA = GPIO.PWM(ENA, 2000)
        pwm_ENB = GPIO.PWM(ENB, 2000)
        pwm_ENA.start(0)
        pwm_ENB.start(0)

    def duty_range(self,duty1,duty2,duty3,duty4):
        if duty1>4095:
            duty1=4095
        elif duty1<-4095:
            duty1=-4095        
        
        if duty2>4095:
            duty2=4095
        elif duty2<-4095:
            duty2=-4095
            
        if duty3>4095:
            duty3=4095
        elif duty3<-4095:
            duty3=-4095
            
        if duty4>4095:
            duty4=4095
        elif duty4<-4095:
            duty4=-4095
        return duty1,duty2,duty3,duty4


    #Only two motors on G1 Tank, need left and right motor
    def setMotorModel(self,duty1,duty2,duty3,duty4):
        duty1,duty2,duty3,duty4=self.duty_range(duty1,duty2,duty3,duty4)
        setMotorPwm(duty1,duty3)

def setMotorPwm(left, right):
    power = 95
    if(left > 0):
      GPIO.output(IN1, GPIO.HIGH)
      GPIO.output(IN2, GPIO.LOW)
      #pwm_ENA.ChangeDutyCycle(left/41)
      pwm_ENA.ChangeDutyCycle(power)
    elif(left < 0):
      GPIO.output(IN1, GPIO.LOW)
      GPIO.output(IN2, GPIO.HIGH)
      #pwm_ENA.ChangeDutyCycle(-1*left/41)
      pwm_ENA.ChangeDutyCycle(power)
    else:
      GPIO.output(IN1, GPIO.LOW)
      GPIO.output(IN2, GPIO.LOW)

    if(right > 0):
      GPIO.output(IN3, GPIO.HIGH)
      GPIO.output(IN4, GPIO.LOW)
      #pwm_ENB.ChangeDutyCycle(right/41)
      pwm_ENB.ChangeDutyCycle(power)
    elif(right < 0):
      GPIO.output(IN3, GPIO.LOW)
      GPIO.output(IN4, GPIO.HIGH)
      #pwm_ENB.ChangeDutyCycle(-1*right/41)
      pwm_ENB.ChangeDutyCycle(power)
    else:
      GPIO.output(IN3, GPIO.LOW)
      GPIO.output(IN4, GPIO.LOW)
                            
def loop(): 
    PWM.setMotorModel(2000,2000,2000,2000)       #Forward
    time.sleep(3)
    PWM.setMotorModel(-2000,-2000,-2000,-2000)   #Back
    time.sleep(3)
    PWM.setMotorModel(-500,-500,2000,2000)       #Left 
    time.sleep(3)
    PWM.setMotorModel(2000,2000,-500,-500)       #Right    
    time.sleep(3)
    PWM.setMotorModel(0,0,0,0)                   #Stop
    
def destroy():
    PWM.setMotorModel(0,0,0,0) 

if __name__=='__main__':
    try:
        
        PWM=Motor()
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
