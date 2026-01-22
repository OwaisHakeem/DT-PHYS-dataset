Step 2 — Arduino IDE Installation and Serial Communication Verification


Aim

To install and configure the Arduino Integrated Development Environment (IDE) and verify stable serial communication with the Arduino Uno.



Software Used

Arduino IDE (latest stable version)

Windows USB serial drivers (automatic)



Actions Performed

Installed Arduino IDE on the host computer.

Selected Arduino Uno as the target board in the IDE.

Selected the correct COM port assigned to the Arduino Uno.

Uploaded a basic serial test sketch to confirm communication.



Verification Sketch
void setup() {
Serial.begin(115200);
}

void loop() {
Serial.println("Arduino serial communication OK");
delay(1000);
}

Outcome

Continuous serial messages were successfully received via the Serial Monitor, confirming reliable communication between the Arduino IDE and the Arduino Uno.

