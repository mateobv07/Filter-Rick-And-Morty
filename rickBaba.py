import cv2
import numpy as np
from math import hypot

def createBaba(landmarks, frame):
    baba_imagen = cv2.imread("assets/baba.png")

     #get coordinates for mouth
    left_mouth = (landmarks.part(59).x , landmarks.part(59).y + 10)
    right_mouth = (landmarks.part(55).x , landmarks.part(55).y + 10)
    center_mouth = (landmarks.part(57).x , landmarks.part(57).y + 10 )

    width_mouth= int(hypot(left_mouth[0] - right_mouth[0], left_mouth[1] - right_mouth[1]))
    height_mouth = int(width_mouth*.77)


    baba_rick = cv2.resize(baba_imagen, (width_mouth, height_mouth))
    baba_rick_gray = cv2.cvtColor(baba_rick, cv2.COLOR_BGR2GRAY)
    
    _, baba_mask = cv2.threshold(baba_rick_gray, 25, 255, cv2.THRESH_BINARY_INV)

    #Get area of mouth
    top_left = ( int(center_mouth[0] - width_mouth/2), int(center_mouth[1] - height_mouth/2))

    baba_area = frame[top_left[1]: top_left[1] + height_mouth, top_left[0]: top_left[0] + width_mouth]

    baba_rick_area_sin_baba = cv2.bitwise_and(baba_area,baba_area, mask=baba_mask)

    final = cv2.add(baba_rick_area_sin_baba, baba_rick)

    #frame[top_left[1]: top_left[1] + height_mouth, top_left[0]: top_left[0] + width_mouth] = baba_final

    fromY = top_left[1]
    toY = top_left[1] + height_mouth
    fromX = top_left[0]
    toX = top_left[0] + width_mouth

    return fromX, toX, fromY, toY, final