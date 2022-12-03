#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstring>
#include <fstream>
#include <vector>
#include <exception>
#include <map>
#include <set>
#include <iterator>

int read_lines(const std::string& path, std::vector<std::string>& line_buffer) {
    std::ifstream file_stream(path);
    if (!file_stream.is_open()) {
        return 1;
    }
    std::string line;
    while (std::getline(file_stream, line)) {
        line_buffer.push_back(line);
    }
    return 0;
}

int main(void) {
    const char* path = "input.txt";
    std::vector<std::string> lines;
    int status = read_lines(path, lines);
    if (status != 0) {
        printf("Could not read file. Check if it exists. File name: %s\n", path);
        return 1;
    }
    return 0;
}