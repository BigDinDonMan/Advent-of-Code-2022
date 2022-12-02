#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstring>
#include <fstream>
#include <vector>
#include <exception>

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
    std::cout << "WELCOME BOYO" << std::endl;
    std::vector<std::string> lines;
    read_lines("input.txt", lines);
    for (const auto& line : lines) {
        std::cout << "Line: " << line << std::endl;
    }
    return 0;
}