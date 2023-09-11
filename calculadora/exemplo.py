import cl
import cv2
import numpy as np

imgs = cv2.imread("/home/cesar/Desktop/PDI/PID/calculadora/imgs/Baboon.tiff",1)
img2 = cv2.imread("/home/cesar/Desktop/PDI/PID/calculadora/imgs/Splash.tiff",1)
imgs = cv2.resize(imgs,(200,200))
img2 = cv2.resize(img2,(200,200))

res = np.max(imgs)

cv2.imshow("Resultado",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
