#include <stdint.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>

uint_fast8_t getPri(uint_fast8_t a) {
    if (a > 0x60) return a - 0x60;
    else          return a - 0x26;
}

int main() {
    std::fstream input("./4.txt", std::ios::in);

    std::string line;
    uint_fast16_t containTotal = 0,
                  isectTotal = 0;
    while (std::getline(input, line)) {
        std::string tmp1, tmp2, tmp3, tmp4;
        std::stringstream in(line);
        std::getline(in, tmp1, ',');
        std::getline(in, tmp2, ',');
        in.str(tmp1);
        in.clear();
        std::getline(in, tmp3, '-');
        std::getline(in, tmp4, '-');
        uint_fast16_t e1[2] = {
            (uint_fast16_t)atoi(tmp3.c_str()),
            (uint_fast16_t)atoi(tmp4.c_str())
        };
        in.str(tmp2);
        in.clear();
        std::getline(in, tmp3, '-');
        std::getline(in, tmp4, '-');
        uint_fast16_t e2[2] = {
            (uint_fast16_t)atoi(tmp3.c_str()),
            (uint_fast16_t)atoi(tmp4.c_str())
        };

        if ((e1[0] <= e2[0] && e1[1] >= e2[1]) || (e2[0] <= e1[0] && e2[1] >= e1[1])) containTotal++;
        if ((e2[0] >= e1[0] && e2[0] <= e1[1]) || (e1[0] >= e2[0] && e1[0] <= e2[1])) isectTotal++;
    }
    std::cout << "PT.1 >> " << containTotal << "\n";
    std::cout << "PT.2 >> " << isectTotal << "\n";
}
