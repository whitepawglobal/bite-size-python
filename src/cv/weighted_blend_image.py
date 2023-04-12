#https://stackoverflow.com/questions/57723968/blending-multiple-images-with-opencv

import cv2
import numpy as np


if __name__ == "__main__":
    

    img1 = cv2.imread('/Users/chiawei.lim/Downloads/background.jpg')
    img2 = cv2.imread('/Users/chiawei.lim/Downloads/6a00d83451c0aa69e2015432796940970c-800wi.jpg')
    
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    print(img1.shape)
    print(img2.shape)
    
    combined_img = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

    cv2.imwrite('combined.png', combined_img)
    
    print("complete")
