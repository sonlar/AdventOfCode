from re import match


class Day03:
    def __init__(self, file) -> None:
        self.file = file

    def read_file(self) -> None:
        with open(self.file, "r") as f:
            self.f = f.readlines()
        
    def find_num(self) -> None:
        num = list()
        y_length = len(self.f)
        x_length = len(self.f[0])
        for y,line in enumerate(self.f):
            for x, char in enumerate(line):
                if self.is_symbol(char):
                    num.append(self.check_adjacent(y, x, y_length, x_length))
        print(sum(num))

    def check_adjacent(self, y, x, y_length, x_length) -> int:
        num_count = 0
        num = list()
        for ypos in range(y-1, y+2):
            if 0 <= ypos < y_length:
                num_pos = [-1]*3
                for xpos in range(x-1,x+2):
                    if 0<= xpos < x_length:
                        if self.is_num(self.f[ypos][xpos]) and xpos not in range(num_pos[1], num_pos[2]+1):
                            num_pos = self.extract_number(ypos, xpos, x_length)
                            num.append(num_pos[0])
                            num_count += 1
        if num_count == 2:
            return int(num[0]) * int(num[1])
        return 0

    def extract_number(self, y, x, x_length):
        n = x
        num = [str(), int(), int()]
        while 0 <= n and self.is_num(self.f[y][n]):
            num[0] = self.f[y][n] + num[0]
            n -= 1
        num[1] = n + 1
        n = x + 1
        while n < x_length and self.is_num(self.f[y][n]):
            num[0] += self.f[y][n]
            n += 1
        num[2] = n - 1
        return num
        

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
