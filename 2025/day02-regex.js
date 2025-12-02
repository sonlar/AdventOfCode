import fs from "node:fs";

const data = fs.readFileSync("./input", "utf8");
const ids = data.split(/[,\n]/).filter(Boolean);
const ranges = ids.map((id) => id.split("-"));

console.time("regex");
const invalid = (range) => {
  let value = 0;
  const start = parseInt(range[0]);
  const end = parseInt(range[1]);

  for (let i = start; i <= end; i++) {
    const strum = i.toString();
    let re = /^(\d+)\1+$/;
    if (strum.match(re)) {
      value += i;
    }
  }
  return value;
};
const score = ranges
  .map((range) => invalid(range))
  .reduce((sum, val) => sum + val, 0);

console.log(score);
console.timeEnd("regex");
