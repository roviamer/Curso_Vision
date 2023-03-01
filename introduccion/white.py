# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:01:23 2023

@author: JaimesPita
"""

import cv2
import numpy as np

#def white_patch(imagen):


imagenO=cv2.imread('./imagenes/manos.jpg')
imagen1=np.copy(imagenO)
imagen2=np.copy(imagenO)
imagen3=np.copy(imagenO)
imagen3[:,:,0]=imagenO[:,:,0]+50
imagen2[:,:,1]=imagenO[:,:,1]+40
imagen1[:,:,2]=imagenO[:,:,2]+20


# imagenc=cv2.hconcat([imagenO,imagen1,imagen2,imagen3] )
# #magen=cv2.hconcat([imagenO,imagen1,imagen2,imagen3] )
# cv2.imshow('manos',imagenc)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#white_patch(imagen1)
#white_patch(imagen2)
#white_patch(imagen3)
Bmax=np.max(imagen1[:,:,0])
Gmax=np.max(imagen1[:,:,1])
Rmax=np.max(imagen1[:,:,2])
#global imagenW1
imagenW1=np.zeros_like(imagen1).astype(np.float32)
imagen1=imagen1.astype(np.float32)*255.0

imagenW1[:,:,0]=imagen1[:,:,0]/Bmax
imagenW1[:,:,1]=imagen1[:,:,1]/Gmax
imagenW1[:,:,2]=imagen1[:,:,2]/232
# imageng=(imagenO*255).astype(np.uint8)
imagenW1=imagenW1.astype(np.uint8)
imagenc=cv2.hconcat([imagenO,imagenW1] )
cv2.imshow('white',imagenc)
cv2.waitKey(0)
cv2.destroyAllWindows()