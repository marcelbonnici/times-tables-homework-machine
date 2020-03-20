#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import cv2
import serial
import pytesseract
import re
import os
def splice():
    path, dirs, files = next(os.walk("/home/marcelbonnici/Dropbox/000_LINUX/winterproject/limages"))
    upper = cv2.imread('limages/snap1.png')

    upper = cv2.cvtColor(upper, cv2.COLOR_BGR2GRAY)
    (thresh, upper) = cv2.threshold(upper, 110, 255, cv2.THRESH_BINARY)
    for k in range(1, len(files)-2): #for each slice # changed from len(files)-1
        address='limages/snap'+str(k+1)+'.png'
        lower=cv2.imread(address) #newest pic is lower, previous stuff is upper
        lower = cv2.cvtColor(lower, cv2.COLOR_BGR2GRAY)
        (thresh, lower) = cv2.threshold(lower, 90, 255, cv2.THRESH_BINARY) #B&W
        match=0
        candidates=[]
        for j in range(0, 24): #for height
            for i in range(0, 640): #for width
                if np.any(upper[len(upper)-24+j, i]==lower[j, i]) and np.any(lower[j, i]==[255, 255, 255]): #if a pixel between the 25 last of upper and 25 first of lower are both white
                    match=match+1 #keep tally of how many matching whites are in each row
            candidates.append(match)
            match=0 #once the white pixel tally is saved, clear match for next row
        biggest=candidates.index(max(candidates)) #index of most similar row of the overlapping pictures
        upper=upper[:len(upper)-24+biggest] #change the endpoint of the upper to the index where best row is
        lower=lower[biggest:]
        sheet = np.concatenate((upper, lower), axis=0)
        upper=sheet
        cv2.imwrite('limages/splice.png', sheet)
