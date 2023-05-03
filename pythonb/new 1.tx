import cv2
import numpy as np

# arguments
invert = "no"     # invert mask; yes or no
rotate = 0        # rotate composite; 0, 90, 180, 270

# read image (must be square)
img = cv2.imread('river_valley.png')
ht, wd = img.shape[:2]

# transpose the image
imgt = cv2.transpose(img)

# create diagonal bi-tonal mask
mask = np.zeros((ht,wd), dtype=np.uint8)
points = np.array( [[ [0,0], [wd,0], [wd,ht] ]] )
cv2.fillPoly(mask, points, 255)
if invert == "yes":
    mask = cv2.bitwise_not(mask)

# composite img and imgt using mask
compA = cv2.bitwise_and(imgt, imgt, mask=mask)
compB = cv2.bitwise_and(img, img, mask=255-mask)
comp = cv2.add(compA, compB)

# rotate composite
if rotate == 90:
    comp = cv2.rotate(comp,cv2.ROTATE_90_CLOCKWISE)
elif rotate == 180:
    comp = cv2.rotate(comp,cv2.ROTATE_180)
elif rotate == 270:
    comp = cv2.rotate(comp,cv2.ROTATE_90_COUNTERCLOCKWISE)

# mirror (flip) horizontally
mirror = cv2.flip(comp, 1)

# concatenate horizontally
top = np.hstack((comp, mirror))

# mirror (flip) vertically
bottom = cv2.flip(top, 0)

# concatenate vertically
kaleidoscope_big = np.vstack((top, bottom))

# resize
kaleidoscope = cv2.resize(kaleidoscope_big, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# save results
cv2.imwrite('river_valley_kaleidoscope_mask.png', mask)
cv2.imwrite('river_valley_kaleidoscope.png', kaleidoscope)


cv2.imshow('image', img)
cv2.imshow('transpose', imgt)
cv2.imshow('mask', mask)
cv2.imshow('compA', compA)
cv2.imshow('compB', compB)
cv2.imshow('comp', comp)
cv2.imshow('kaleidoscope', kaleidoscope)
cv2.waitKey(0)
cv2.destroyAllWindows()