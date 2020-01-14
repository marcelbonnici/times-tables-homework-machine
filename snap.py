import numpy as np
import cv2
import serial
import pytesseract
import re
#"""
arduinoSerialData = serial.Serial('/dev/ttyACM3',9600)

cnt = 0

while cnt < 10:
    if (arduinoSerialData.inWaiting()>0):

        myData = arduinoSerialData.readline()
        #print myData

        cap = cv2.VideoCapture(2) # video capture source camera (Here webcam of laptop)
        ret,frame = cap.read() # return a single frame in variable `frame`
        cnt = cnt+1
        snapname = 'images/snap'+str(cnt)+'.png'

        frame = frame[230:328]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        cv2.imwrite(snapname, frame)
        #cv2.destroyAllWindows()
        cap.release()



p1 = cv2.imread('images/snap1.png')
p2 = cv2.imread('images/snap2.png')
p3 = cv2.imread('images/snap3.png')
p4 = cv2.imread('images/snap4.png')
p5 = cv2.imread('images/snap5.png')
p6 = cv2.imread('images/snap6.png')
p7 = cv2.imread('images/snap7.png')
p8 = cv2.imread('images/snap8.png')
p9 = cv2.imread('images/snap9.png')
p10 = cv2.imread('images/snap10.png')
sheet = np.concatenate((p1, p2, p3, p4, p5, p6, p7, p8, p9, p10), axis=0)
cv2.imwrite('images/sheet.png', sheet)
#"""


img = cv2.imread('images/sheet.png')
#img = img[0:100, 125:275]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)
#good = str(qwertyuopasdfghjkzcvbnm')
settings=r'--tessdata-dir "/home/marcelbonnici/Dropbox/000_LINUX/winterproject/tessdata" -l eng --oem 0 --psm 6 -c tessedit_char_whitelist=0123456789x=qwertyuopasdfghjkzcvbnm'
text = pytesseract.image_to_string(blackAndWhiteImage, config=settings)#config='--psm 6', lang='eng')
bad = "=qwertyuopasdfghjkzcvbnm "
boxes = pytesseract.image_to_boxes(blackAndWhiteImage, config=settings)
"""
for ch in range(len(bad)):
    text=text.replace(bad[ch], "")

boxes=re.split('\n', boxes)

ar=0
boxold=boxes
boxes=[]
for ar in range(len(boxold)):
    boxindex = boxold[ar]
    if str(boxindex)[2] != "x":
        added = boxold[ar]
        boxes=boxes.append(added)
"""
print(text)
print("---------------")
#print(boxes)
#print("---------------")
for i in range(len(text)):
    if text[i] == "x" and text[i+1].isdigit() == True and text[i-1].isdigit() == True and i > 0:
        if text[i+1] == "1":
            if text[i+2] == "0" or text[i+2] == "1" or text[i+2] == "2":
                number2 = text[i+1:i+3]
            else:
                number2=text[i+1]
        else:
            number2=text[i+1]
        if text[i-1]== "0" or text[i-1] == "1" or text[i-1] == "2":
            if text[i-2] == 1:
                number1 = text[i-2:i]
            else:
                number1 = text[i-1]
        else:
            number1=text[i-1]
        #print(number1)
        #print(number2)
        print (int(number1) * int(number2))
#print (text)

cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imwrite("bwimage.png", blackAndWhiteImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
