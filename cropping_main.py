import numpy as np
import cv2 as cv
import random
from pathlib import Path

def doinmain(savename):
    im = cv.imread(Path('images/main.png'))

    im = im[450:725, 130:1280]

    color = cv.inRange(im, (25, 25, 25), (30, 30, 30))

    mask = cv.morphologyEx(color, cv.MORPH_CLOSE, np.ones((3, 3), np.uint8))

    cnts = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)[0]

    for c in cnts:
        size_tresh = 500
        x, y, w, h = cv.boundingRect(c)
        if w < size_tresh and h < size_tresh:
            cv.drawContours(mask, [c], 0, 0, -1)

    y, x = np.where(mask == 255)
    x0, y0 = x.min(), y.min()
    x1, y1 = x.max(), y.max()

    #cv.rectangle(im, (x0,y0), (x1,y1), (250,0,0), 5)

    crop_img = im[y0:y1, x0:x1]

    path = Path('images/'+savename+'.png')

    cv.imwrite(path, crop_img)

    #cv.imshow('fuck', crop_img)
    
    cv.waitKey()
    cv.destroyAllWindows()



def main():
    pass

if __name__ == "__main__":
   main()
