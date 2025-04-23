#!/usr/bin/python 
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import socket
import io
import sys
import struct
from PIL import Image
from multiprocessing import Process
from Command import COMMAND as cmd

class VideoStreaming:
    def __init__(self):
        #self.face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
        self.video_Flag=True
        self.connect_Flag=False
        self.face_x=0
        self.face_y=0
    def StartTcpClient(self,IP):
        self.client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def StopTcpcClient(self):
        try:
            self.client_socket.shutdown(2)
            self.client_socket1.shutdown(2)
            self.client_socket.close()
            self.client_socket1.close()
        except:
            pass

    def IsValidImage4Bytes(self,buf): 
        bValid = True
        if buf[6:10] in (b'JFIF', b'Exif'):     
            if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):
                bValid = False
        else:        
            try:  
                Image.open(io.BytesIO(buf)).verify() 
            except:  
                bValid = False
        return bValid

    """def face_detect(self,img):
        if sys.platform.startswith('win') or sys.platform.startswith('darwin'):
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray,1.3,5)
            if len(faces)>0 :
                for (x,y,w,h) in faces:
                    self.face_x=float(x+w/2.0)
                    self.face_y=float(y+h/2.0)
                    img= cv2.circle(img, (int(self.face_x),int(self.face_y)), int((w+h)/4), (0, 255, 0), 2)
            else:
                self.face_x=0
                self.face_y=0
        cv2.imwrite('video.jpg',img)"""
        
    def streaming(self,ip):
        stream_bytes = b' '
        try:
            self.client_socket.connect((ip, 5000))
        except:
            #print "command port connect failed"
            print("Failed Camera")
            pass
        while True:
            try:
                # Receive frame size
                frame_size = int.from_bytes(self.client_socket.recv(4), byteorder='big')
                
                # Receive frame data
                frame_data = b''
                while len(frame_data) < frame_size:
                    frame_data += self.client_socket.recv(frame_size - len(frame_data))
                    
                # Decode frame from JPEG
                frame_np = cv2.imdecode(np.frombuffer(frame_data, dtype=np.uint8), cv2.IMREAD_COLOR)
                cv2.imwrite('video.jpg',frame_np)
            except Exception as e:
                print ("Failure")
                break
                  
    def sendData(self,s):
        if self.connect_Flag:
            self.client_socket1.send(s.encode('utf-8'))

    def recvData(self):
        data=""
        try:
            data=self.client_socket1.recv(1024).decode('utf-8')
        except:
            pass
        return data

    def socket1_connect(self,ip):
        try:
            self.client_socket1.connect((ip, 8000))
            self.connect_Flag=True
            print ("Connection Successful !")
        except Exception as e:
            print ("Connect to server Failed!: Server IP is right? Server is opened?")
            self.connect_Flag=False

if __name__ == '__main__':
    pass

