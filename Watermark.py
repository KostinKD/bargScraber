import numpy as np
import cv2


# OR

img = cv2.imread('image.jpg')
mask = cv2.imread('mask.png', 0)

dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

cv2.imwrite('result.jpg', dst)


img = cv2.imread('image.jpg')

alpha = 1.5 # яркость
beta = 0 # контраст

new_image = np.zeros(img.shape, img.dtype)
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        for c in range(img.shape[2]):
            new_image[y,x,c] = np.clip(alpha*img[y,x,c] + beta, 0, 255)

cv2.imwrite('result.jpg', new_image)




