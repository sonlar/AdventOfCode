class Scratchcards:
    def __init__(self, file):
        self.file = file
        self.process_numbers()

    def process_numbers(self):
        num = dict()
        tickets = dict()
        with open(self.file, "r") as f:
            for line_number, line in enumerate(f):
                tickets[line_number + 1] = tickets.get(line_number + 1, 0) + 1
                line = line[line.find(":") + 1 :]
                winners, numbers = line[: line.find("|")], line[line.find("|") + 1 :]
                for digit in winners.split():
                    num[digit] = num.get(digit, 0)
                for digit in numbers.split():
                    if digit in num:
                        num[digit] = num.get(digit, 0) + 1
                for ticket in range(tickets[line_number + 1]):
                    for x in range(1, sum(num.values()) + 1):
                        tickets[line_number + 1 + x] = (
                            tickets.get(line_number + 1 + x, 0) + 1
                        )
                num.clear()
        print(sum(tickets.values()))


Scratchcards("input.txt")
