import fs from "node:fs";

const data = fs.readFileSync("./input", "utf8");
const ids = data.split(/[,\n]/).filter(Boolean);
const ranges = ids.map((id) => id.split("-"));

const isRepeating = (line, pattern) => {
  if (line.length % pattern.length != 0) return false;
  let j = 0;
  for (let i = pattern.length; i <= line.length; i += pattern.length) {
    if (line.slice(j, i) != pattern) return false;
    j = i;
  }
  console.log(`line: ${line}, pattern: ${pattern}`);
  return true;
};

const invalid = (range) => {
  let value = 0;
  const start = parseInt(range[0]);
  const end = parseInt(range[1]);

  for (let i = start; i <= end; i++) {
    const strum = i.toString();
    const half = Math.floor(strum.length / 2);
    for (let j = 1; j <= half; j++) {
      let repeating = isRepeating(strum, strum.slice(0, j));
      if (repeating) {
        value += i;
        break;
      }
    }
  }
  return value;
};
const score = ranges
  .map((range) => invalid(range))
  .reduce((sum, val) => sum + val, 0);

console.log(score);
