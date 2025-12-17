#include <eHealth.h>

void setup() {
  Serial.begin(115200);
  Serial.println("timestamp_ms,GSR");
}

void loop() {
  unsigned long t = millis();
  float gsr = eHealth.getSkinConductance();
  Serial.print(t);
  Serial.print(",");
  Serial.println(gsr);
  delay(200); // 5 Hz
}
