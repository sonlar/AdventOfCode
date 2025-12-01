import fs from "node:fs";

const data = fs.readFileSync("./input", "utf8");
const instructions = data.split(/\s/).filter(Boolean);
let dial = 50;

const score = (instruction, direction) => {
  let score = 0;
  const dir = direction === "L" ? -1 : +1;
  for (let i = 0; i < instruction; i++) {
    dial = (dial + dir + 100) % 100;
    score += dial === 0 ? +1 : 0;
  }
  return score;
};

const result = instructions
  .map((instruction) => score(instruction.slice(1), instruction.charAt(0)))
  .reduce((sum, val) => sum + val);

console.log(result);
