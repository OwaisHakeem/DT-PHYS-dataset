# eHealth Library Procedure (Arduino Uno + e-Health v2.0)

## Purpose
Document installation and compatibility steps for the legacy eHealth library to ensure reproducibility.

## Library location (Windows)
C:\Users\Owais Hakeem\Documents\Arduino\libraries\eHealth\

## Arduino IDE requirement
Sketchbook location must be:
C:\Users\Owais Hakeem\Documents\Arduino

## Compatibility patches applied
1) Flexible array member fix (eHealth.h)
- change: uint8_t position[];  →  uint8_t position[3];

2) Deprecated AVR type fix (eHealthDisplay.h)
- add:
  #include <avr/pgmspace.h>
  #ifndef prog_uint8_t
  typedef const uint8_t prog_uint8_t;
  #endif

## Verification
A minimal sketch using `#include <eHealth.h>` compiles and uploads successfully.
