import re
from dataclasses import dataclass, field
from typing import List, Callable
from operator import mul, add, mod
from collections import defaultdict
from functools import reduce

@dataclass
class Monke:
    id: int
    divisor: int
    monkey_if_true: int
    monkey_if_false: int
    operator_func: Callable[[int], int] 
    items: List[int] = field(default_factory=list)

with open('input.txt', mode='r') as f:
    lines = f.readlines()

def parse_monkeys(lines):
    monke_lists = []

    for i in range(0, len(lines), 7):
        monke_lists.append(lines[i:i+6])

    monkeys = []
    for l in monke_lists:
        _id = int(l[0].split()[1].replace(':',''))
        item_matches = re.findall(r'\d+', l[1])
        items = list(map(int, item_matches))
        divisor = int(re.findall(r'\d+', l[3])[0])
        true_val = int(re.findall(r'\d+', l[4])[0])
        false_val = int(re.findall(r'\d+', l[5])[0])

        idx = l[2].find("Operation: new = ")
        op_str = l[2][idx + len("Operation: new = "):]
        elements = op_str.split(' ')
        op = add if elements[1] == '+' else mul
        op_func = lambda x, operand=op, param=elements[2]: operand(x, x if param.strip() == "old" else int(param))
        monkeys.append(Monke(_id, divisor, true_val, false_val, op_func, items))
    return monkeys

def run_solution(monkeys, rounds, divisor, divide_op):
    inspections_map = defaultdict(int)
    monke_map = { x.id: x for x in monkeys }
    for _ in range(rounds):
        for monke in monkeys:
            for item in monke.items:
                new = monke.operator_func(item)
                newitem = divide_op(new, divisor)
                target_id = monke.monkey_if_true if newitem % monke.divisor == 0 else monke.monkey_if_false
                monke_map[target_id].items.append(newitem)
                inspections_map[monke.id] += 1
            monke.items.clear()

    s = sorted([(k, v) for k, v in inspections_map.items()], key=lambda x: x[1], reverse=True)
    print(s[0][1] * s[1][1])

# parsing occurs twice because original monkeys are mutated so we need a new batch. typing this made me realize it sounds ridicoulus but ok
monkeys = parse_monkeys(lines)
run_solution(monkeys, 20, 3, lambda x, y: x // y)
run_solution(parse_monkeys(lines), 10000, reduce(lambda x, y: x * y.divisor, monkeys, 1), mod)
