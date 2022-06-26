# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:45:05 2022

@author: 33660
"""


import numpy as np 
import cv2
from image import *

cap= cv2.VideoCapture('test2.mp4')
while (cap.isOpened()) : 
    _,frame = cap.read()
    canny_image = canny(frame)
    interet_image = region_interet(canny_image)
    hough_image = cv2.HoughLinesP(interet_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    moyenne_image = moyenne_lignes_origine(frame, hough_image)
    video_image = afficher_lignes(frame, moyenne_image)
    video_trace = cv2.addWeighted(frame, 0.8, video_image, 1, 0)
    cv2.imshow('le resultat',video_trace)
    
    if cv2.waitKey(1)  & 0xFF == ord('e'):
        break 
    
cap.release()
cap.destroyAllwindows() 