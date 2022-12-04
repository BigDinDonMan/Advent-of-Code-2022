import { readFileSync } from 'fs';

const readFileLines = (path: string): string[] => readFileSync(path, 'utf-8').split('\n').map((s: string) => s.trim());

let lines = readFileLines("./main.ts");
console.log(lines);