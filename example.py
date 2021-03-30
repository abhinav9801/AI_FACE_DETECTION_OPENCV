import cv2
from random import randrange

# load some pre trained data on face frontals from open cv
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose an image to detect faces in
#img=cv2.imread('rdj.jpg')

# To capture video from webcam
webcam=cv2.VideoCapture(0)

# iterate forever over frames
while True:

    # Read the current frame
    successful_frame_read,frame=webcam.read()
    # must convert to gray scale
    grayscale_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Detect face
    face_coordinate=trained_face_data.detectMultiScale(grayscale_img)
    
    # Draw rectangle around faces
    for (x,y,w,h) in face_coordinate:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),5)

    cv2.imshow("Abhinav'S Face Detector",frame)
    key=cv2.waitKey(1)

    # stop if Q key is presssed
    if key==81 or key==113:
        break

# Release the video capture object
webcam.release()
print("code completed ")


''''
# must convert to gray scale
grayscale_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinate=trained_face_data.detectMultiScale(grayscale_img)

# print(face_coordinate)

# Draw rectangle around faces
for (x,y,w,h) in face_coordinate:
    cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),10)




# Display the image
cv2.imshow("Abhinav'S Face Detector",img)

# to display picture until a key is pressed
cv2.waitKey()
'''
