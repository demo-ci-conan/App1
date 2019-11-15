
#include <iostream>

#include "libB/libB.h"
#include "libC/libC.h"

int main() {
    std::cout << "App1: " << std::endl;
    hello_libB(indent+1, "called from App1");
    hello_libC(indent+1, "called from App1");

    return 0;
}