# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 23:34:01 2025

@author: Hayrunisa Polat
"""

#Kamera Açma ve Videoya Kaydetme
import cv2

cap= cv2.VideoCapture(0)

genislik= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
yukseklik= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter("video_kaydi.mp4",cv2.VideoWriter.fourcc(*'DIVX'),20,(genislik,yukseklik)) # 4x4 lük kayıt

while True:
    ret,frame=cap.read()
    cv2.imshow("VIDEO", frame)
    writer.write(frame)
    
    if(cv2.waitKey(1)&0xFF==ord('q')):break

cap.release()
writer.release()
cv2.destroyAllWindows()