import cv2

imgpath = "ada.jpg"

image = cv2.imread(imgpath)

# font
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (50, 50)
  
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (255, 255, 255)
  
# Line thickness of 2 px
thickness = 2

# # Using cv2.putText() method
image = cv2.putText(image, "OpenCV", org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)


# to write multiple line

text1 = "hello world"
text2 = "have a good day"

# Using cv2.putText() method
image = cv2.putText(image, text1, (50, 90), font, 
                   fontScale, color, thickness, cv2.LINE_AA)


# Using cv2.putText() method
image = cv2.putText(image, text2, (50, 130), font, 
                   fontScale, color, thickness, cv2.LINE_AA)



# Displaying the image
cv2.imshow("win", image) 

cv2.waitKey(0)

