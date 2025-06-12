# pip install opencv-python
# pip install mediapipe
import cv2
import mediapipe as mp
import pyfirmata


def recrop(value, min, max):
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value


camera = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mp.solutions.hands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

board = pyfirmata.Arduino('COM10')
led = board.get_pin('d:11:p')

while True:
    _, img = camera.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(imgRGB) 

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            for id, point in enumerate(handLms.landmark):
                width, height, _ = img.shape
                os_x, os_y = int(point.x * height), int(point.y * width)
                if id == 8:
                    cv2.circle(img, (os_x, os_y), 15, (255, 0, 255), cv2.FILLED)
                    print(point.x)
                    # led.write(point.x)
                    # led.write(recrop(point.x, 0, 1))
                    led.write(recrop(point.x - 0.1, 0, 1))

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:
        break