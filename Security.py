import cv2
import os
import smtplib
import datetime
from time import gmtime,strftime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
cap = cv2.VideoCapture(0)

def real_time():
    time=strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return time

def remove_image_from_pc(image):
    print("Deleting image....")
    print("Done!")
    os.remove(os.path.abspath(os.getcwd()) + '/' + image)


def mail(image):

    sender = "teogisis12@gmail.com"
    receiver = "myrasberrygisis@gmail.com"
    password="atsaoleole123"
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = "SECURITY CAMERA"

    body = 'SOMEONE IS HERE!'
    msg.attach(MIMEText(body,'plain'))

    filename= image
    attachment = open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender,receiver,text)
    server.quit()

def calculacedifference(frame,frame1):
    different = cv2.absdiff(frame1 ,frame)
    return different

def converPicture(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5) ,0)
    _,thresh =cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilate = cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return contours

def DrawBoxes(contours):
    for c in contours:
         x, y, w, h = cv2.boundingRect(c)
         if (cv2.contourArea(c)) < 2000:
            continue
         else:
            cv2.rectangle(frame1,(x,y), (x+w,y+h), (0,0,0), 2)
            return 0


if __name__ == "__main__":
    img_counter = 0
    
    if not cap.isOpened():
        print("Error Camera not Opened!")
        
  
    while cap.isOpened() :
        time=real_time()
        ret,frame =cap.read()
        ret,frame1 =cap.read()
        new_image=calculacedifference(frame,frame1)
        contours=converPicture(new_image)
        if DrawBoxes(contours) == 0:           
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            img_counter = img_counter+1
            print("detecting movement at ")
            print(time) 
            print("sending email...")
            print("Done!")
            mail(img_name)
            remove_image_from_pc(img_name)
        else:
            DrawBoxes(contours)

        if cv2.waitKey(1)==ord('q'):
            break
        image=cv2.resize(frame1,(1280,720))       
        cv2.imshow("frame",image)
        
