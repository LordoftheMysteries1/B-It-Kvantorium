# pip install opencv-python
# pip install mediapipe
import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mp.solutions.hands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

while True:
    _, img = camera.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(imgRGB) 

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:
        break