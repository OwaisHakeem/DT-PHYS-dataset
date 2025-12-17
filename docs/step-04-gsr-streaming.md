# Step 4 — GSR Streaming (e-Health v2.0 + Arduino Uno)

## Aim
Stream time-stamped GSR values via Serial at 115200 baud for stress-related sensing.

## Hardware
- Arduino Uno
- e-Health Sensor Platform v2.0
- GSR electrodes

## Method
- Electrodes placed on index + middle finger of same hand.
- Sampling: 5 Hz (delay 200 ms).
- Output format: timestamp_ms,GSR

## Evidence
- Screenshot of Serial Monitor output (e.g., 49268,5.54).
- Photo of GSR connected to the GSR port.
