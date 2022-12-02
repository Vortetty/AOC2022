#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::fstream input("./1.txt", std::ios::in);

    std::string line;
    uint64_t newInt;
    uint64_t total = 0;
    std::vector<uint64_t> elves = {0, 0, 0};
    while (std::getline(input, line)) {
        if (line.length() > 0) {
            //linestream >> newInt;
            newInt = std::atoll(line.c_str());
            total += newInt;
        } else {
            if (total > elves[0]) elves[0] = total;
            else if (total > elves[1]) elves[1] = total;
            else if (total > elves[2]) elves[2] = total;
            total = 0;
        }
    }
    if (total > elves[0]) elves[0] = total;
    else if (total > elves[1]) elves[1] = total;
    else if (total > elves[2]) elves[2] = total;

    std::cout << "#1 >> " << elves[0] << "\n";
    //std::cout << "#2 >> " << elves[1] << "\n";
    //std::cout << "#3 >> " << elves[2] << "\n";
    std::cout << "#A >> " << elves[0] + elves[1] + elves[2] << "\n";

    return 0;
}