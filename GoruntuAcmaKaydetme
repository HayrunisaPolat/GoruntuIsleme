import cv2

#resimi okuma
img= cv2.imread("araba.jpg") # ("araba.jpg",0) yaparsak gri olarak kaydeder.
#resimi gösterme
cv2.imshow("ARABA",img)

k= cv2.waitKey(0)

if k==27:#esc tuşuna basılınca direkt çıkılıyor.
    cv2.destroyAllWindows()
elif k==ord('s'):#s tuşuna basılırsa resimi kaydediyor ve ekranı kapatıyor.
    cv2.imwrite("araba_kaydetme.png", img)
    cv2.destroyAllWindows()
