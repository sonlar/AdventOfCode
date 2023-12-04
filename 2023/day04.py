class Scratchcards:
    def __init__(self, file):
        self.file = file
        self.score = 0
        self.process_numbers()

    def process_numbers(self):
        num = dict()
        with open(self.file, "r") as f:
            for line in f:
                line = line[line.find(":") + 1 :]
                winners, numbers = line[: line.find("|")], line[line.find("|") + 1 :]
                for digit in winners.split():
                    num[digit] = num.get(digit, 0)
                for digit in numbers.split():
                    if digit in num:
                        num[digit] = num.get(digit, 0) + 1
                score = 0
                for x in range(sum(num.values())):
                    score *= 2
                    if score == 0:
                        score += 1
                self.score += score
                num.clear()
        self.print_score()

    def print_score(self):
        print(self.score)


Scratchcards("input.txt")
