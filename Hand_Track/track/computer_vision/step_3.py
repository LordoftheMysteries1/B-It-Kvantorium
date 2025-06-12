# pip install opencv-python
# pip install mediapipe
import cv2
import mediapipe as mp
h=[0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0 ]
w=[0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0 ]
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

            for id, point in enumerate(handLms.landmark):
                width, height, _ = img.shape
                os_x, os_y = int(point.x * height), int(point.y * width)
                h[id] = os_y
                w[id] = os_x
                if h[20] > h[17] and h[16] > h[13] and h[12] > h[9] and h[8] > h[5] and w[4] > w[3]:
                    print('Камень')
                elif h[20] > h[17] and h[16] > h[13] and h[12] < h[9] and h[8] < h[5]:
                    print('Ножницы')
                if h[20] < h[17] and h[16] < h[13] and h[12] < h[9] and h[8] < h[5]:
                    print('Бумага')

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:
        break