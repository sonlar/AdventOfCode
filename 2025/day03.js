import fs from "node:fs";

const data = fs.readFileSync("./input", "utf8");
const lines = data.split(/[,\n]/).filter(Boolean);

const partOne = (line) => {
  let first = 0;
  let second = 0;

  for (let i = 0; i < line.length; i++) {
    if (line.at(i) > first && i < line.length - 1) {
      first = line.at(i);
      second = -1;
    } else if (line.at(i) > second) {
      second = line.at(i);
    }
  }
  return String(first + second);
};

const partTwo = (line) => {
  let bank = line.slice(0, 12).split("");
  for (let i = 12; i < line.length; i++) {
    let prev = 0;
    for (let curr = 1; curr < bank.length; curr++) {
      if (bank.at(prev) < bank.at(curr)) {
        bank.splice(prev, 1);
        bank.push(line.at(i));
        break;
      } else if (curr === bank.length - 1 && bank.at(curr) < line.at(i)) {
        bank.splice(-1, 1, line.at(i));
      }
      prev = curr;
    }
  }
  return bank.reduce((total, num) => total + num);
};

const sum = lines
  .map((line) => Number(maxBank(line)))
  .reduce((sum, val) => sum + val, 0);

console.log(sum);
