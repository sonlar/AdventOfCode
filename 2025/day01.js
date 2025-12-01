import fs from "node:fs";

const data = fs.readFileSync("./input", "utf8");
const instructions = data.split(/\s/).filter(Boolean);
let dial = 50;

const left = (instruction) => {
  for (let i = 0; i < instruction; i++) {
    dial--;
    if (dial === -1) dial = 99;
  }
  return dial ? 0 : 1;
};

const right = (instruction) => {
  for (let i = 0; i < instruction; i++) {
    dial++;
    if (dial === 100) dial = 0;
  }
  return dial ? 0 : 1;
};

const result = instructions
  .map((instruction) =>
    instruction.startsWith("L")
      ? left(instruction.slice(1))
      : right(instruction.slice(1)),
  )
  .reduce((sum, val) => sum + val);

console.log(result);
