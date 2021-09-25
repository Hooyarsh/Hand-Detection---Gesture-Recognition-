import cv2
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)

detector= HandDetector(detectionCon=0.8)


while True:
	success,img=cap.read()
	hands,img= detector.findHands(img)
	
	if hands: 
		hand1=hands[0]
		lmList1=hand1["lmList"]
		bbox1=hand1["bbox"]
		centerPoint1=hand1["center"]
		handType1=hand1["type"]
		finger1=detector.fingersUp(hand1)
		length,info,img=detector.findDistance(lmList1[8],lmList1[12],img)
		 
	if len(hands)==2:
		hand2=hands[1]
		lmList2=hand2["lmList"]
		bbox2=hand2["bbox"]
		centerPoint2=hand2["center"]
		handType2=hand2["type"]
		finger2=detector.fingersUp(hand2)
		length,info,img=detector.findDistance(lmList1[8],lmList2[8],img)
		length,info,img=detector.findDistance(centerPoint1,centerPoint2,img)



	cv2.imshow("Image",img)


	key_pressed = cv2.waitKey(1) & 0xFF 
	if key_pressed == ord('q'): 
		break

cap.release()
cv2.destroyALlWindows()