"""
arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)
cnt = 0
while cnt < 9: #12
    if (arduinoSerialData.inWaiting()>0):

        myData = arduinoSerialData.readline()
        #print myData

        cap = cv2.VideoCapture(2) # video capture source camera (Here webcam of laptop)
        ret,frame = cap.read() # return a single frame in variable `frame`
        cnt = cnt+1
        snapname = 'limages/snap'+str(cnt)+'.png'

        frame = frame[215:315] #230:328
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

sheet = np.concatenate((p1, p2, p3, p4, p5, p6, p7, p8, p9), axis=0)
cv2.imwrite('limages/sheet.png', sheet)
"""
#splice()
font = cv2.FONT_HERSHEY_SIMPLEX
#img = cv2.imread('limages/splice.png')
img = cv2.imread('limages/sheet.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(gray, 103, 255, cv2.THRESH_BINARY)
height=825
blackAndWhiteImage = blackAndWhiteImage [75:, 55:585] #55:585
blackAndWhiteImage=cv2.cvtColor(blackAndWhiteImage,cv2.COLOR_GRAY2BGR)
settings=r'--tessdata-dir "/home/marcelbonnici/Dropbox/000_LINUX/winterproject/tessdata" -l eng --oem 0 --psm 13 -c tessedit_char_whitelist=T0123456789x=qwertyuopasdfghjkzcvbnm~ ' #կ
text = pytesseract.image_to_string(blackAndWhiteImage, config=settings)
bad = "qwertyupasdfghjkzcvbnm~" #qwertyuopasdfghjkzcvbnm~
boxes = pytesseract.image_to_boxes(blackAndWhiteImage, config=settings)

"""
for bz in boxes:
    print(bz)
    #blackAndWhiteImage=cv2.rectangle(blackAndWhiteImage, (int(boxes[bz][1]), height-int(boxes[bz][2])), (int(boxes[bz][3]), height-int(boxes[bz][4])), (255, 0, 0), 1)
for ch in range(len(bad)):
    text=text.replace(bad[ch], "")
"""

boxes=re.split('\n', boxes)
eloc=[]
product=[]
xs=[]
ys=[]
goodielist=[]
boxedit=[]

for z in range(0, len(boxes)-1):
    subb=boxes[z]
    subb=subb.encode("utf-8")
    x1 = int(subb.rsplit(None,5)[1])
    y1 = int(subb.rsplit(None,5)[2])
    x2 = int(subb.rsplit(None,5)[3])
    y2 = int(subb.rsplit(None,5)[4])
    productpix=(int(x2)-int(x1))*(int(y2)-int(y1))
    if not subb[0] in bad and productpix>50 and productpix<2000:#if subb[0] is not a blacklisted character

        goodie = [subb[0], x1, y1, x2, y2]
        goodielist.append(goodie)
        blackAndWhiteImage=cv2.rectangle(blackAndWhiteImage, (x1, height-y1), (x2, height-y2), (0, 0, 255), 1)
boxes=goodielist
print(len(boxes))
app1=['7', 305, -21, 308, 30]
boxes.append(app1)
boxes.sort(key=lambda x: x[2], reverse=True)

while len(boxes)>1:
    row=[]
    det=0
    while int(boxes[0][2])-20<boxes[det][2]:
        row.append(boxes[det])
        det=det+1
    del boxes[:det]
    row.sort(key=lambda x: x[1])
    for hh in range (0, len(row)):
        boxedit.append(row[hh])
boxes=boxedit
for za in range (0, len(boxes)):
    if boxes[za][0]=='o':
        boxes[za][0]='0'
    print(boxes[za])
print(len(boxes))
#blackAndWhiteImage=cv2.rectangle(blackAndWhiteImage, (634, height-314), (640, height-330), (255, 0, 0), 1)
for z in range(0, len(boxes)):
    subb=boxes[z]
    x1 = int(boxes[z][1])
    y1 = int(boxes[z][2])
    x2 = int(boxes[z][3])
    y2 = int(boxes[z][4])

    ratio=(y2-y1)/(x2-x1) #how big y pixelage is compared to x pixelage

    if subb[0]=="x" and (boxes[z-1][0]).isdigit()==True and (boxes[z+1][0]).isdigit()==True and x2 < int(boxes[z+1][1]) and x2+100 > int(boxes[z+1][1]) and x1 > int(boxes[z-1][3]) and x1-100 < int(boxes[z-1][3]) and ratio>0.5 and ratio<2:
        #if detected character is an "x" and the previous and following detected characters are #s and left side of x is within 100 pixels of right side of following number and the number isn't too wide and isn't too skinny
        cv2.putText(blackAndWhiteImage, str(subb[0]), (x1,height-y1), font, 1, (0, 255, 0), 2, cv2.LINE_AA) #write "x" on top of where it is detected
        if boxes[z+1][0] == "1": #if following number is a 1
            stx2=int(boxes[z+1][3]) #Second Ten's x2 -> ? x 1| 2
            sox1=int(boxes[z+2][1]) #Second One's x1 -> ? x 1 |2

            if (boxes[z+2][0] == "0" or boxes[z+2][0] == "1" or boxes[z+2][0] == "2") and stx2 < sox1 and stx2+25 > sox1:
                #if one's place of second number is a 0, 1 or 2 and the ones place is after the tens but by no more than 25 pixels
                n2=int(boxes[z+1][0]+boxes[z+2][0]) #the second number of the expression formed from concatenating the string of each digit
            else:
                n2=int(boxes[z+1][0]) #if the number isn't 10, 11 or 12, it is 1
        elif (boxes[z+1][0]).isdigit()==True: #if the number isn't 1, it's whatever 1-digit number was sensed
            n2=int(boxes[z+1][0])
        if boxes[z-1][0] == "0" or boxes[z-1][0] == "1" or boxes[z-1][0] == "2": #if the one's place of the first number is 0, 1 or 2
            if boxes[z-2][0] == "1" and int(boxes[z-2][3]) < int(boxes[z-1][1]) and int(boxes[z-2][3])+25 > int(boxes[z-1][1]):
                #if there is a tens place of 1, and that tens place is between 0-24 pixels to the left of the ones place
                n1=int(boxes[z-2][0]+boxes[z-1][0]) #the first number of the expression formed from concatenating the string of each digit
            else:
                n1=int(boxes[z-1][0]) #if the number isn't 10, 11 or 12, it is the 0, 1 or 2 that was initially detected
        elif (boxes[z-1][0]).isdigit()==True: #if the one's place before the multiplication sign is not suggestive of a 10, 11, or 12
            n1=int(boxes[z-1][0]) #the 1-digit number is the full number

        product.append(n1*n2) #multiply the two numbers together

        ys.append(y1)#keep an array of the y-axis location of each whitelisted, detected character
        if len(str(abs(n2)))==1: #if the second number is 1-digit
            xs.append(int(boxes[z+1][3])) #store the right side location of the unmistakeable ones place number in an array
        elif len(str(abs(n2)))==2: #if the second number is 2-digits
            xs.append(int(boxes[z+2][3])) #store the right side location of the unmistakeable ones place in an array
    if subb[0]=="=" and (boxes[z-1][0]).isdigit()==True: #if equals sign follows a number
        eloc.append(x2-int(boxes[z-1][3])) #get left side of numebr before equals sign #could mess up later cuz the number before the equals could be on different line

eloc.sort() #sort left side of number before equal signs in ascending order
if len(eloc)==0: #if no equal signs were detected, assume the product is semi-ambiguously written to the left of the last number by 50 pixels
    eoffset=50
elif len(eloc)%2==1: #if an odd number of equal signs were detected
    eoffset=eloc[int(len(eloc)/2)] #offset=median value
else: #if even number of equal signs detected
    eoffset=abs(int((eloc[int(len(eloc)/2)]+eloc[int((len(eloc)/2)-1)])/2)) #offset=median value
eoffset=eoffset+5 #semi-ambiguously add 40 pixels to each offset
for wr in range(0, len(product)): #for the number of the assumed products to calculate
    answerx=xs[wr]+eoffset # the x-coordinate of the answer is immediately to the left of the last printed number plus the offset
    answery=height-ys[wr] # the y-coordinate of the answer is the lower y-coordinate of the multipliciation sign
    cv2.putText(blackAndWhiteImage, str(product[wr]), (answerx,answery-0), font, 1, (0, 0, 255), 2, cv2.LINE_AA) #write the product on the file


cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imwrite("bwimage.png", blackAndWhiteImage)
print("------")
#print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()
