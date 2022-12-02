input_path = './input.txt'

with open(input_path, mode='r') as f:
    nums = list(map(lambda x: int(s) if (s := x.strip()) else 0, f.readlines()))

zero_indices = [i for i, val in enumerate(nums) if val == 0]
elf_calories = []
start = 0
for index in zero_indices:
    calories = nums[start:index]
    elf_calories.append(sum(calories))
    start = index


# part 2
from itertools import permutations

elf_threes = permutations(elf_calories, 3)
print(max(sum(e) for e in elf_threes))