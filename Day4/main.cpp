#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstring>
#include <fstream>
#include <vector>
#include <set>
#include <tuple>

struct range {
    int min;
    int max;

    std::vector<int> values;

    range(int _min, int _max) : min(_min), max(_max) {
        if (min == max) {
            values.push_back(min);
            return;
        }
        for (int i = min; i <= max; ++i) {
            values.push_back(i);
        }
    }
};

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

std::pair<std::string, std::string> split_to_pair(const std::string& input, char delimiter) {
    int index = input.find(delimiter);
    auto s1 = input.substr(0, index);
    auto s2 = input.substr(index+1, input.length() - index);
    return std::make_pair(s1, s2);
}

void solution(const std::vector<std::string>& lines) {
    int result_part1 = 0;
    int result_part2 = 0;

    for (const auto& line : lines) {
        auto[first_half, second_half] = split_to_pair(line, ',');
        auto[range_min1, range_max1] = split_to_pair(first_half, '-');
        auto[range_min2, range_max2] = split_to_pair(second_half, '-');

        auto range_1 = range(std::stoi(range_min1), std::stoi(range_max1));
        auto range_2 = range(std::stoi(range_min2), std::stoi(range_max2));
        auto set1 = std::set<int>(range_1.values.begin(), range_1.values.end());
        auto set2 = std::set<int>(range_2.values.begin(), range_2.values.end());

        std::vector<int> temp;
        std::set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(), std::back_inserter(temp));
        int count = temp.size();
        result_part1 += (int)(count == range_1.values.size() || count == range_2.values.size());
        result_part2 += (int)(count > 0);
    }

    printf("Results: part 1 - %d, part 2 - %d\n", result_part1, result_part2);
}

int main(void) {
    const char* path = "input.txt";
    std::vector<std::string> lines;
    int status = read_lines(path, lines);
    if (status != 0) {
        printf("Could not read file. Check if it exists. File name: %s\n", path);
        return 1;
    }

    solution(lines);

    return 0;
}