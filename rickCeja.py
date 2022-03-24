import cv2
import numpy as np
from math import hypot

def createCeja(landmarks, frame):
    ceja_imagen = cv2.imread("ceja.png")

     #get coordinates for eye brow
    left_ceja = (landmarks.part(18).x , landmarks.part(18).y)
    right_ceja = (landmarks.part(25).x , landmarks.part(24).y - 20)
    center_ceja = (landmarks.part(27).x , landmarks.part(21).y - 20)

    width_ceja = int(hypot(left_ceja[0] - right_ceja[0], left_ceja[1] - right_ceja[1]))

    height_ceja = 70
    ceja_rick = cv2.resize(ceja_imagen, (width_ceja, height_ceja))
    ceja_rick_gray = cv2.cvtColor(ceja_rick, cv2.COLOR_BGR2GRAY)
    
    _, ceja_mask = cv2.threshold(ceja_rick_gray, 25, 255, cv2.THRESH_BINARY_INV)

    #Get area of eye brow
    top_left = ( int(center_ceja[0] - width_ceja/2), int(center_ceja[1] - height_ceja/2))

    ceja_area = frame[top_left[1]: top_left[1] + height_ceja, top_left[0]: top_left[0] + width_ceja]

    ceja_rick_area_sin_ceja = cv2.bitwise_and(ceja_area,ceja_area, mask=ceja_mask)

    final = cv2.add(ceja_rick_area_sin_ceja, ceja_rick)

    #frame[top_left[1]: top_left[1] + height_ceja, top_left[0]: top_left[0] + width_ceja] = ceja_final

    fromY = top_left[1]
    toY = top_left[1] + height_ceja
    fromX = top_left[0]
    toX = top_left[0] + width_ceja

    return fromX, toX, fromY, toY, final