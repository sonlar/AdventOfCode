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
        for y,line in enumerate(self.f):
            for x, char in enumerate(line):
                if self.is_num(char):
                    tempnum += char
                elif tempnum:
                    num.append(tempnum)
                    tempnum = str()
        print(num)

    def is_symbol(self, char):
        if match(r"[^\w\.]", char):
            return True
        return False

    def is_num(self, char) -> bool:
        if char.isdigit():
            return True
        return False


if "__main__" == __name__:
    scheme = Day03("test.txt")
    scheme.read_file()
    scheme.find_num()
