import cv2
import numpy as np
from math import hypot

def createTitulo(landmarks, frame):
    titulo_imagen = cv2.imread("assets/titulo.png")

     #get coordinates for above head
    left_forehead = (landmarks.part(19).x , landmarks.part(19).y - 100)
    right_forehead = (landmarks.part(24).x , landmarks.part(24).y - 100)
    center_forehead = (landmarks.part(27).x , landmarks.part(27).y - 100 )

    width_forehead = int(hypot(left_forehead[0] - right_forehead[0], left_forehead[1] - right_forehead[1]))
    height_forehead = int(width_forehead*1.05)


    title_rick = cv2.resize(titulo_imagen, (width_forehead, height_forehead))
    title_rick_gray = cv2.cvtColor(title_rick, cv2.COLOR_BGR2GRAY)
    
    _, title_mask = cv2.threshold(title_rick_gray, 25, 255, cv2.THRESH_BINARY_INV)

    #Get area of title
    top_left = ( int(center_forehead[0] - width_forehead/2), int(center_forehead[1] - height_forehead/2))
    try:
        title_area = frame[top_left[1]: top_left[1] + height_forehead, top_left[0]: top_left[0] + width_forehead]

        title_rick_area_sin_title = cv2.bitwise_and(title_area,title_area, mask=title_mask)

        final = cv2.add(title_rick_area_sin_title, title_rick)

        #frame[top_left[1]: top_left[1] + height_forehead, top_left[0]: top_left[0] + width_forehead] = title_final

        fromY = top_left[1]
        toY = top_left[1] + height_forehead
        fromX = top_left[0]
        toX = top_left[0] + width_forehead

        return fromX, toX, fromY, toY, final
    except:
        return 0, 0, 0, 0, 0