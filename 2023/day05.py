class Day05:
    def __init__(self, input) -> None:
        self.input = input
        self.seeds = list()

    def extract_mapping(self) -> None:
        maps = {}
        current_map = None
        with open(self.input, "r") as f:
            for line in f.readlines():
                line_split = line.split()
                if line.startswith("seeds:"):
                    self.seeds.extend(int(seed) for seed in line_split[1:])
                elif "map" in line:
                    current_map = line_split[0]
                    maps.update({current_map: dict()})
                elif current_map and line_split[0].isdigit():
                    for i in range(int(line_split[2])):
                        maps[current_map][int(line_split[0])+i] = maps[current_map].get(int(line_split[0])+i, int(line_split[1])+i)
        print(maps)





if "__main__" == __name__:
    seeds = Day05("input.txt")
    seeds.extract_mapping()
