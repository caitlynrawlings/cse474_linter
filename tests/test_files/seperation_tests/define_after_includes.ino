// Filename: define_after_includes.ino
// Author: John Doe
// Date: 2024-06-19
// Description: This is a test file for the linter.

// This return all clear rn but ideally would return a message about `#define TAU 6.28` being in the wrong section

// =================== Macros ===================
#define PI 3.14

// ================== Includes ==================
#include <Arduino.h>
#define TAU 6.28