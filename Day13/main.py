from ast import literal_eval
from typing import Union, List
from copy import deepcopy

with open('input.txt', mode='r') as f:
    lines = f.readlines()

def compare_packets(first: Union[int, List[int]], second: Union[int, List[int]]) -> int:
    if isinstance(first, int) and isinstance(second, int):
        return 1 if first < second else (0 if first == second else -1)
    elif isinstance(first, list) and isinstance(second, list):
        c_f, c_s = deepcopy(first), deepcopy(second)
        while len(c_f) > 0 and len(c_s) > 0:
            f, s = c_f.pop(0), c_s.pop(0)
            res = compare_packets(f, s)
            if res == -1 or res == 1:
                return res
        return 1 if len(c_f) < len(c_s) else 0 if len(c_f) == len(c_s) else -1
    elif (isinstance(first, int) and isinstance(second, list)):
        return compare_packets([first], second)
    elif (isinstance(first, list) and isinstance(second, int)):
        return compare_packets(first, [second])

    raise ValueError(f"Arguments have unsupported types; expected int or list of ints, got: first={type(first)}, second={type(second)}")

packets = [literal_eval(l) for l in lines if l.strip()]

packet_pairs = [(packets[i], packets[i+1]) for i in range(0, len(packets), 2)]
indices = []
for index, pair in enumerate(packet_pairs,start=1):
    if compare_packets(*pair) > 0:
        indices.append(index)

print(sum(indices))

# part 2
packets.append([[2]])
packets.append([[6]])
# classic bubble sort lets go
for i in range(len(packets)):
    for j in range(i + len(packets) - i):
        result = compare_packets(packets[i], packets[j])
        if result > 0:
            packets[i], packets[j] = packets[j], packets[i]

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))