import math

class Race:
    def __init__(self, file) -> None:
        self.file = file
        self.time = list()
        self.distance = list() 

    def read_file(self):
        with open(self.file, "r") as f:
            num = str()
            for line in f:
                for character in line:
                    if character.isdigit():
                        num += character
                if num:
                    if line.startswith("Time:"):
                        self.time.append(int(num))
                    elif line.startswith("Distance:"):
                        self.distance.append(int(num))
                    num = str()

    def calculate(self):
        combination = 1
        temp = 0
        for time, distance in zip(self.time, self.distance):
            for num in range(time):
                if ((time - num) * num > distance):
                    temp += 1
            if temp:
                combination *= temp
                temp = 0
        print(combination)

    def abc(self):
        a = 1
        b = self.time[0]
        c = self.distance[0]
        lower = math.ceil((-b - math.sqrt(math.pow(b, 2) - 4 * a* c )) / 2 * a)
        upper = math.floor((-b + math.sqrt(math.pow(b, 2) - 4 * a* c )) / 2 * a)
        combinations = len(range(lower, upper+1))
        print(combinations)

if "__main__" == __name__:
    file = "input.txt"
    first_race = Race(file)
    first_race.read_file()
    # first_race.calculate()
    first_race.abc()
