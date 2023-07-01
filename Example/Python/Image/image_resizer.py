import cv2
import os
__DIR__ = os.path.dirname(os.path.abspath(__file__))

img = cv2.imread(__DIR__ + '/photo1.jpg')
# (h,w,c) = img.shape
# print ('width: {} pixels'.format(w))
# print ('height: {}  pixels'.format(h))
# print ('channels: {}'.format(c))
# print (img.shape[0],img.shape[1],img.shape[2])
print ('Original Dimensions :' , img.shape)
width = int(img.shape[1] / 5)
height = int(img.shape[0] / 5)
scaled_img = cv2.resize(img, (width,height), interpolation = cv2.INTER_AREA)
print ('Resized Dimensions :' , scaled_img.shape)
cv2.imwrite(__DIR__ + '/scaled_photo1.jpg', scaled_img)