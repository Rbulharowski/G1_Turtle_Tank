#!/usr/bin/python

import time
import math
import RPi.GPIO as GPIO

#Definition of  motor pins 

#Left Motor
IN1 = 20
IN2 = 21
ENA = 16

#Right Motor
IN3 = 19
IN4 = 26
ENB = 13

#Definition of servo pin
ServoPin0 = 23
ServoPin1 = 11

class PCA9685:

  #Set the GPIO port to BCM encoding mode
  GPIO.setmode(GPIO.BCM)

  #Ignore warning information
  GPIO.setwarnings(False)


  def __init__(self,input):
    if input == 0:
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
    else:
      global pwm_servo0
      global pwm_servo1
      GPIO.setup(ServoPin0, GPIO.OUT)
      GPIO.setup(ServoPin1, GPIO.OUT)

      #Set the servo frequency to 50 Hz
      pwm_servo0 = GPIO.PWM(ServoPin0, 50)
      pwm_servo1 = GPIO.PWM(ServoPin1, 50)
      pwm_servo0.start(0)
      pwm_servo1.start(0)

  def setMotorPwm(self, left, right):
    if(left > 0):
      GPIO.output(IN1, GPIO.HIGH)
      GPIO.output(IN2, GPIO.LOW)
      pwm_ENA.ChangeDutyCycle(left/41)
    elif(left < 0):
      GPIO.output(IN1, GPIO.LOW)
      GPIO.output(IN2, GPIO.HIGH)
      pwm_ENA.ChangeDutyCycle(-1*left/41)
    else:
      GPIO.output(IN1, GPIO.LOW)
      GPIO.output(IN2, GPIO.LOW)

    if(right > 0):
      GPIO.output(IN3, GPIO.HIGH)
      GPIO.output(IN4, GPIO.LOW)
      pwm_ENB.ChangeDutyCycle(right/41)
    elif(right < 0):
      GPIO.output(IN3, GPIO.LOW)
      GPIO.output(IN4, GPIO.HIGH)
      pwm_ENB.ChangeDutyCycle(-1*right/41)
    else:
      GPIO.output(IN3, GPIO.LOW)
      GPIO.output(IN4, GPIO.LOW)

  
  def setServoPulse(self,channel, pulse):
    if(channel == 8):
      pwm_servo0.ChangeDutyCycle(pulse)
      time.sleep(0.1)
      pwm_servo0.ChangeDutyCycle(0)
    elif (channel == 9):
      pwm_servo1.ChangeDutyCycle(pulse)
      time.sleep(0.1)
      pwm_servo0.ChangeDutyCycle(0)

if __name__=='__main__':
    pass
    
      
