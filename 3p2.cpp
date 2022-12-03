#include <stdint.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

uint_fast8_t getPri(uint_fast8_t a) {
    if (a > 0x60) return a - 0x60;
    else          return a - 0x26;
}

int main() {
    std::fstream input("./3.txt", std::ios::in);

    std::string line;
    uint_fast16_t total = 0;
    while (std::getline(input, line)) {
        std::string b1, b2;
        std::getline(input, b1);
        std::getline(input, b2);
        for (char c : line) {
            if (b1.find(c) != std::string::npos && b2.find(c) != std::string::npos) {
                total += getPri(c);
                break;
            }
        }
    }
    std::cout << total << "\n";
}
