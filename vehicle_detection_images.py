import cv2
from main import create_snap
 
face_cascade = cv2.CascadeClassifier('cars.xml')



available = True
count = 1

while available:

	frame = cars = []
	car_number = {}

	for i in range(1, 5):
		frame = cv2.imread("snaps/" + str(i) + ".png")

		# cv2.imshow("abc_color", frame)
		# cv2.waitKey(0)

		gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

		# cv2.imshow("abc", gray)
		# cv2.waitKey(0)

		cars_temp =  face_cascade.detectMultiScale(gray, 1.1, 1) 
		# cars_2 = face_cascade.detectMultiScale(gray, 1.1, 2)

		# print cars_temp

		ind_lane_count = 0
		for (x,y,w,h) in cars_temp:
		    cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 0, 0),2)
		    ind_lane_count += 1

		

		if i == 1:
			frame0 = frame
			car_number["direction0"] = ind_lane_count
		elif i == 2:
			frame1 = frame
			car_number["direction1"] = ind_lane_count
		elif i == 3:
			frame2 = frame
			car_number["direction2"] = ind_lane_count
		else:
			frame3 = frame
			car_number["direction3"] = ind_lane_count

		# for (x,y,w,h) in cars_2:
		#     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2)
		#     ncars = ncars + 1

		# show result
		# cv2.imshow("Result", frame)
		# cv2.waitKey(0)

	for i in car_number:
			print i, "=>",  car_number[i]

	available = create_snap(count)
	count += 1

cv2.waitKey(0)


