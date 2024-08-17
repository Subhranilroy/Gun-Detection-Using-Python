import numpy as np  
import cv2
import imutils
import datetime

gun_cascade = cv2.CascadeClassifier('C:/Users/KIIT/Downloads/cascade.xml')
camera = cv2.VideoCapture(0)
firstFrame = None
gun_exist = None

while True:
    # Capture frame from the camera
    ret, frame = camera.read()

    # If frame not captured successfully, handle the error
    if not ret or frame is None:
        print("Failed to grab frame.")
        break

    # Resize the frame
    frame = imutils.resize(frame, width=500)

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns in the frame
    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    if len(gun) > 0:
        gun_exist = True

    # Draw rectangles around detected guns
    for (x, y, w, h) in gun:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Initialize the first frame if it's None
    if firstFrame is None:
        firstFrame = gray
        continue

    # Display the security feed
    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF

    # Break the loop if 'q' is pressed
    if key == ord("q"):
        break

    # Print whether a gun was detected or not
    if gun_exist:
        print("Gun detected")
    else:
        print("Gun not detected")

# Release the camera and close windows
camera.release()
cv2.destroyAllWindows()
