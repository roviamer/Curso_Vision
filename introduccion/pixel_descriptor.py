# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:08:10 2023

@author: JaimesPita
"""

import cv2

import cv2
import numpy as np

imagen=cv2.imread(".\imagenes\hormigas.jpg",1)
imagen_bn=np.zeros((imagen.shape[0],imagen.shape[1]))


               
for x in range(imagen.shape[0]):
    for y in range(imagen.shape[1]):
        if ((50<imagen[x,y,0]<90)  and (50<imagen[x,y,1]<90) and (100<imagen[x,y,2]<145)):
            imagen_bn[x,y]=1;
           
cv2.imshow('img',imagen_bn)
cv2.waitKey(0)