// Filename: no_name.ino
// Author: John Doe
// Date: 2024-06-19
// Description: This is a test file for the linter.

// missing the name comment
// Description: this is a description
void noName(int num) {  // comment over here shouldn't cause an issue
    if (num) {
        print(num);
    }
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