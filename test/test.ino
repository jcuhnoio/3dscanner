#include <Servo.h>
Servo xServo;
Servo yServo;
int xServoPin = 9;
int yServoPin = 10;
int sensorPin = 5;
int ypos = 120;

void setup(){
  xServo.attach(xServoPin);
  yServo.attach(yServoPin);
  

  long baudRate = 9600;       // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     // NOTE2: Set the baudRate to 115200 for faster communication

  xServo.write(60); // Move servos to initial position
  yServo.write(ypos);
}

void loop(){
  bool scanning = true; // Initializing boolean for while loop
  while (ypos > 70){
    // Horizontal sweeping
    for(int servo_xpos = 60; servo_xpos < 120; servo_xpos += 1){
      xServo.write(servo_xpos);
      int sensorVal = analogRead(sensorPin);
      Serial.println(sensorVal);
      delay(50);
    }

    // Vertical scroll
    ypos -= 1;
    yServo.write(ypos);

    // Horizontal sweeping (backwards)
    for(int servo_xpos = 120; servo_xpos > 60; servo_xpos -= 1){
      xServo.write(servo_xpos);
      int sensorVal = analogRead(sensorPin);
      Serial.println(sensorVal);
      delay(50);
    }

    // Vertical scroll
    ypos -= 1;
    yServo.write(ypos);

  } 
  Serial.println("Scan complete");
}