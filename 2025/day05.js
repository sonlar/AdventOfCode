import fs from "node:fs";

const data = fs.readFileSync("./input", "utf8");
const lines = data.trimEnd().split("\n");
const ranges = Array();
const numbers = Array();
lines.forEach((num) =>
  Number(num)
    ? numbers.push(Number(num))
    : ranges.push(num.split("-").map(Number)),
);
const partOne = () => {
  const isFresh = (number) =>
    ranges.some(([min, max]) => min <= number && number <= max);
  const freshCount = numbers
    .map((number) => isFresh(number))
    .reduce((count, hit) => count + hit, 0);
  return freshCount;
};
console.time("part one");
console.log(partOne());
console.timeEnd("part one");
const partTwo = () => {
  const freshID = ranges
    .sort((a, b) => a[0] - b[0])
    .reduce((merged, range) => {
      const last = merged[merged.length - 1];
      last && range[0] <= last[1]
        ? (last[1] = Math.max(range[1], last[1]))
        : merged.push(range);
      return merged;
    }, [])
    .reduce((count, [min, max]) => count + max - min + 1, 0);
  return freshID;
};
console.time("part two");
console.log(partTwo());
console.timeEnd("part two");
