#include <stdint.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <string>

uint_fast8_t getPri(uint_fast8_t a) {
    if (a > 0x60) return a - 0x60;
    else          return a - 0x26;
}

// faster
// https://stackoverflow.com/a/16826908
// https://web.archive.org/web/20221206083933/https://stackoverflow.com/questions/16826422/c-most-efficient-way-to-convert-string-to-int-faster-than-atoi/16826908 (from paddy's answer)
uint_fast16_t fast_atoi( const char * str )
{
    uint_fast16_t val = 0;
    while( *str ) {
        val = val*10 + (*str++ - '0');
    }
    return val;
}

int main() {
    std::fstream input("./4.txt", std::ios::in);

    std::string line;                   // current line
    uint_fast16_t containTotal = 0,     // part 1's counter
                  isectTotal = 0;       // part 2's counter
    uint_fast16_t e1[2], e2[2];         // elf 1 and elf 2
    while (std::getline(input, line, '-')) {
        e1[0] = fast_atoi(line.c_str());
        std::getline(input, line, ',');
        e1[1] = fast_atoi(line.c_str());
        std::getline(input, line, '-');
        e2[0] = fast_atoi(line.c_str());
        std::getline(input, line, '\n');
        e2[1] = fast_atoi(line.c_str());

        if ((e1[0] <= e2[0] && e1[1] >= e2[1]) || (e2[0] <= e1[0] && e2[1] >= e1[1])) containTotal++; // check if elf 1's range is inside elf 2's or vice-versa, if it is increment part 1's counter
        if ((e2[0] >= e1[0] && e2[0] <= e1[1]) || (e1[0] >= e2[0] && e1[0] <= e2[1])) isectTotal++;   // check if either range starts within the other, if one does increment part 2's counter
    }
    std::cout << "PT.1 >> " << containTotal << "\n";
    std::cout << "PT.2 >> " << isectTotal << "\n";
}
