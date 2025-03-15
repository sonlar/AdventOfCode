from re import match


class Day03:
    def __init__(self, file) -> None:
        self.file = file

    def read_file(self) -> None:
        with open(self.file, "r") as f:
            self.f = f.readlines()
        
    def find_num(self) -> None:
        num = list()
        tempnum = str()
        y_length = len(self.f)
        x_length = len(self.f[0])
        for y,line in enumerate(self.f):
            for x, char in enumerate(line):
                if self.is_num(char):
                    tempnum += char
                elif tempnum:
                    if self.check_adjacent(y, x, len(tempnum), y_length, x_length):
                        num.append(int(tempnum))
                    tempnum = str()
        print(sum(num))

    def check_adjacent(self, y, x, num_length, y_length, x_length) -> bool:
        for ypos in range(y-1, y+2):
            if 0 <= ypos < y_length:
                for xpos in range(x-num_length-1,x+1):
                    if 0<= xpos < x_length:
                        if self.is_symbol(self.f[ypos][xpos]):
                            return True
        return False

    def is_symbol(self, char) -> bool:
        if match(r"[*]", char):
            return True
        return False

    def is_num(self, char) -> bool:
        if char.isdigit():
            return True
        return False


if "__main__" == __name__:
    scheme = Day03("input.txt")
    scheme.read_file()
    scheme.find_num()
