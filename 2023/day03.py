class Day03:
    def __init__(self, file) -> None:
        self.file = file

    def read_file(self) -> None:
        with open(self.file, "r") as f:
            self.f = f.readlines()
        
    def find_num(self) -> None:
        num = list()
        tempnum = str()
        for line in self.f:
            for char in line:
                if self.is_num(char):
                    tempnum += char
                else:
                    if tempnum:
                        num.append(tempnum)
                        tempnum = str()

    def is_num(self, num) -> bool:
        if num.isdigit():
            return True
        return False


if "__main__" == __name__:
    scheme = Day03("test.txt")
    scheme.read_file()
    scheme.find_num()
