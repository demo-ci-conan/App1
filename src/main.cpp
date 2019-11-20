
#include <iostream>

#include "libB/libB.h"
#include "libC/libC.h"

int main() {
    std::cout << "App1: " << std::endl;
    hello_libB(1, "called from App1");
    hello_libC(1, "called from App1");
    hello_libG(1, "called from App1");
    hello_libH(1, "called from App1");

    return 0;
}