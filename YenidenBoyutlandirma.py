# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 22:41:44 2025

@author: Hayrunisa Polat
"""

import cv2

#Fotoğrafı Açma
img = cv2.imread("araba.jpg")
print("Görselin boyutu : ",img.shape)
cv2.imshow("ARABA", img)

#Görselin Boyutunu Değiştirme
imgResized = cv2.resize(img,(500,500))
print("Boyutu degistirilmis görselin boyutu : ",imgResized.shape)
cv2.imshow("Boyutu degistirilmis gorsel", imgResized)

#Görseli Kırpma
imgCropped = img[:800,:800] # yükseklik genişlik  
print("Kırpılmış görselin boyutu : ",imgCropped.shape)
cv2.imshow("Kirpilmis gorsel", imgCropped)