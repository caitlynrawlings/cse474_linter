// Filename: multiline_description.ino
// Author: John Doe
// Date: 2024-06-19
// Description: This is a test file for the linter.

// =================== Macros ===================
#define PI 3.14
#define TAU 6.28

// ================== Includes ==================
#include <Arduino.h>

// ============== Global Variables ==============
int COUNTER = 0;

// ============= Function Prototypes ============
void updateCounter();

// Name: noAndNever
// Description: This is the function description
// This is a second line of description
bool* noAndNever() {
    return false;
}

void setup() {
    // setup code
    updateCounter();
    #define PI 3.14
    #include <Arduino.h>
    void updateCounter();
}

void loop() {
    // loop code
    updateCounter();
}