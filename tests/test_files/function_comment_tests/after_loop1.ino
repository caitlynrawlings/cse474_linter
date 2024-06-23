// Filename: after_loop1.ino
// Author: John Doe
// Date: 2024-06-19
// Description: This is a test file for the linter.

// Name: updateCounter
// Description: This is the function description
int updateCounter() {
    return 3;
}

// Name: noDesc
// Description: 
int** noDesc() {
    int l = updateCounter();
    updateCounter();
    #define PI 3.14
    #include <Arduino.h>
    void updateCounter();
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

// Name: wrongName
// Description: this is the description
int** anotherFunction() {
    int l = updateCounter();
    updateCounter();
    #define PI 3.14
    #include <Arduino.h>
    void updateCounter();
}

// Name: func
// Description: This is the function description
bool* func(int a, double b) {
    int i = updateCounter();
}