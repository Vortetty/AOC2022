#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdint.h>
#include <string>
#include <vector>

int main() {
    std::fstream input("./5.txt", std::ios::in);

    std::string line;  // current line
    std::vector<std::vector<char>> pre_crates;
    std::vector<std::vector<char>> rot_crates;
    std::vector<std::vector<char>> crates1;
    std::vector<std::vector<char>> crates2;
    while (std::getline(input, line) && line.size() > 0) {
        pre_crates.push_back(std::vector<char>(line.begin(), line.end()));
    }
    rot_crates.resize(std::max_element(
                          pre_crates.begin(), pre_crates.end(),
                          [](const std::vector<char> &a, const std::vector<char> &b) {
                              return a.size() < b.size();
                          })
                          ->size());
    for (auto &crate : rot_crates) {
        crate.resize(pre_crates.size());
    }
    for (int x = 0; x < pre_crates.size(); x++) {
        for (int y = 0; y < rot_crates.size(); y++) {
            rot_crates[y][pre_crates.size() - x - 1] = pre_crates[x][y];
        }
    }

    std::copy_if(rot_crates.begin(), rot_crates.end(), std::back_inserter(crates1), [](std::vector<char> i) {
        return i[0] != ' ';
    });
    for (auto &crate : crates1) {
        auto it = std::find(crate.begin(), crate.end(), ' ');
        if (it != crate.end()) crate.erase(it, crate.end());
        crate.erase(crate.begin());
    }
    std::copy(crates1.begin(), crates1.end(), std::back_inserter(crates2));

    std::string i1, i2, i3;
    int i1i, i2i, i3i;
    char tmp;
    while (std::getline(input, line, ' ') && line == "move") {
        std::getline(input, i1, ' ');
        std::getline(input, line, ' ');
        std::getline(input, i2, ' ');
        std::getline(input, line, ' ');
        std::getline(input, i3, '\n');

        i1i = atoi(i1.c_str());
        i2i = atoi(i2.c_str()) - 1;
        i3i = atoi(i3.c_str()) - 1;

        crates1[i3i].insert(crates1[i3i].end(), std::make_move_iterator(crates1[i2i].rbegin()), std::make_move_iterator(crates1[i2i].rbegin() + i1i));
        crates1[i2i].erase(crates1[i2i].end() - i1i, crates1[i2i].end());

        crates2[i3i].insert(crates2[i3i].end(), std::make_move_iterator(crates2[i2i].end() - i1i), std::make_move_iterator(crates2[i2i].end()));
        crates2[i2i].erase(crates2[i2i].end() - i1i, crates2[i2i].end());
    }

    for (auto i : crates1)
        std::cout << i[i.size() - 1];
    std::cout << "\n";
    for (auto i : crates2)
        std::cout << i[i.size() - 1];
    std::cout << "\n";

    return 0;
}
