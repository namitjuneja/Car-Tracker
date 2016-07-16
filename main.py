import cv2
import math
import numpy as np

def create_snap(time):
	#################### Setting up the file ################
	videoFile = "./videos/video1.avi"
	vidcap = cv2.VideoCapture(videoFile)
	success,image = vidcap.read()

	#################### Setting up parameters ################

	seconds = 5 * time
	fps = vidcap.get(cv2.cv.CV_CAP_PROP_FPS) # Gets the frames per second
	multiplier = int(fps * seconds)

	#################### Initiate Process ################

	count = 0
	while success:
		frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
		success, image = vidcap.read()

		if frameId % (multiplier+45) == 0:
			cv2.imwrite("snaps/4.png", image)
			count+=1;
			print frameId, multiplier

		elif frameId % (multiplier+30) == 0:
			cv2.imwrite("snaps/3.png", image)
			count+=1;
			print frameId, multiplier

		elif frameId % (multiplier+15) == 0:
			cv2.imwrite("snaps/2.png", image)
			count+=1;
			print frameId, multiplier

		elif frameId % (multiplier) == 0:
			cv2.imwrite("snaps/1.png", image)
			count+=1;
			print frameId, multiplier

		
		if count == 4:
			break


	vidcap.release()
	return success

print create_snap(6)