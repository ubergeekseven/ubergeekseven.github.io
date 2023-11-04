\--- layout: post title: Pinball Controller HID code categories: [] tags: []
status: publish type: post published: true meta: {} \---

So, i worked on my controller for a while last night. I have it working, but I
need to refine the program a bit.

So far I have the left and right buttons, the trigger button and the shooter.
The left and right buttons are digital. The shooter is a linear potentiometer,
and the trigger button is digital but just sends the highest value from the
potentiometer before the button was pressed.

The thing is, I can't quite figure out what I am doing wrong with the code. I
know it has to clear the variable, but I began to get stuck in a loop last
night, so I gave up until I could think clearly again.

This is the code currently, it is adapted from this project here:
http://www.imaginaryindustries.com/blog/?p=80

/*

// this is the address of each button in the 4 bytes  
definitions :  
#define BUTTON_1 0x01  
#define BUTTON_2 0x02  
#define BUTTON_3 0x03  
#define BUTTON_4 0x04  
#define BUTTON_5 0x05  
#define BUTTON_6 0x06  
#define BUTTON_7 0x07  
#define BUTTON_8 0x08  
#define BUTTON_9 0x09  
#define BUTTON_10 0x0A  
#define BUTTON_11 0x0B  
#define BUTTON_12 0x0C  
#define BUTTON_13 0x0D  
#define BUTTON_14 0x0E  
#define BUTTON_15 0x0F  
#define BUTTON_16 0x10  
#define BUTTON_17 0x11  
#define BUTTON_18 0x12  
#define BUTTON_19 0x13  
#define BUTTON_20 0x14  
#define BUTTON_21 0x15  
#define BUTTON_22 0x16  
#define BUTTON_23 0x17  
#define BUTTON_24 0x18  
#define BUTTON_25 0x19  
#define BUTTON_26 0x1A  
#define BUTTON_27 0x1B  
#define BUTTON_28 0x1C  
#define BUTTON_29 0x1D  
#define BUTTON_30 0x1E  
#define BUTTON_31 0x1F  
#define BUTTON_32 0x20

*/

#include <Bounce2.h>  
JoyState_t joySt; // joystick HID descriptor

  
const bool DEBUG = false; // set to true to debug the raw values  
int BUTTON_1 = 11;// LEFT TRIGGER ON PINBALL  
int BUTTON_2 = 10;//RIGHT TRIGGER ON PINBALL  
int BUTTON_3 = 9; //Used to trigger the value of the pinball shooter at its
apex  
int throttlePin = A5; //One Axes for pinball shooter  
int xPin = A2;  
int yPin = A3;  
int xZero, yZero;  
int xValue, yValue;  
int deadzone = 5; // smaller values will be set to 0  
int throttleValue;// CURRENTLY SET TO PINBALL LAUNCHER  
unsigned int maxRead ; //SET MAXREAD AS THE MAX INPUT FOR THE BALL  
unsigned int lastRead; // last stored reading greater than previous  
unsigned int count;  
unsigned int count1;  
void setup()  
{

// if(DEBUG) {  
Serial.begin(57600);  

maxRead = 0; //zero the value before loop  
lastRead = 0; // zero the value before loop  
count = 0;  
count1 = 0;  
// Setup the button with an internal pull-up :  
  
  
pinMode(BUTTON_1,INPUT_PULLUP);  
pinMode(BUTTON_2,INPUT_PULLUP);  
pinMode(throttlePin, INPUT);  
pinMode(xPin, INPUT);  
pinMode(yPin, INPUT);  
pinMode(BUTTON_3,INPUT_PULLUP);  
xZero = analogRead(xPin);  
yZero = analogRead(yPin);  
  

// guessing that these values are zeroed at the beginning of the sketch  
joySt.xAxis = 0;  
joySt.yAxis = 0;  
joySt.zAxis = 0;  
joySt.xRotAxis = 0;  
joySt.yRotAxis = 0;  
joySt.zRotAxis = 0;  
joySt.throttle = 0;  
joySt.rudder = 0;  
joySt.hatSw1 = 0;  
joySt.hatSw2 = 0;  
joySt.buttons = 0;

}

  
void loop()  
{  
joySt.buttons = 0x00; // off state  
  
// if (count = 1) {  
if (digitalRead(BUTTON_3) == HIGH){  
joySt.zAxis = 0;  
// count = 0;  
}  

  
if (digitalRead(BUTTON_1) == LOW){  
joySt.buttons += 0x01;  
  
}  
  
if (digitalRead(BUTTON_2) == LOW){  
joySt.buttons += 0x02; //adds the two inputs together  
  
}  
  
  
if (digitalRead(BUTTON_3) == LOW){  
joySt.zAxis = map(maxRead,0,1023,0,255);  
// count = 1;  
  
}  
  
xValue = analogRead(xPin) - xZero;  
yValue = analogRead(yPin) - yZero;

if(abs(xValue) < deadzone) {  
xValue = 0;  
}  
if(abs(yValue) < deadzone) {  
yValue = 0;  
}

throttleValue = analogRead(throttlePin); //(throttlePin) - throttleZero;  
  
  
// THIS SECTION WILL DETERMINE THE LAST HIGHEST READING AND APPLY THAT TO THE
BUTTON  
  
if (throttleValue > lastRead) {  
lastRead = throttleValue; // store the current throttle value in last read  
}  
else if (throttleValue < lastRead) {  
maxRead = lastRead; // store the max value in last read  
}  
  
  

joySt.xAxis = map(xValue, 450, -450, 0, 255); // here the axis is inverted  
joySt.yAxis = map(yValue, -400, 400, 0, 255);  
joySt.throttle = map(throttleValue,0,1023,0,255); // scaling the throttle
value  
  
  
// if(DEBUG) {  
// Serial.print("X: ");  
// Serial.println(xValue);  
// Serial.print("Y: ");  
// Serial.println(yValue);  
// Serial.print("Throttle value");  
// Serial.println(throttleValue);  
// }

// joySt.xAxis = random(255);  
// joySt.yAxis = random(255);  
// joySt.zAxis = random(255);  
// joySt.xRotAxis = random(255);  
// joySt.yRotAxis = random(255);  
// joySt.zRotAxis = random(255);  
// joySt.throttle = random(255);  
// joySt.rudder = random(255);  
//  
// joySt.throttle++;  
//  
//  
// joySt.buttons <<= 1;  
// if (joySt.buttons == 0)  
// joySt.buttons = 1;  
//  
// joySt.hatSw1++;  
// joySt.hatSw2--;  
//  
// if (joySt.hatSw1 > 8)  
// joySt.hatSw1 = 0;  
// if (joySt.hatSw2 > 8)  
// joySt.hatSw2 = 8;  
//  
// delay(100);  
//  
// if (joySt.throttle > 127)  
// digitalWrite(13, HIGH);  
// else  
// digitalWrite(13, LOW);

  
// Call Joystick.move  
Joystick.setState(&joySt);

}

I need to figure out how to make a timer that actually counts well. I think.
But, it is thanksgiving today, and I have two sick kids. I will have to return
to this tomorrow. For now I will just think about it.

