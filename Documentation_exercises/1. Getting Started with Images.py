import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("image.jpg"))

if img is not None:
    cv.imshow("Display window", img)
    k = cv.waitKey(0)

    if k == ord("s"):
        cv.imwrite("image.png", img)

else:
    sys.exit("Could not read the image.")

