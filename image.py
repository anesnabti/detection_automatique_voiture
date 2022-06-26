 # -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:48:41 2021

@author: 33660
"""

import cv2
import numpy as np


def creer_coordonnee (image, tab) : 
    pente,ordonnee_origine = tab
    y1 =int(image.shape[0])
    y2 =int(y1*3/5)
    x1 =int((y1-ordonnee_origine)/pente)
    x2 =int((y2-ordonnee_origine)/pente)
    
    return [[x1,y1,x2,y2]]
    
    

            
            
def moyenne_lignes_origine (image, lignes) :
    ajustement_gauche= []
    ajustement_droit =[]
    
    if lignes is None : 
        return None 
    for i in lignes :
       x1,y1,x2,y2= i.reshape(4)
       parametre = np.polyfit ((x1,x2),(y1,y2),1)
       pente= parametre [0]
       ordonnee_origine= parametre [1]
       if pente < 0 :
           ajustement_gauche.append((pente,ordonnee_origine))
       else :
            ajustement_droit.append((pente,ordonnee_origine))
   
    moyenne_ajustement_gauche= np.average(ajustement_gauche,axis=0)
    moyenne_ajustement_droit= np.average(ajustement_droit, axis=0)
    ligne_gauche= creer_coordonnee(image,moyenne_ajustement_gauche)
    ligne_droite= creer_coordonnee(image,moyenne_ajustement_droit)       
   
    return np.array([ligne_gauche , ligne_droite])


def canny (img):
    image_gris= cv2.cvtColor (img,cv2.COLOR_RGB2GRAY )
    image_filt= cv2.GaussianBlur(image_gris,(5,5),0)
    canny = cv2.Canny(image_filt,50,150)
    return canny


def region_interet (image):
    hauteur =image.shape[0]
    mask= np.zeros_like(image)
    triangle= np.array([[
    (200,hauteur),
    (550,250),
    (1000,hauteur),]],np.int32)
    cv2.fillPoly (mask,triangle,255)
    image_masquee= cv2.bitwise_and(mask,image)
    
    return image_masquee


def afficher_lignes (image, lignes):
    traits_image= np.zeros_like(image)
    if lignes is not None : 
        for i in lignes :
            x1,y1,x2,y2 = i.reshape(4)
            trace_ligne= cv2.line(traits_image, (x1,y1), (x2,y2), (255,0,0),10)
     
    return traits_image        

    
        


