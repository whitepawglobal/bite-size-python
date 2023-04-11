import numpy as np
import cv2 as cv

#https://mlhive.com/2022/04/draw-on-images-using-mouse-in-opencv-python

drawing = False # true if mouse is pressed
ix,iy = -1,-1
pad = 5

# mouse callback function
def draw_point(event, x, y, flags, param):
    """ Draw rectangle on mouse click and drag """
    global drawing, mode
    # if the left mouse button was clicked, record the starting and set the drawing flag to True
    if event == cv.EVENT_LBUTTONDOWN:
        print("x: " + str(x))
        print("y: " + str(y))
        cv.rectangle(img, (x-pad, y - pad), (x + pad, y + pad), (255, 255, 255), -1)

# mouse callback function
def draw_rectangle(event, x, y, flags, param):
    """ Draw rectangle on mouse click and drag """
    global ix,iy,drawing,mode
    # if the left mouse button was clicked, record the starting and set the drawing flag to True
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    # mouse is being moved, draw rectangle
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.rectangle(img, (ix, iy), (x, y), (255, 255, 0), -1)
    # if the left mouse button was released, set the drawing flag to False
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

# create a black image (height=360px, width=512px), a window and bind the function to window

height = 250
width = 600
img = np.zeros((height, width,3), np.uint8)
cv.namedWindow('image') 
cv.setMouseCallback('image',draw_point)

while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

    
cv.destroyAllWindows()
