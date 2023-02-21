# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:01:23 2023

@author: JaimesPita
"""

import cv2
import numpy as np
imagen=cv2.imread('./imagenes/hormigas.jpg')
imagen1=np.copy(imagen)
imagen1[:,:,0]=imagen[:,:,0]*0.5
