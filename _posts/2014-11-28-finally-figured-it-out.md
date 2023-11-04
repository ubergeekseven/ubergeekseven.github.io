---
date: 2014-11-28
header:
  teaser: /img/imgplaceholder
  overlay_image: /img/imgplaceholder
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
--- 
And now that I have it figured out, I feel stupid. I guess sleeping on it
works.

While trying to get the variable to reset after the button was pushed, i was
clearing all of the variables that were sent to the button push. But not the
variable that creates the data for the other variables. I just figured that
since the value would shift so much all of the time, it would not matter if I
did clear it.

But, I cant process information in the linear fashion that this code does, so
my brain broke when I tried to reason with it. I am so glad I didn't post this
question on Stack Exchange. That would be an invitation for trolling, for
sure.

But here is my code as of now.

    
    
    
    /*
    All around joystick to easily create custom layouts 
    
    
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
        
        
        const bool DEBUG = false;  // set to true to debug the raw values
        int BUTTON_1 = 11;// LEFT TRIGGER ON PINBALL
        int BUTTON_2 = 10;//RIGHT TRIGGER ON PINBALL
        int BUTTON_3 = 9; //Used to trigger the value of the pinball shooter at its apex
        int throttlePin = A5; //One Axes for pinball shooter
        int xPin = A2;
        int yPin = A3;
        int xZero, yZero;
        int xValue, yValue;
        int deadzone = 5;  // smaller values will be set to 0
        int throttleValue;// CURRENTLY SET TO PINBALL LAUNCHER
        unsigned int maxRead ; //SET MAXREAD AS THE MAX INPUT FOR THE BALL
        unsigned int lastRead; // last stored reading greater than previous
        unsigned int pushed; //was the button pushed last time?
    
    
    
    /**************************************************************************************/
        void setup()
        {
    
        if(DEBUG) {
            Serial.begin(9600);
                   }
        
    
            maxRead = 0;  //zero the value before loop
            lastRead = 0; // zero the value before loop
            pushed = false;
         
        // Setup the button with an internal pull-up :
      
      
            pinMode(BUTTON_1,INPUT_PULLUP); 
            pinMode(BUTTON_2,INPUT_PULLUP);
            pinMode(throttlePin, INPUT);
            pinMode(xPin, INPUT);
            pinMode(yPin, INPUT);
            pinMode(BUTTON_3,INPUT_PULLUP);      
            xZero = analogRead(xPin);
        yZero = analogRead(yPin);
           
        
    
        // zero out all axis and button variables 
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
            
       
            if (digitalRead(BUTTON_1) == LOW){
            joySt.buttons += 0x01;
            
            }
            
            if (digitalRead(BUTTON_2) == LOW){
            joySt.buttons += 0x02; //adds the two inputs together
           
            }
            
            if (digitalRead(BUTTON_3) == LOW){ //if the button is pushed set pushed to true and lastread to 0 and set the axis value to the max read. lastread will read on the next loop
               joySt.zAxis = map(maxRead,0,1023,0,255);
               pushed = true;
               delay(1);
               lastRead = 0;
               
            }        
           
            xValue = analogRead(xPin) - xZero;
        yValue = analogRead(yPin) - yZero;
    
        if(abs(xValue) < deadzone) {
            xValue = 0;
        }
        if(abs(yValue) < deadzone) {
            yValue = 0;
        }
    
        throttleValue = analogRead(throttlePin);  //(throttlePin) - throttleZero;
        
        
            // THIS SECTION WILL DETERMINE THE LAST HIGHEST READING AND APPLY THAT TO THE BUTTON 
            
            if (throttleValue > lastRead) {
                     lastRead = throttleValue; // store the current throttle value in last read
            }
              else if (throttleValue <= lastRead) { //throttle is changing direction so record th elast value that was the highes t and store it 
                     maxRead = lastRead;  // store the max value in last read
                  
            }
    
            if (digitalRead(BUTTON_3) == HIGH && (pushed = true)){ // if the button is pressed and let go, set the axis back to 0
               joySt.zAxis = 0;
               pushed = false;
              }
              
    
    
    
        joySt.xAxis = map(xValue, 450, -450, 0, 255);  // here the axis is inverted
        joySt.yAxis = map(yValue, -400, 400, 0, 255);
            joySt.throttle = map(throttleValue,0,1023,0,255); // scaling the throttle value
            
            
        if(DEBUG) {
            Serial.print("X: ");
            Serial.println(xValue);
            Serial.print("Y: ");
            Serial.println(yValue);
                    Serial.print("Throttle value");
                    Serial.println(throttleValue);
                    Serial.print("maxread");
                    Serial.println(maxRead);
                    Serial.print("lastRead");
                    Serial.println(lastRead);
                    
        }
    
    //  joySt.xAxis = random(255);
    //  joySt.yAxis = random(255);
    //  joySt.zAxis = random(255);
    //  joySt.xRotAxis = random(255);
    //  joySt.yRotAxis = random(255);
    //  joySt.zRotAxis = random(255);
    //  joySt.throttle = random(255);
    //  joySt.rudder = random(255);
    //
    //  joySt.throttle++;
    //
    //
    //  joySt.buttons <<= 1;
    //  if (joySt.buttons == 0)
    //      joySt.buttons = 1;
    //
    //  joySt.hatSw1++;
    //  joySt.hatSw2--;
    //
    //  if (joySt.hatSw1 > 8)
    //      joySt.hatSw1 = 0;
    //  if (joySt.hatSw2 > 8)
    //      joySt.hatSw2 = 8;
    //
    //  delay(100);
    //
    //  if (joySt.throttle > 127)
    //      digitalWrite(13, HIGH);
    //  else
    //      digitalWrite(13, LOW);
    
    
        // Call Joystick.move
        Joystick.setState(&joySt);
    
        }

These two files enable you to replace the default HID descriptors in the
arduino IDE. To use them in your projects, with an arduino leonardo or an
arduino pro micro, rename your original files and place them in a folder
within the directory. Use the .BAK file extension to remind you that it is a
backup. The directory is in C:\Program Files
(x86)\Arduino\hardware\arduino\cores\arduino and the files to replace are
HID.cpp and USBAPI.h.

The files are below for use. I originaly saw this when first researching @
http://www.instructables.com/id/Add-a-little-two-analog-axis-thumb-joystick-
to-you/?ALLSTEPS

Then that pointed towards http://www.imaginaryindustries.com/blog/?p=80

Which gave me insight in to the working of HID. it is confusing at first, but
once you stare at the HID descriptors and play with the descriptor tool from
the USB site and some other sites that have java versions of the descriptor
tool.

And this is the list of sites I read through to understand this stuff more. It
should be comprehensive if you are willing to look through them. I pretty much
did all of the googling for you.

http://share.xmarks.com/folder/bookmarks/nOiUcxaHt6

This is using xmarks so its web based.

[ HID.cpp ](/s/HID.cpp)

[ USBAPI.h ](/s/USBAPI.h)

[ Arduino Sketch ](/s/MyJoyStick2.ino)

  

  

