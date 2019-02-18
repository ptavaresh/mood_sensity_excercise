import numpy as np
import cv2

import requests
import json

send_url = 'http://api.ipstack.com/177.245.200.30?access_key=f4422326475b6edb7ed6caf6a56a1694'
r = requests.get(send_url)
j = json.loads(r.text)
print(j)
lat = j['latitude']
lon = j['longitude']
print('latitude: ' + str(lat) + '\n' + 'longitude: ' + str(lon))

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
ret,frame = cap.read() # return a single frame in variable `frame`

while(True):
    cv2.imshow('img1',frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite('images/c1.png',frame)
        cv2.destroyAllWindows()
        break

cap.release()
