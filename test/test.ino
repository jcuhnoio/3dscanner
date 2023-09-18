#include <Servo.h>
Servo xServo;
Servo yServo;
int xServoPin = 9;
int yServoPin = 11;
int sensorPin = 5;
int ypos = 60;

void setup(){
  xServo.attach(xServoPin);
  yServo.attach(yServoPin);
  

  long baudRate = 9600;       // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     // NOTE2: Set the baudRate to 115200 for faster communication

  xServo.write(0); // Center servos
  yServo.write(ypos);
}

void loop(){
  bool scanning = true; // Initializing boolean for while loop
  while (scanning == true){
    // Horizontal sweeping
    for(int servo_xpos = 0; servo_xpos < 60; servo_xpos += 1){
      xServo.write(servo_xpos);
      int sensorVal = analogRead(sensorPin);
      Serial.println(sensorVal);
      delay(40);
    }
    delay(100);
    // Vertical scroll
    ypos -= 1;
    yServo.write(ypos);
    Serial.println("y servo moved");
    Serial.println(ypos);

    // Horizontal sweeping (backwards)
    for(int servo_xpos = 60; servo_xpos > 0; servo_xpos -= 1){
      xServo.write(servo_xpos);
      int sensorVal = analogRead(sensorPin);
      Serial.println(sensorVal);
      delay(40);
    }

    delay(100);
    // Vertical scroll
    ypos -= 1;
    yServo.write(ypos);
    Serial.println("y servo moved");
    Serial.println(ypos);

  } 
  if (ypos == 0) {
    scanning = false;
  }
}