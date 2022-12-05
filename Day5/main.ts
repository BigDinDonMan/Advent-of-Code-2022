import { readFileSync } from 'fs';

const readFileLines = (path: string) => readFileSync(path, 'utf-8').split('\n').map(s => s.trim());

const lines = readFileLines("./input.txt");

const stacks = [
    ['D','M','S','Z','R','F','W','N'],
    ['W','P','Q','G', 'S'],
    ['W','R','V','Q','F','N','J','C'],
    ['F','Z','P','C','G','D','L'],
    ['T', 'P', 'S'],
    ['H','D','F','W','R','L'],
    ['Z','N','D','C'],
    ['W','N','R','F','V','S','J','Q'],
    ['R','M','S','G','Z','W','V'],
];

function parseMoveData(input: string): number[] {
    const occurences = [...input.matchAll(/\d+/g)];
    return occurences.map(match => Number(match));
}

//hey, as long as it works
function deepCopyArray(a: any): any {
    return JSON.parse(JSON.stringify(a));
}

function getResult(a: any): string {
    return a.map((stack: any) => stack[stack.length - 1]).filter((element: any) => !!element).join('');
}

function part1(lines: string[]) {
    const newStacks = deepCopyArray(stacks);
    lines.forEach((line: string) => {
        const [moveCount, srcStack, destStack] = parseMoveData(line);

        for (let i = 0; i < moveCount; ++i) {
            const item = newStacks[srcStack-1].pop() || '';
            newStacks[destStack-1].push(item);
        }
    });

    console.log(getResult(newStacks));
}

function part2(lines: string[]) {
    const newStacks = deepCopyArray(stacks);
    for (let i = 0; i < lines.length; ++i) {
        const line = lines[i];

        const [moveCount, srcStack, destStack] = parseMoveData(line);
        let tempArray: string[] = [];
        for (let i = 0; i < moveCount; ++i) {
            let stack = newStacks[srcStack - 1];
            tempArray.push(stack.pop() || '');
        }
        tempArray = tempArray.reverse();
        tempArray.forEach(e => newStacks[destStack - 1].push(e));
    }

    console.log(getResult(newStacks));
}

part1(lines);
part2(lines);