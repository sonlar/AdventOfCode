digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
convert_digits = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3ree",
    "four": "f4ur",
    "five": "f5ve",
    "six": "s6x",
    "seven": "s7ven",
    "eight": "e8ght",
    "nine": "n9ne",
}
num = list()
temp_num = list()

with open("input.txt", "r") as f:
    for line in f:
        convert_line = line.strip()
        for digit in digits:
            if digit in line:
                convert_line = convert_line.replace(digit, convert_digits.get(digit))
        for char in convert_line:
            if char.isnumeric():
                temp_num.append(char)
        num.append(int(temp_num[0] + temp_num[-1]))
        temp_num.clear()
print(sum(num))
