const int buttonPin = 7;
int buttonState = 0;

const int rollStep = 8; //8  //pin to pulse for steps
const int rollDir = 9;  //9  //pin to change step direction

const int slideStep = 12;
const int slideDir = 10;

const int writeStep = 13;
const int writeDir = 11;

const int oSS = 20;
const int oSR = 10;
const int fast = 75;
void setup(){
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
  //set pins as outputs
  pinMode(rollStep, OUTPUT);
  pinMode(rollDir, OUTPUT);
  pinMode(slideStep, OUTPUT);
  pinMode(slideDir, OUTPUT);
  pinMode(writeStep, OUTPUT);
  pinMode(writeDir, OUTPUT);
  
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
}



void loop(){
  digitalWrite(2, HIGH);
  digitalWrite(4, HIGH);
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    roll();
    
    //fullSlideFWD();
    
    //number0();
    //number1();
    //number2();
    //number3();
    //number4();
    //number5();
    //number6();
    //number7();
    //number8();
    //number9();
                
    //rollREV();
    //rollREV();
    
    delay(4000);
    sectroll();
    sectroll();
    sectroll();
    sectroll();
    sectroll();
    sectroll();
    sectroll();
    sectroll();
    sectroll();
    sectroll(); //new starts here
    sectroll();
    rollREV();
    rollREV();
    rollREV();
    rollREV();
    }
}

void roll(){
    digitalWrite(rollDir, HIGH);
    for(int i = 0; i < 140; i++){
      digitalWrite(rollStep, HIGH);
      delay(1);
      digitalWrite(rollStep, LOW);
      delay(1);
      }
      Serial.println("S");
      delay(fast);
}

void sectroll(){
    digitalWrite(rollDir, HIGH);
    for(int i = 0; i < 54; i++){ //was 66
      digitalWrite(rollStep, HIGH);
      delay(1);
      digitalWrite(rollStep, LOW);
      delay(1);
      }
      Serial.println("S");
      delay(4000);
}

void rollREV(){
    digitalWrite(rollDir, LOW);
    for(int i = 0; i < 200; i++){
      digitalWrite(rollStep, HIGH);
      delay(1);
      digitalWrite(rollStep, LOW);
      delay(1);
      }
      delay(fast);
}
void fullSlideFWD(){
    digitalWrite(slideDir, HIGH);
    for(int i = 0; i < 530; i++){
      digitalWrite(slideStep, HIGH);
      delay(1);
      digitalWrite(slideStep, LOW);
      delay(1);
    }
    delay(fast);
}
void fullSlideREV(){
    digitalWrite(slideDir, LOW);
    for(int i = 0; i < 530; i++){
      digitalWrite(slideStep, HIGH);
      delay(1);
      digitalWrite(slideStep, LOW);
      delay(1);
    }
    delay(fast);
}

void write1(){
    digitalWrite(writeDir, HIGH);
    for(int i = 0; i < 25; i++){
      digitalWrite(writeStep, HIGH);
      delay(1);
      digitalWrite(writeStep, LOW);
      delay(1);
    }
    delay(fast);
}
void write0(){
    digitalWrite(writeDir, LOW);
    for(int i = 0; i < 25; i++){
      digitalWrite(writeStep, HIGH);
      delay(1);
      digitalWrite(writeStep, LOW);
      delay(1);
    }
    delay(fast);
}

void segmentSlide(){
    //digitalWrite(slideDir, HIGH);
    digitalWrite(slideDir, LOW);
    for(int i = 0; i < oSS; i++){
      digitalWrite(slideStep, HIGH);
      delay(1);
      digitalWrite(slideStep, LOW);
      delay(1);
    }
    delay(fast);
}

void segmentSlideREV(){
    digitalWrite(slideDir, HIGH);
    for(int i = 0; i < oSS; i++){
      digitalWrite(slideStep, HIGH);
      delay(1);
      digitalWrite(slideStep, LOW);
      delay(1);
    }
    delay(fast);
}

void segmentSlideTad(){
    digitalWrite(slideDir, LOW);
    for(int i = 0; i < 3; i++){
      digitalWrite(slideStep, HIGH);
      delay(1);
      digitalWrite(slideStep, LOW);
      delay(1);
    }
    delay(fast);
}

void segmentRoll(){
    digitalWrite(rollDir, HIGH);
    for(int i = 0; i < oSR; i++){
      digitalWrite(rollStep, HIGH);
      delay(1);
      digitalWrite(rollStep, LOW);
      delay(1);
      }
      delay(fast);
}

void segmentRollREV(){
    digitalWrite(rollDir, LOW);
    for(int i = 0; i < oSR; i++){
      digitalWrite(rollStep, HIGH);
      delay(1);
      digitalWrite(rollStep, LOW);
      delay(1);
      }
      delay(fast);
}

void number0(){
  write1();
  segmentSlide();
  segmentRoll();
  segmentRoll();
  segmentSlideREV();
  segmentRollREV();
  segmentRollREV();
  segmentSlide();
  write0();
  segmentSlideTad();
}

void number1(){
  segmentSlide();
  write1();
  segmentRoll();
  segmentRoll();
  write0();
  segmentRollREV();
  segmentRollREV();
  segmentSlideTad();
}

void number2(){
  write1();
  segmentSlide();
  segmentRoll();
  segmentSlideREV();
  segmentRoll();
  segmentSlide();
  write0();
  segmentRollREV();
  segmentRollREV();
  segmentSlideTad();
}

void number3(){
  write1();
  segmentSlide();
  segmentRoll();
  segmentSlideREV();
  segmentSlide();
  segmentRoll();
  segmentSlideREV();
  write0();
  segmentRollREV();
  segmentRollREV();
  segmentSlide();
  segmentSlideTad();
}

void number4(){
  write1();
  segmentRoll();
  segmentSlide();
  segmentRollREV();
  segmentRoll();
  segmentRoll();
  write0();
  segmentRollREV();
  segmentRollREV();
  segmentSlideTad();
}

void number5(){
  segmentSlide();
  write1();
  segmentSlideREV();
  segmentRoll();
  segmentSlide();
  segmentRoll();
  segmentSlideREV();
  write0();
  segmentRollREV();
  segmentRollREV();
  segmentSlide();
  segmentSlideTad();
}

void number6(){
  write1();
  segmentSlide();
  segmentSlideREV();
  segmentRoll();
  segmentRoll();
  segmentSlide();
  segmentRollREV();
  segmentSlideREV();
  write0();
  segmentRollREV();
  segmentSlide();
  segmentSlideTad();
}

void number7(){
  write1();
  segmentSlide();
  segmentRoll();
  segmentRoll();
  write0();
  segmentRollREV();
  segmentRollREV();
  segmentSlideTad();
}

void number8(){
  write1();
  segmentSlide();
  segmentRoll();
  segmentRoll();
  segmentSlideREV();
  segmentRollREV();
  segmentSlide();
  segmentSlideREV();
  segmentRollREV();
  write0();
  segmentSlide();
  segmentSlideTad();
}

void number9(){
  segmentSlide();
  segmentRoll();
  segmentRoll();
  write1();
  segmentRollREV();
  segmentRollREV();
  segmentSlideREV();
  segmentRoll();
  segmentSlide();
  write0();
  segmentRollREV();
  segmentSlideTad();
}
