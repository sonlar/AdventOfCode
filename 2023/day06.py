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
                    elif num:
                        if line.startswith("Time:"):
                            self.time.append(int(num))
                        elif line.startswith("Distance:"):
                            self.distance.append(int(num))
                        num = str()

        print(self.time)
        print(self.distance)

if "__main__" == __name__:
    file = "input.txt"
    first_race = Race(file)
    first_race.read_file()
