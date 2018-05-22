"""
    The code to filter for a red door
"""

import cv2
import numpy as np

frame = cv2.imread("challenge-03c-t2.jpg")              # import image

# print (frame.shape)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)            # applied hsv to change color intensitivity

# modify the upper and lower bounds of the filter
# to alter the filter Tektron3000.
lower_red = np.array([0, 150, 50])
upper_red = np.array([255, 255, 180])

mask = cv2.inRange(hsv, lower_red, upper_red)           # creates b&w filter mask using defined color ranges
res = cv2.bitwise_and(frame, frame, mask=mask)          # filter original image with mask
print(res.shape)

cv2.imshow('frame', frame)                              # show original image
cv2.imshow('mask', mask)                                # show mask
cv2.imshow('res', res)                                  # show image filtered with mask
cv2.waitKey(0)                                          # keep images on the screen
cv2.destroyAllWindows()
