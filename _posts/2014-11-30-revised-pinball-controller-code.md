---
date: 2014-11-30
header:
  teaser: /img/imgplaceholder
  overlay_image: /img/imgplaceholder
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
--- 
So with my last attempt, I was using a SPST switch and attempting to use a
spring to release the button. After several failed linear pots and a half
working sketch, I tried something else.

This time I am using a endstop type switch that is SPDT and I wired the Norm
off position to the button 3 input and the Norm on position to the button 4
input. I tried to do the same sketch with the SPST using the ON position to
start the readPull() function, and it just plain will not work. This solutino
takes another input to resolve the issue, but it seems to work cleanly.

The only thing is, because the function is outside the loop, the buttons wont
work while pulling back. But, I do not think that people usually push the
buttons while pulling the shooter. And now that I write this, I could just put
the other buttons in to the function and in the off chance that you would push
them, it would still work.

Anyhow, this is the updated code. I will post the schematics another time. I
need to move on to the actual game. I wasted enough time trying to figure out
the pull shooter code.

    
    
    
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
        int BUTTON_4 = 8; //
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
        int count = 0;
        int maxCount = 100; // number of loops to allow the axis to be sent to the computer. The lower the number the less accurate the input. I will figure this out later.
    
    
    
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
            pinMode(BUTTON_4,INPUT_PULLUP);     
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
    
    
      void loop() {
              
        while(digitalRead(BUTTON_4) == HIGH){
          pushed = false;
          count = 0;   
          readPull();
        }
            
            
            if ((pushed == true) && (count <= maxCount)) { // if the button was pressed and the max count has not been reached
            joySt.zAxis = map(maxRead,0,1023,0,255); // map the output to the axis
            count++; // add one to the count
              }
             else if (count = maxCount){
               pushed = false;
               count = 0;
               joySt.zAxis = 0;
             }       
    
    
            joySt.buttons = 0x00; // off state
            
            
            if (digitalRead(BUTTON_1) == LOW){
            joySt.buttons += 0x01;
            
            }
            
            if (digitalRead(BUTTON_2) == LOW){
            joySt.buttons += 0x02; //adds the two inputs together
           
            }
            
    
    
            xValue = analogRead(xPin) - xZero;
        yValue = analogRead(yPin) - yZero;
    
        if(abs(xValue) < deadzone) {
            xValue = 0;
        }
        if(abs(yValue) < deadzone) {
            yValue = 0;
        }
    
        
    
        joySt.xAxis = map(xValue, 450, -450, 0, 255);  // here the axis is inverted
        joySt.yAxis = map(yValue, -400, 400, 0, 255);
    
            
            
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
    
    
    
    
        // Call Joystick.move
        Joystick.setState(&joySt);
    
         }
                    /**************************************************/
       void readPull() {
         
             throttleValue = analogRead(throttlePin);  //(throttlePin) - throttleZero;
             joySt.throttle = map(throttleValue,0,1023,0,255); // scaling the throttle value      
      
             if (digitalRead(BUTTON_3) == HIGH){ //if the button is pushed set pushed to true and lastread to 0 and set the axis value to the max read. lastread will read on the next loop
               pushed = true;  
               lastRead = 0;
             }
               
               // THIS SECTION WILL DETERMINE THE LAST HIGHEST READING AND APPLY THAT TO THE BUTTON 
            
            if (throttleValue > lastRead) {
                     lastRead = throttleValue; // store the current throttle value in last read
            }
              else if (throttleValue <= lastRead) { //throttle is changing direction so record th elast value that was the highes t and store it 
                     maxRead = lastRead;  // store the max value in last read
                  
            }
            
                // Call Joystick.move
        Joystick.setState(&joySt); // apparently this has to be called every time to update the position of an axis or joystick button. 
             }
    
       
                    /**************************************************/

Until next time.....

