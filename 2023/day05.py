class Day05:
    def __init__(self, input) -> None:
        self.input = input
        self.seeds = list()
        self.maps = {}

    def extract_mapping(self) -> None:
        current_map = None
        with open(self.input, "r") as f:
            for line in f.readlines():
                line_split = line.split()
                if line.startswith("seeds:"):
                    self.seeds.extend(int(seed) for seed in line_split[1:])
                elif "map" in line:
                    current_map = line_split[0]
                    self.maps.update({current_map: dict()})
                elif len(line_split) > 0 and line_split[0].isdigit():
                    for i in range(int(line_split[2])):
                        self.maps[current_map][int(line_split[1])+i] = self.maps[current_map].get(int(line_split[1])+i, int(line_split[0])+i)

    def find_location(self, seed) -> int:
        for map in self.maps:
            seed = self.maps[map].get(seed, seed)
        return seed

    def lowest_location(self):
        lowest = float("inf")
        for seed in self.seeds:
            lowest = min(self.find_location(seed), lowest)
        return lowest


if "__main__" == __name__:
    seeds = Day05("input.txt")
    seeds.extract_mapping()
    print(seeds.lowest_location())
