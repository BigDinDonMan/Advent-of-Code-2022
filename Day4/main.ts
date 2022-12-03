import { readFileSync } from 'fs';

function readFileLines(path: string): string[] {
    return readFileSync(path, 'utf-8').split('\n').map((s: string) => s.trim());
}

let lines = readFileLines("./main.ts");
console.log(lines);