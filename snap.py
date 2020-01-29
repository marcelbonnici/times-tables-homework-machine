#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import serial
import pytesseract
import re
"""
arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)

cnt = 0

while cnt < 19:
    if (arduinoSerialData.inWaiting()>0):

        myData = arduinoSerialData.readline()
        #print myData

        cap = cv2.VideoCapture(2) # video capture source camera (Here webcam of laptop)
        ret,frame = cap.read() # return a single frame in variable `frame`
        cnt = cnt+1
        snapname = 'limages/snap'+str(cnt)+'.png'

        frame = frame[230:328]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        cv2.imwrite(snapname, frame)
        #cv2.destroyAllWindows()
        cap.release()



p1 = cv2.imread('limages/snap1.png')
p2 = cv2.imread('limages/snap2.png')
p3 = cv2.imread('limages/snap3.png')
p4 = cv2.imread('limages/snap4.png')
p5 = cv2.imread('limages/snap5.png')
p6 = cv2.imread('limages/snap6.png')
p7 = cv2.imread('limages/snap7.png')
p8 = cv2.imread('limages/snap8.png')
p9 = cv2.imread('limages/snap9.png')
p10 = cv2.imread('limages/snap10.png')
p11 = cv2.imread('limages/snap11.png') #new
p12 = cv2.imread('limages/snap12.png')
sheet = np.concatenate((p1, p2, p3, p4, p5, p6, p7, p8, p9, p10), axis=0)
cv2.imwrite('limages/sheet.png', sheet)
"""

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread('limages/splice.png')
#img = img[0:100, 125:275]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)
#good = str(qwertyuopasdfghjkzcvbnm')
blackAndWhiteImage=cv2.cvtColor(blackAndWhiteImage,cv2.COLOR_GRAY2BGR)



settings=r'--tessdata-dir "/home/marcelbonnici/Dropbox/000_LINUX/winterproject/tessdata" -l eng --oem 0 --psm 6 -c tessedit_char_whitelist=0123456789x=Tqwertyuopasdfghjkzcvbnm~ ' #կ
text = pytesseract.image_to_string(blackAndWhiteImage, config=settings)
bad = "qwertyuopasdfghjkzcvbnm~ " #qwertyuopasdfghjkzcvbnm~
boxes = pytesseract.image_to_boxes(blackAndWhiteImage, config=settings)
for ch in range(len(bad)):
    text=text.replace(bad[ch], "")

