import cv2
import numpy as np
from math import hypot

def createHair(landmarks, frame):

    hair_imagen = cv2.imread("assets/hair.png")

    #get coordinates for hair
    left_hair = (landmarks.part(0).x -100, landmarks.part(0).y)
    right_hair = (landmarks.part(25).x +100, landmarks.part(16).y )
    center_hair = (landmarks.part(27).x , landmarks.part(24).y )
    bottom_hair = (landmarks.part(8).x , landmarks.part(8).y )
    
    width_hair = int(hypot(left_hair[0] - right_hair[0], left_hair[1] - right_hair[1]))
    height_hair = int(hypot(bottom_hair[0] - center_hair[0], bottom_hair[1] - center_hair[1]) * 1.6)
    hair_rick = cv2.resize(hair_imagen, (width_hair, height_hair))
    hair_rick_gray = cv2.cvtColor(hair_rick, cv2.COLOR_BGR2GRAY)
    
    _, hair_mask = cv2.threshold(hair_rick_gray, 25, 255, cv2.THRESH_BINARY_INV)

    #Get area of hair
    top_left = ( int(center_hair[0] - width_hair/1.85), int(center_hair[1] - height_hair/2))

    hair_area = frame[top_left[1]: top_left[1] + height_hair, top_left[0]: top_left[0] + width_hair]

    hair_rick_area_sin_hair = cv2.bitwise_and(hair_area, hair_area, mask=hair_mask)

    final = cv2.add(hair_rick_area_sin_hair, hair_rick)
    
    #Add hair to frame
    #frame[top_left[1]: top_left[1] + height_hair, top_left[0]: top_left[0] + width_hair] = final

    fromY = top_left[1]
    toY = top_left[1] + height_hair
    fromX = top_left[0]
    toX = top_left[0] + width_hair

    return fromX, toX, fromY, toY, final
