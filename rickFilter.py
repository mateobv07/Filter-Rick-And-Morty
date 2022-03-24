#Para este filtro nos basamos en el siguiente recurso:
#https://pysource.com/2019/03/25/pigs-nose-instagram-face-filter-opencv-with-python/
import cv2
import dlib
from rickCeja import createCeja
from rickHair import createHair
from rickBaba import createBaba
from rickTitulo import createTitulo
cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(frame)

    for face in faces:
        landmarks = predictor(gray_frame, face)
        #hair
        
        fromX, toX, fromY, toY, final = createHair(landmarks, frame)
        if fromX != 0:
            frame[fromY: toY , fromX: toX] = final
        #ceja
        fromX, toX, fromY, toY, final = createCeja(landmarks, frame)
        if fromX != 0:
            frame[fromY: toY , fromX: toX] = final
        #baba
        fromX, toX, fromY, toY, final = createBaba(landmarks, frame)
        if fromX != 0:
            frame[fromY: toY , fromX: toX] = final
        #titulo
        fromX, toX, fromY, toY, final = createTitulo(landmarks, frame)
        if fromX != 0:
            frame[fromY: toY , fromX: toX] = final
    cv2.imshow("RickMorty", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
