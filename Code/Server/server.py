#!/usr/bin/python 
# -*- coding: utf-8 -*-
import io
import socket
import struct
import time
import cv2
from threading import Condition
import fcntl
import  sys
import threading
from Motor import *
from servo import *
from Led import *
from Buzzer import *
from Thread import *
from Light import *
from Ultrasonic import *
from Line_Tracking import *
from threading import Timer
from threading import Thread
from Command import COMMAND as cmd

class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()

class Server:   
    def __init__(self):
        self.PWM=Motor()
        self.servo=Servo()
        self.led=Led()
        self.buzzer=Buzzer()
        self.light=Light()
        self.tcp_Flag = True
        self.sonic=False
        self.Light=False
        self.Mode = 'one'
        self.endChar='\n'
        self.intervalChar='#'

    def get_interface_ip(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return "192.168.1.3"

    def StartTcpServer(self):
        ### IMPORTANT: Need to update the Host server ip address

        HOST = "192.168.1.3"
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket1 = socket.socket()
        self.server_socket1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
        self.server_socket1.bind((HOST, 8000))
        self.server_socket1.listen(1)
        self.server_socket = socket.socket()
        self.server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
        self.server_socket.bind((HOST, 5000))              
        self.server_socket.listen(1)
        print('Server address: '+HOST) 
        self.buzzer.run(self,'1')
        time.sleep(1)
        self.buzzer.run(self,'0')   
        
    def StopTcpServer(self):
        try:
            self.connection.close()
            self.connection1.close()
        except Exception as e:
            print ('\n'+"No client connection")
         
    def Reset(self):
        self.StopTcpServer()
        self.StartTcpServer()
        self.SendVideo=Thread(target=self.sendvideo)
        self.ReadData=Thread(target=self.readdata)
        self.SendVideo.start()
        self.ReadData.start()
    def send(self,data):
        self.connection1.send(data.encode('utf-8'))    

    def sendvideo(self):
        try:
            self.connection,self.client_address = self.server_socket.accept()
        except:
            pass
        self.server_socket.close()
        print ("socket video connected ... ")
        camera = cv2.VideoCapture(0)
        while True:
            # Read frame from camera
            ret, frame = camera.read()
            
            # Encode frame as JPEG
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]  # Adjust quality as needed
            _, frame_encoded = cv2.imencode('.jpg', frame, encode_param)
            
            # Send frame size
            self.connection.send(len(frame_encoded).to_bytes(4, byteorder='big'))
            
            # Send frame data
            self.connection.send(frame_encoded)
                 
    def stopMode(self):
        try:
            #stop_thread(self.infraredRun)
            self.PWM.setMotorModel(0,0,0,0)
        except:
            pass
        try:
            #stop_thread(self.lightRun)
            self.PWM.setMotorModel(0,0,0,0)
        except:
            pass            
        try:
            #stop_thread(self.ultrasonicRun)
            self.PWM.setMotorModel(0,0,0,0)
            self.servo.setServoPwm('0',90)
            self.servo.setServoPwm('1',90)
        except:
            pass
        
    def readdata(self):
        try:
            try:
                self.connection1,self.client_address1 = self.server_socket1.accept()
                print ("Client connection successful !")
            except:
                print ("Client connect failed")
            restCmd=""
            self.server_socket1.close()
            while True:
                try:
                    AllData=restCmd+self.connection1.recv(1024).decode('utf-8')
                except:
                    if self.tcp_Flag:
                        self.Reset()
                    break
                print(AllData)
                if len(AllData) < 5:
                    restCmd=AllData
                    if restCmd=='' and self.tcp_Flag:
                        self.Reset()
                        break
                restCmd=""
                if AllData=='':
                    break
                else:
                    cmdArray=AllData.split("\n")
                    if(cmdArray[-1] != ""):
                        restCmd=cmdArray[-1]
                        cmdArray=cmdArray[:-1]     
            
                for oneCmd in cmdArray:
                    data=oneCmd.split("#")
                    if data==None:
                        continue
                    elif cmd.CMD_MODE in data:
                        if data[1]=='one' or data[1]=="1":
                            self.stopMode()
                            self.Mode='one'

                    elif (cmd.CMD_MOTOR in data) and self.Mode=='one':
                        try:
                            data1=int(data[1])
                            data2=int(data[2])
                            data3=int(data[3])
                            data4=int(data[4])
                            if data1==None or data2==None or data2==None or data3==None:
                                continue
                            self.PWM.setMotorModel(data1,data2,data3,data4)
                        except:
                            pass
                    elif cmd.CMD_SERVO in data:
                        try:
                            data1=data[1]
                            data2=int(data[2])
                            if data1==None or data2==None:
                                continue
                            self.servo.setServoPwm(data1,data2)
                        except:
                            pass

                    elif cmd.CMD_LED in data:
                        try:
                            self.led.toggleRed()
                        except:
                            pass
                    elif cmd.CMD_BUZZER in data:
                        try:
                            self.buzzer.run(data[1])
                        except:
                            pass
        except Exception as e: 
            print(e)
        self.StopTcpServer()    
if __name__=='__main__':
    pass
