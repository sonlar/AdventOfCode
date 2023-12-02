colors = {"red": 12, "green": 13, "blue": 14}
games = list()
wrong = False
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        wrong = False
        for color, value in colors.items():
            if wrong is True:
                break
            for amount in range(line.count(color)):
                if value < int(line[: line.find(color)].split()[-1]):
                    wrong = True
                    break
                line = line.replace(color, "x", 1)
        if wrong is False:
            games.append(int(line[line.find(" ") + 1 : line.find(":")]))

print(sum(games))
