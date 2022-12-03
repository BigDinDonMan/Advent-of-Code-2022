
def get_priorities():
    d = {}
    lowercase_priority_start = 1
    uppercase_priority_start = 27
    for i in range(ord('a'), ord('z')+1):
        d[chr(i)] = lowercase_priority_start
        lowercase_priority_start += 1
    
    for i in range(ord('A'), ord('Z')+1):
        d[chr(i)] = uppercase_priority_start
        uppercase_priority_start += 1
    
    return d

priority_map = get_priorities()

with open('input.txt', mode='r') as f:
        lines = f.readlines()

def part1():
    chars = []
    for line in lines:
        h1 = line[0:len(line)//2]
        h2 = line[len(line)//2:len(line)]
        s1, s2 = set(h1), set(h2)
        chars += list(s1 & s2)

    print(sum(priority_map[c] for c in chars))

def part2():
    elf_group_size = 3
    chars = []
    for index in range(0, len(lines), elf_group_size):
        group = lines[index:index+elf_group_size]
        group = map(lambda s: s.strip(), group)
        sets = list(map(set, group))
        chars += list(map(lambda s: s.strip(), sets[0] & sets[1] & sets[2]))
    print(sum(priority_map[c] for c in chars))

part1()
part2()