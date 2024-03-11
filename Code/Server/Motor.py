import time
from PCA9685 import PCA9685
class Motor:

    def __init__(self):
        self.pwm = PCA9685()
        self.pwm.setMotorPwm(0,0)

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
        self.pwm.setMotorPwm(duty1,duty3)
                     
PWM=Motor()          
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
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
