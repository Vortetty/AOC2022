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

    std::string line;                   // current line
    uint_fast16_t containTotal = 0,     // part 1's counter
                  isectTotal = 0;       // part 2's counter
    std::stringstream in;               // stringstream to use for splitting on a character since getline only supports streams
    std::string tmp1, tmp2, tmp3, tmp4; // in order: elf 1's raw range, elf 2's raw range, current elf's beginning int, current elf's end int (last two are used for both elves at different times)
    uint_fast16_t e1[2], e2[2];         // elf 1 and elf 2
    while (std::getline(input, line)) {
        in.str(line);                              // Clear and reinitialize stringstream with the current line
        in.clear();                                // Clear and reinitialize stringstream with the current line
        std::getline(in, tmp1, ',');               // Get elf 1's raw range into tmp1, treating "," as the newline char (this is janky but it works)
        std::getline(in, tmp2, ',');               // Get elf 2's raw range into tmp2, treating "," as the newline char (this is janky but it works)
        in.str(tmp1);                              // Clear and reinitialize stringstream with elf 1's raw range
        in.clear();                                // Clear and reinitialize stringstream with elf 1's raw range
        std::getline(in, tmp3, '-');               // Get elf 1's beginning int into tmp3 (as string), treating "-" as the newline char
        std::getline(in, tmp4, '-');               // Get elf 1's end int into tmp4 (as string), treating "-" as the newline char
        e1[0] = (uint_fast16_t)atoi(tmp3.c_str()); // get int from elf1's beginning int string then store it
        e1[1] = (uint_fast16_t)atoi(tmp4.c_str()); // get int from elf1's end int string then store it
        in.str(tmp2);                              // Clear and reinitialize stringstream with elf 2's raw range
        in.clear();                                // Clear and reinitialize stringstream with elf 2's raw range
        std::getline(in, tmp3, '-');               // Get elf 2's beginning int into tmp3 (as string), treating "-" as the newline char
        std::getline(in, tmp4, '-');               // Get elf 2's end int into tmp4 (as string), treating "-" as the newline char
        e2[0] = (uint_fast16_t)atoi(tmp3.c_str()); // get int from elf2's beginning int string then store it
        e2[1] = (uint_fast16_t)atoi(tmp4.c_str()); // get int from elf2's end int string then store it

        if ((e1[0] <= e2[0] && e1[1] >= e2[1]) || (e2[0] <= e1[0] && e2[1] >= e1[1])) containTotal++; // check if elf 1's range is inside elf 2's or vice-versa, if it is increment part 1's counter
        if ((e2[0] >= e1[0] && e2[0] <= e1[1]) || (e1[0] >= e2[0] && e1[0] <= e2[1])) isectTotal++;   // check if either range starts within the other, if one does increment part 2's counter
    }
    std::cout << "PT.1 >> " << containTotal << "\n";
    std::cout << "PT.2 >> " << isectTotal << "\n";
}
