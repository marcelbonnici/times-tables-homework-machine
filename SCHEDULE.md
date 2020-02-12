## Week 5:
### Goals:
#### a) Read the A4988 (stepper driver) datasheet
MS1 to MS3: Leaving these three microstep selection pins disconnected results in full-step mode (setting certain ones high allows ½, ¼, ⅛ and 1/16 stepping)

1A-2B: The 1’s are one coil, The 2’s are another coil

VDD & GND: Fueled by Arduino’s 5V and GND, respectively

VMOT & Nearby GND: Connect to motor power supply; capacitor smooths out voltage spikes

DIR & STEP: DIR determines CCW or CW rotation, Arduino sends a pulse for each microstep

SLEEP: Minimizes power consumption when motor is not in use

RESET: Resets pin to predefined home state (SLEEP brings it high, enabling the board)

ENABLE: Left at “0”; disabled if set HIGH
Operates from 8 – 35V and can deliver up to 2A per coil

Short-to-ground and shorted-load protection

The current must actively be limited to under 1A to prevent damage to the motor

#### b) Redo the Schematic
![Schematic](https://drive.google.com/uc?id=1vQ-Yz2gtWRwMnAk3NjZ9Q9aPLeRKemZP)

#### c) Revamp the solderless breadboard to a soldered board
![Solderless](https://drive.google.com/uc?id=12tXcYpsLQCcfG5BND59r_yeJiCRXaZJO)

#### d) Non-LEGO Build
Elevation of rollers either causes slippage or (less commonly) is low enough where the motor shaft cannot move.

Video Summary: https://youtu.be/PJKJnOjDxVc

## Week 4:
### Goals:
#### a) Check accuracy of flagged 4's
Indeed, Tesseract can read flagged 4's well but not unflagged 4's
![Flagged 4's Success](https://drive.google.com/uc?id=126Fyc8H01b-a1vnNVNpYV-1rghVIIxss)

#### b) CAD Model
Finished designing
![CAD Model](https://drive.google.com/uc?id=1hhevIHauUj8ufHCcS13pJPmuBcdY5emo)

#### c) Improve Accuracy of Readings
i) My code for detecting which of Tesseract’s sensed values matter remains effective, but the library is worse with detecting 2 problems per line (even when cropped)

ii) Marginally better when changing the page segmentation method.

iii) Should I stick with only “one-problem-per-line” worksheets?
![Side-by-side](https://drive.google.com/uc?id=1ZkzxihR2bQ4MYTbb1v_0sxfjb63OXOiN)

## Week 3:
### Goal: Perfect the CV Readings

What Was Accomplished: Created a work-in-progress algorithm that performs splicing better than concatenating fractions of a worksheet

What Needs Improvement: The exemplary worksheet has 4 written like an upside-down "h", which tesseract cannot detect. To solve the issue, machine learning or training tesseract will likely be adopted.

![Current Worksheet](https://drive.google.com/uc?id=1PPeljTDCaGpwQ9thuLyyd3U5yvDKxsEJ)
## Week 2:
### Goals:
a) Circuit Schematic
![Schematic](https://drive.google.com/uc?id=1zkVi1hcIQvFpEZ9kJQ8lUu-UZ44Osxcb)
b) Find where to write the answers and output to serial

c) Increase reading accuracy of math problems
## Week 1: The Prototype
### Goals:
X Reassembling the prototype after transportation

X Figuring out how to make the machine more "from scratch" mechatronically

Video Summary: https://youtu.be/4DkF8HEpO0E
![Scanned Worksheet](https://drive.google.com/uc?id=1PPeljTDCaGpwQ9thuLyyd3U5yvDKxsEJ)
### a) The LEGO prototype
#### Rolling in the Worksheet
![Roll in worksheet](https://drive.google.com/uc?id=148idN9rdXBSMik1ECmNwPElVLoeeI1SS)
#### Gliding the Pen
![Glide](https://drive.google.com/uc?id=1LVtw1w3lcxQLSuAcGKF12C5SY0o-oY-S)
#### Lifting/Lowering the Pen
Lifted:
![Lift](https://drive.google.com/uc?id=1icXoNfebSrbkBTsXE-7cJH-v1EuXlAjK)
Lowered:
![Lower](https://drive.google.com/uc?id=1K24BJ-F79rWtNwnqroH9GYHnmLo8bI0A)
The motor and its green/yellow rectangular cam:
![Cam](https://drive.google.com/uc?id=12pwXxt6xH8_WjmZdWIJYvfxPbq9IiqD2)
### b) The Arduino code
Lacks how to take serial data as an input.
### c) The python code (WIP)
#### Reads the Arduino's serial messages to scan the worksheet
#### Transcribes text to calculate and print answers
