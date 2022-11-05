import cv2
import mediapipe as mp
import uuid
import os

# we are using the drawing utils to draw the hand landmarks
mp_drawing = mp.solutions.drawing_utils
# to get the hand model
mp_hands = mp.solutions.hands

#starting the webcam using opencv
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8,
                    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        #BGR to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #flipping the image
        image = cv2.flip(image, 1)
        #set flag
        image.flags.writeable = False
        #detections
        results = hands.process(image)
        #set flag to true
        image.flags.writeable = True
        #RGB to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        print(results)

        #Rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(
                    image, hand, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(121, 22, 76),
                                           thickness=2,
                                           circle_radius=4),
                    mp_drawing.DrawingSpec(color=(121, 44, 250),
                                           thickness=2,
                                           circle_radius=2))

        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
