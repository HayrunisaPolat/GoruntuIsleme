import cv2
import matplotlib.pyplot as plt

img = cv2.imread("manzara.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img,cmap="gray") # cmap = colormap 
plt.axis("Off")
plt.show()

# Eşikleme - Threshold
#  thresh :60 eşik değerinin altındakileri ön plana çıkarıyor.
# THRESH_BINARY 60 ve 255 değerleri arasındakileri  beyaz yapıyor
# THRESH_BINARY_INV 60 ve 255 değerleri arasındakileri siyah yapıyor.
_,thresh_img = cv2.threshold(img, thresh=60, maxval=255, type= cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh_img,cmap="gray") # cmap = colormap 
plt.axis("Off")
plt.show()

# Uyarlamalı Threshold
# Görseli komşularına bakarak ayırıyor. blockSize = Komşu sayısı
thresh_img2 = cv2.adaptiveThreshold(src=img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=11, C=8)
plt.figure()
plt.imshow(thresh_img2,cmap="gray") 
plt.axis("Off")
plt.show()