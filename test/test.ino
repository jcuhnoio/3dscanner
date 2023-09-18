#include <Servo.h>
Servo servo1;
int horServoPin = 9;
int vertServoPin = 11;
int sensorPin = 5;

void setup(){
  servo1.attach(horServoPin);
  servo2.attach(vertServoPin);
  bool scanning = True; // Initializing boolean for while loop

  long baudRate = 9600;       // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     // NOTE2: Set the baudRate to 115200 for faster communication

  servo1.write(0); // Center servos
  servo2.write(0);
  servo2.write(ypos);
  int ypos = -60;
}

void loop(){
  while (scanning == True){
    // Horizontal sweeping
    for(servo_xpos = 0; servo_xpos < 500; servo_xpos += 0.5){
      servo1.writeMicroseconds(servo_xpos);
      sensorVal = analogRead(sensorPin);
      Serial.println(sensorVal);
      delay(40);
    }
    // Vertical scroll
    ypos += 0.5;
    servo2.write(ypos);

    // Horizontal sweeping (backwards)
    for(servo_xpos = 500; servo_xpos > 0; servo_xpose -= 0.5){
      servo1.writeMicroseconds(servo_xpos);
      sensorVal = analogRead(sensorPin);
      Serial.println(sensorVal);
      delay(40);
    }

  } 
}