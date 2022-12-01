#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::fstream input("./1.txt", std::ios::in);

    std::string line;
    std::stringstream linestream;
    uint64_t newInt;
    uint64_t total = 0;
    std::vector<uint64_t> elves = {};
    while (std::getline(input, line)) {
        linestream.clear();
        linestream << line;

        if (line.length() > 0) {
            linestream >> newInt;
            total += newInt;
        } else {
            elves.push_back(total);
            total = 0;
        }
    }
    if (total > 0) elves.push_back(total);

    std::sort(elves.begin(), elves.end(), std::greater<>());

    std::cout << "#1 >> " << elves[0] << "\n";
    std::cout << "#2 >> " << elves[1] << "\n";
    std::cout << "#3 >> " << elves[2] << "\n";
    std::cout << "#A >> " << elves[0] + elves[1] + elves[2] << "\n";

    return 0;
}