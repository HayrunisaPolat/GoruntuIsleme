# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 23:13:32 2025

@author: Hayrunisa Polat
"""
import cv2
import time

video_adi = "video.mp4"
cap= cv2.VideoCapture(video_adi)

if(cap.isOpened()==False):
    print("Video Boş Okunamıyor")

print("Genişlik : " , cap.get(3))
print("Yükseklik : ", cap.get(4))


while True:
    ret,frame = cap.read()
    if ret == True:
        time.sleep(0.05) #videonun normal hızında gösterilmesi için , hızlı akmaması için 
        cv2.imshow("Video",frame)
    else : break
    
    if (cv2.waitKey(1) & 0xFF==ord("q")): # 'q tuşuna basılınca while bloğundan çıkar videoyu sonlandırır.
        break
    
    
cap.release() # video okumayı durduruyoruz.
cv2.destroyAllWindows()#bütün pencereleri kapatıyoruz.