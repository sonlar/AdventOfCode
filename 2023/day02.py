colors = {"red": 1, "green": 1, "blue": 1}
games = list()
power = 1
value = 1


with open("input.txt", "r") as f:
    for line in f:
        for color in colors:
            value = 1
            for amount in range(line.count(color)):
                if value < int(line[: line.find(color)].split()[-1]):
                    colors.update({color: int(line[: line.find(color)].split()[-1])})
                    value = int(line[: line.find(color)].split()[-1])
                line = line.replace(color, "x", 1)

        for color, value in colors.items():
            power *= value

        games.append(power)
        power = 1
        colors = {"red": 1, "green": 1, "blue": 1}


print(sum(games))
