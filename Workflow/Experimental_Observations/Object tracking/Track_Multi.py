import cv2

TrDict = {'csrt':cv2.TrackerCSRT_create,'kcf':cv2.TrackerKCF_create,
          'boosting':cv2.TrackerBoosting_create, 'mil':cv2.TrackerMIL_create,
          'tld':cv2.TrackerTLD_create,'medianflow':cv2.TrackerMedianFlow_create,
          'moose':cv2.TrackerMOSSE_create}

trackers =cv2.MultiTracker_create()

v = cv2.VideoCapture('sample5.mp4')

ret, frame =v.read()

k=3
for i in range(k):
    cv2.imshow('Frame',frame)
    bbi = cv2.selectROI('Frame',frame)
    tracker_i=TrDict['csrt']()
    trackers.add(tracker_i,frame,bbi)


while True:
    ret, frame =v.read()
    if not ret:
        break
    (success,boxes)= trackers.update(frame)
    for box in boxes:
        (x,y,w,h) = [int(a) for a in box]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('Frame',frame)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
        break
v.release()
cv2.destroyAllWindows()




