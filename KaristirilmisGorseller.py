# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 21:44:18 2025

@author: Hayrunisa Polat
"""

import cv2
import matplotlib.pyplot as plt

#Görsel Okuma
img1=cv2.imread("agac.jpg")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=cv2.imread("deniz.jpg")
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB) # Görseli rgb renklerine dönüştürmek için

#Boyutlarını eşitleme
img1 = cv2.resize(img1,(600,600))
img2 = cv2.resize(img2,(600,600))

#Karıştırılmış resim
karistirilmisResim = cv2.addWeighted(img1,0.5,img2,0.5,gamma=0) # iki resimi eşit oranda karıştırıyor.
plt.figure()
plt.imshow(karistirilmisResim)

