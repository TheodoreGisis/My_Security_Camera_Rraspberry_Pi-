import cv2
import datetime
import time
import sys

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

cap =  cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") 
frame_size = (int(cap.get(3)), int(cap.get(4)))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
while True:
    _,frame  = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    body = body_cascade.detectMultiScale(gray,1.2,2)

    #for (x,y,width,height) in faces:
        #cv2.rectangle(frame,(x,y), (x+width, y+ height),(255,0,0),3)
    #for(x,y,width,height) in body:
        #cv2.rectangle(frame,(x,y), (x+width, y+ height),(255,0,0),3)
    if len(faces) + len (body) > 0:
        if detection:
            timer_starded = False
        else: 
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Started recording.....")
    elif detection:
        if timer_starded:
            if time.time() - detection_stopped_time  >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_starded =False 
                out.release()
                print("Stop!")
        else:
            timer_starded =True
            detection_stopped_time  =time.time()
            
    if detection:
        out.write(frame)
    cv2.imshow("Camera",frame)

    if cv2.waitKey(1)  == ord('q'):   
        break
        
cap.release()
out.release()
cv2.destroyAllWindows()    
