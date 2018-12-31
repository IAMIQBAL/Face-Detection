import cv2

#Constants
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
video_path = '' #Leave empty to use webcam, or add a path to the video for detection face in pre-existing video

def detect_face(path):
	if video_path == '':
		cap = cv2.VideoCapture(0)
	else:
		cap = cv2.VideoCapture(video_path)
        
	while (True):
		
		# Capture frame-by-frame

		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

		for (x, y, w, h) in faces:
			roi_gray = gray[y:y+h, x:x+w]

			color = (255, 25, 100)
			stroke = 2
			width = x + w
			height = y + h

			cv2.rectangle(frame, (x, y), (width, height), color, stroke)
			
			#Save a Shot of the face

			img_tag = "me.png"
			cv2.imwrite(img_tag, roi_gray)

		# Display the resulting frame

		cv2.imshow('Output', frame)
		if cv2.waitKey(20) & 0xFF == ord('q'):			
			break

    # When everything done, release the capture

	cap.release()
	cv2.destroyAllWindows()

detect_face(video_path)