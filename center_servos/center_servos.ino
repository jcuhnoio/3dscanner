#include <Servo.h>
Servo xServo;
Servo yServo;
int xServoPin = 9;
int yServoPin = 10;

void setup() {
  // put your setup code here, to run once:
  xServo.attach(xServoPin);
  yServo.attach(yServoPin);

  xServo.write(90); // Move servos to initial position
  yServo.write(90);
}

void loop() {
  // put your main code here, to run repeatedly:

}
