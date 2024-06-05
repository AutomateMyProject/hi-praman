# Import the required libraries.
import mediapipe as mp
import cv2

# Initialize the MediaPipe Hands model.
mp_hands = mp.solutions.hands

# Initialize the VideoCapture object.
cap = cv2.VideoCapture(0)

# Create a loop to capture and process video frames.
while cap.isOpened():

    # Capture a frame from the video stream.
    ret, frame = cap.read()

    # Convert the frame to RGB color space.
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image with the MediaPipe Hands model.
    results = mp_hands.process(image)

    # Draw the hand landmarks on the image.
    image = mp.solutions.drawing_utils.draw_landmarks(image, results.multi_hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the image.
    cv2.imshow('Hand Gesture Detection', image)

    # Press 'q' to quit.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object.
cap.release()

# Destroy all windows.
cv2.destroyAllWindows()
