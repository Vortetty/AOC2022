#include <cerrno>
#include <cstdio>
#include <string>
#include <iostream>

// Using this for speed
// https://insanecoding.blogspot.com/2011/11/how-to-read-in-file-in-c.html
// https://web.archive.org/web/20221206061841/https://insanecoding.blogspot.com/2011/11/how-to-read-in-file-in-c.html
std::string get_file_contents(const char *filename) {
    std::FILE *fp = std::fopen(filename, "rb");
    if (fp) {
        std::string contents;
        std::fseek(fp, 0, SEEK_END);
        contents.resize(std::ftell(fp));
        std::rewind(fp);
        std::fread(&contents[0], 1, contents.size(), fp);
        std::fclose(fp);
        return (contents);
    }
    throw(errno);
}

// Fast
// https://www.geeksforgeeks.org/determine-string-unique-characters/ (contributed by Divyam Madaan)
// https://web.archive.org/web/20221206062457/https://www.geeksforgeeks.org/determine-string-unique-characters/ (contributed by Divyam Madaan)
bool uniqueCharacters(std::string str) {
    // Assuming string can have characters
    // a-z, this has 32 bits set to 0
    int checker = 0;

    for (int i = 0; i < str.length(); i++) {

        int bitAtIndex = str[i] - 'a';

        // if that bit is already set in
        // checker, return false
        if ((checker & (1 << bitAtIndex)) > 0) {
            return false;
        }

        // otherwise update and continue by
        // setting that bit in the checker
        checker = checker | (1 << bitAtIndex);
    }

    // no duplicates encountered, return true
    return true;
}

int main() {
    std::string in = get_file_contents("./6.txt");
    int i1 = 0;
    int i2 = 0;
    while (i1++ || 1) {
        if (uniqueCharacters(in.substr(i1, 4))) break;
    }
    while (i2++ || 1) {
        if (uniqueCharacters(in.substr(i2, 14))) break;
    }
    std::cout << "PT.1 >> " << i1 + 3 << " (" << in.substr(i1, 4) << ")\n";
    std::cout << "PT.2 >> " << i2 + 13 << " (" << in.substr(i2, 14) << ")\n";
}
