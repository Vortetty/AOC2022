#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>

std::unordered_map<char, int64_t> scoreTable = {
    {'A', 1},
    {'B', 2},
    {'C', 3},
    {'X', 1},
    {'Y', 2},
    {'Z', 3}
};

std::unordered_map<int64_t, std::unordered_map<int64_t, int64_t>> smartMoveMap = {
    { 1, { {1,3}, {2,1}, {3,2} } },
    { 2, { {1,1}, {2,2}, {3,3} } },
    { 3, { {1,2}, {2,3}, {3,1} } }
};

int64_t score(int64_t a, int64_t b) {
    int64_t score = b;
    if (a == b)           score += 3;
    else if (b - a == 1)  score += 6;
    else if (b - a == -2) score += 6;
    return score;
}

inline int64_t smartScore(int64_t a, int64_t b) {
    return score(a, smartMoveMap[b][a]);
}

int main() {
    std::fstream input("./2.txt", std::ios::in);

    std::string line;
    int64_t total = 0;
    int64_t smarttotal = 0;
    while (std::getline(input, line)) {
        int a = scoreTable[line.at(0)],
            b = scoreTable[line.at(2)];
        total += score(a, b);
        smarttotal += smartScore(a, b);
    }
    std::cout << "Naive score: " << total << "\n";
    std::cout << "Smart score: " << smarttotal << "\n";

    return 0;
}