import cv2

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Display the frame
    cv2.imshow('Camera', frame)
    
    # Check if the user presses the 'c' key to capture their reaction
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # Capture the current frame
        cv2.imwrite('reaction.jpg', frame)
        print("Reaction captured!")
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()