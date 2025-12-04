import fs from "node:fs";

const data = fs.readFileSync("./input", "utf8");
const lines = data.trimEnd().split("\n");
const len = lines.at(0).length;
lines.unshift(".".repeat(len));
lines.push(".".repeat(len));
const border = lines.map((line) => "." + line + ".");

const checkAdjacent = (row, col) => {
  let count = 0;
  const re = /@/g;
  for (let i = row - 1; i <= row + 1; i++) {
    const adj = border[i].slice(col - 1, col + 2);
    const found = adj.match(re);
    count += found ? found.length : 0;
  }
  return count <= 4 ? true : false;
};
const rolls = (border) => {
  let count = 0;
  for (let row = 0; row < border.length; row++) {
    const line = border.at(row);
    for (let col = 0; col < line.length; col++) {
      if (border[row][col] === "@") {
        if (checkAdjacent(row, col)) count += 1;
      }
    }
  }
  console.log(count);
};
rolls(border);
