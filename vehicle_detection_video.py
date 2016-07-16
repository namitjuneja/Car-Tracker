# -*- coding: utf-8 -*-

import cv2
print(cv2.__version__)

cascade_src = 'cars.xml'

video_src = 'videos/1.m4v'
# video_src = 'videos/2.mp4'
# video_src = 'videos/3.mp4'


cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)
car_count = 0

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresohold = {'videos/1.m4v': 340000, 'videos/2.mp4': 170000, 'videos/3.mp4': 340000}
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    sub_car = None

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        # if w*h > thresohold[video_src]:
        if w*h == 110889 or w*h > thresohold[video_src]:
            sub_car = img[y:y+h, x:x+w]
            cv2.imshow('sub_car', sub_car)
            print "image write path", './cars/car' + str(car_count) + '.png'
            print "image write successful", cv2.imwrite('./cars/car' + str(car_count) + '.png', sub_car)
            # print cv2.imwrite('/var/www/html/public/aksja.png', sub_car)
            car_count += 1
    
    
    cv2.imshow('video', img)

        
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
