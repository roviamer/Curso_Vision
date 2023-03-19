# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 07:34:04 2023

@author: JaimesPita
"""

from deepface import  DeepFace
import cv2 

imagen1=cv2.imread('imagenes/yo.jpg')
imagen2=cv2.imread('imagenes/yo.jpg')
imagen1=cv2.resize(imagen1,(600,600))
cam=cv2.VideoCapture(0)


while True:
    ret,frame=cam.read()
    if ret:
        cv2.imwrite('imagen1.jpg',frame)
        result=DeepFace.verify('imagen1.jpg','imagenes/yo.jpg')
        frame=cv2.resize(frame,(600,600))
        imagen=cv2.hconcat([imagen1,frame])
        cv2.imshow('imagen1',imagen)
        print(result)
        
    if cv2.waitKey(1)==ord('s'):
        break





cam.release()
# cv2.imshow('resultado',imagen)
# cv2.waitKey(0)
cv2.destroyAllWindows()