boxes=re.split('\n', boxes)
eloc=[]
product=[]
xs=[]
ys=[]
for z in range(0, len(boxes)-1):
    subb=boxes[z]
    subb=subb.encode("utf-8")

    if not subb[0] in bad:#if subb[0] is not a blacklisted character
        x1 = int(subb.rsplit(None,5)[1])
        y1 = int(subb.rsplit(None,5)[2])
        x2 = int(subb.rsplit(None,5)[3])
        y2 = int(subb.rsplit(None,5)[4])

        ratio=(y2-y1)/(x2-x1) #how big y pixelage is compared to x pixelage

        if subb[0]=="x" and (boxes[z-1][0]).isdigit()==True and (boxes[z+1][0]).isdigit()==True and x2 < int(boxes[z+1].rsplit(None,5)[1]) and x2+50 > int(boxes[z+1].rsplit(None,5)[1]) and x1 > int(boxes[z-1].rsplit(None,5)[3]) and x1-50 < int(boxes[z-1].rsplit(None,5)[3]) and ratio>0.5 and ratio<2:
            #if detechted character is an "x" and the previous and following detected characters are #s and left side of x is within 50 pixels of right side of following number and the number isn't too wide and isn't too skinny
            cv2.putText(blackAndWhiteImage, str(subb[0]), (x1,len(img)-y1), font, 1, (0, 255, 0), 2, cv2.LINE_AA) #write "x" on top of where it is detected
            if boxes[z+1][0] == "1": #if following number is a 1
                stx2=int(boxes[z+1].rsplit(None,5)[3]) #Second Ten's x2 -> ? x 1| 2
                sox1=int(boxes[z+2].rsplit(None,5)[1]) #Second One's x1 -> ? x 1 |2

                if (boxes[z+2][0] == "0" or boxes[z+2][0] == "1" or boxes[z+2][0] == "2") and stx2 < sox1 and stx2+25 > sox1:
                    #if one's place of second number is a 0, 1 or 2 and the ones place is after the tens but by no more than 25 pixels
                    n2=int(boxes[z+1][0]+boxes[z+2][0]) #the second number of the expression formed from concatenating the string of each digit
                else:
                    n2=int(boxes[z+1][0]) #if the number isn't 10, 11 or 12, it is 1
            elif (boxes[z+1][0]).isdigit()==True: #if the number isn't 1, it's whatever 1-digit number was sensed
                n2=int(boxes[z+1][0])
            if boxes[z-1][0] == "0" or boxes[z-1][0] == "1" or boxes[z-1][0] == "2": #if the one's place of the first number is 0, 1 or 2
                if boxes[z-2][0] == "1" and int(boxes[z-2].rsplit(None,5)[3]) < int(boxes[z-1].rsplit(None,5)[1]) and int(boxes[z-2].rsplit(None,5)[3])+25 > int(boxes[z-1].rsplit(None,5)[1]):
                    #if there is a tens place of 1, and that tens place is between 0-24 pixels to the left of the ones place
                    n1=int(boxes[z-2][0]+boxes[z-1][0]) #the first number of the expression formed from concatenating the string of each digit
                else:
                    n1=int(boxes[z-1][0]) #if the number isn't 10, 11 or 12, it is the 0, 1 or 2 that was initially detected
            elif (boxes[z-1][0]).isdigit()==True: #if the one's place before the multiplication sign is not suggestive of a 10, 11, or 12
                n1=int(boxes[z-1][0]) #the 1-digit number is the full number

            product.append(n1*n2) #multiply the two numbers together

            ys.append(y1)#keep an array of the y-axis location of each whitelisted, detected character
            if len(str(abs(n2)))==1: #if the second number is 1-digit
                xs.append(int(boxes[z+1].rsplit(None,5)[3])) #store the right side location of the unmistakeable ones place number in an array
            elif len(str(abs(n2)))==2: #if the second number is 2-digits
                xs.append(int(boxes[z+2].rsplit(None,5)[3])) #store the right side location of the unmistakeable ones place in an array
        if subb[0]=="=" and (boxes[z-1][0]).isdigit()==True: #if equals sign follows a number
            eloc.append(x2-int(boxes[z-1].rsplit(None,5)[3])) #get left side of numebr before equals sign #could mess up later cuz the number before the equals could be on different line

    if subb[0] in bad: #if detetcted character is blacklisted
        subb="" #don't print it
    else: #if whitelisted character, print it and its square locations
        print(subb)
eloc.sort() #sort left side of number before equal signs in ascending order
if len(eloc)==0: #if no equal signs were detected, assume the product is semi-ambiguously written to the left of the last number by 50 pixels
    eoffset=50
elif len(eloc)%2==1: #if an odd number of equal signs were detected
    eoffset=eloc[int(len(eloc)/2)] #offset=median value
else: #if even number of equal signs detected
    eoffset=abs(int((eloc[len(eloc)/2]+eloc[(len(eloc)/2)-1])/2)) #offset=median value
eoffset=eoffset+70 #semi-ambiguously add 40 pixels to each offset
for wr in range(0, len(product)): #for the number of the assumed products to calculate
    answerx=xs[wr]+eoffset # the x-coordinate of the answer is immediately to the left of the last printed number plus the offset
    answery=len(img)-ys[wr] # the y-coordinate of the answer is the lower y-coordinate of the multipliciation sign
    cv2.putText(blackAndWhiteImage, str(product[wr]), (answerx,answery-15), font, 1, (255, 0, 0), 2, cv2.LINE_AA) #write the product on the file
#print("Equals Sign Array Is: ")
#print(eoffset)
#print("---------------")
#print(text)




#for rus in range (0, len(boxes)-1):
#    subb=boxes[rus]
#    subb=subb.encode("utf-8")
#    x1 = int(subb.rsplit(None,5)[1])
#    y1 = int(subb.rsplit(None,5)[2])
#    x2 = int(subb.rsplit(None,5)[3])
#    y2 = int(subb.rsplit(None,5)[4])
#    if x1==392:
#        blackAndWhiteImage=cv2.rectangle(blackAndWhiteImage, (x1, y1), (x2, y2), (0, 0, 255), 1)



cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imwrite("bwimage.png", blackAndWhiteImage)
print("------")
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()
