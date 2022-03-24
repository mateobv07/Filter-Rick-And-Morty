import cv2
import dlib
from rickCeja import createCeja

cap = cv2.VideoCapture(0)


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(frame)

    for face in faces:
        landmarks = predictor(gray_frame, face)

        #ceja
        fromX, toX, fromY, toY, final = createCeja(landmarks, frame)
        frame[fromY: toY , fromX: toX] = final

       

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break