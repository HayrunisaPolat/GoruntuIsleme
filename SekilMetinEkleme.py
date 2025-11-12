# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 23:01:48 2025

@author: Hayrunisa Polat
"""

import cv2
import numpy as np

# Resim Oluşturma
img = np.zeros((512,512,3),np.uint8) # pikseller sıfırdan oluştuğu için görsel siyah olacaktır.
cv2.imshow("Resim", img)

#Çizik Oluşturma
#resim , başlangıç noktası , bitiş noktası ,kalınlık
img2 = cv2.line(img, (0,0), (512,512),(180,105,255),3)
cv2.imshow("Sekil", img)

#Dikdörtgen Oluşturma
#resim , başlangıç noktası , bitiş noktası 
cv2.rectangle(img, (0,0),(256,256),(180,105,255),cv2.FILLED) # cv2.FILLED fonksiyonu ile dikdörtgenin içini dolduruyoruz.
cv2.imshow("Dikdortgen", img)

#Çember Oluşturma
#resim , merkez , yarıçap , renk
cv2.circle(img, (300,300), 45, (255,0,0),cv2.FILLED)
cv2.imshow("Cember", img)

#Metin Ekleme
#resim , eklenecek metin , başlangıç adresi,font , kalınlık ,renk
cv2.putText(img, "METIN", (256,256), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Eklenen Metin", img)
