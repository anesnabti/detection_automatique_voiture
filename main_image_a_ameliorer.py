# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:45:05 2022

@author: 33660
"""

from image import *
import cv2
import numpy as np


i=cv2.imread('image-route0.jpg')
copy_image= np.copy(i)

canny= canny (copy_image)
image_coupee = region_interet (canny)
lignes= cv2.HoughLinesP(image_coupee, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
ligne_moyenne= moyenne_lignes_origine(copy_image, lignes)
traits_image= afficher_lignes (i,ligne_moyenne)  
trace_image= cv2.addWeighted(copy_image, 0.8, traits_image, 1, 1) 
        
cv2.imshow('traits',ligne_moyenne)
cv2.waitKey(0)