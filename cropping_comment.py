import numpy as np
import cv2 as cv
from pathlib import Path

def doincomment(savename):
    im = cv.imread(Path('images/comment.png'))

    color = cv.inRange(im, (35, 35, 35), (40, 40, 40))

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

    crop_img = im[y0:y1, x0:x1]

    path = Path('images/'+savename+'.png')

    cv.imwrite(path, crop_img)

def main():
    pass

if __name__ == "__main__":
   main()


