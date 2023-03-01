# -*- coding: utf-8 -*-
"""
@author: JaimesPita
"""



import cv2
import numpy as np

class DeteccionObjetosBasico:
    def __init__(self,imagen):
        self.imagen=imagen
        self.x=imagen.shape[0]
        self.y=imagen.shape[1]       
    
    def clasificador_pixel(self):  #Realiza una clasificación  utilizando el descriptor del pixel   
        self.imagen_bn=np.zeros_like(self.imagen,dtype=np.uint8)              
        for x in range(imagen.shape[0]):
            for y in range(imagen.shape[1]):
                if ((fronteras['Bmin']<imagen[x,y,0]<fronteras['Bmax'])  and (fronteras['Gmin']<imagen[x,y,1]<fronteras['Gmax']) and (fronteras['Rmin']<imagen[x,y,2]<fronteras['Rmax'])):
                    self.imagen_bn[x,y,:]=255
        self.mostrar_imagen()
                                    
    def mostrar_imagen(self):
        imagen=cv2.hconcat([self.imagen,self.imagen_bn])
        
        cv2.imshow('img',imagen)
        cv2.waitKey(0)
        
imagen=cv2.imread(".\imagenes\manos.jpg",1)
fronteras={'Bmin':30,'Bmax':90,'Gmin':30,'Gmax':90,'Rmin':80,'Rmax':145}
deteccion1=DeteccionObjetosBasico(imagen)
deteccion1.clasificador_pixel()


