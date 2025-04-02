// Define the pins to output PWM
int pwmPins[] = {9, 10, 11, 12};  // You can change these pins

void setup() {
  Serial.begin(9600);
  
  // Set the pins as output
  for (int i = 0; i < 4; i++) {
    pinMode(pwmPins[i], OUTPUT);
  }
}

void loop() {
  // Read PWM values from the serial port
  if (Serial.available() >= 4) {
    int pwmValues[4];
    
    for (int i = 0; i < 4; i++) {
      pwmValues[i] = Serial.read(); // Read a byte from the serial port (0-255)
    }
    
    // Apply PWM values to the corresponding pins
    for (int i = 0; i < 4; i++) {
      analogWrite(pwmPins[i], pwmValues[i]);
    }
  }
}
