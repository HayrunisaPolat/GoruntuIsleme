# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 23:21:16 2025

@author: Hayrunisa Polat
"""

import cv2
import numpy as np

#Fotoğrafı  içe aktarma
img = cv2.imread("araba.jpg")
img= cv2.resize(img,(700,700))
cv2.imshow("Orijinal Gorsel", img)

#Yatay Olarak Görseli Birleştirme
yatay = np.hstack((img,img))
cv2.imshow("Yatay Eksende Birlestirme", yatay)

#Dikey Olarak Görseli Birleştirme
dikey = np.vstack((img,img))
cv2.imshow("Dikey Eksende Birlestirme", dikey)
