class Day05:
    def __init__(self, input) -> None:
        self.input = input
        self.seeds = list()
        self.maps = dict()
        self.names = list()

    def extract_mapping(self) -> None:
        current_map = None
        with open(self.input, "r") as f:
            for line in f.readlines():
                line_split = line.split()
                if line.startswith("seeds:"):
                    self.seeds.extend(int(seed) for seed in line_split[1:])
                elif "map" in line:
                    current_map = line_split[0]
                    self.names.append(current_map.replace("-", "_"))
                    self.maps.update({current_map: dict()})
                elif line_split and line_split[0].isdigit():
                    line_split = [int(num) for num in line_split]
                    self.maps[current_map][(line_split[1], line_split[1]+(line_split[2]-1))] = self.maps[current_map].get((line_split[1], line_split[1]+line_split[2]-1), (line_split[0], line_split[0]+line_split[2]-1))

    def split_mapping(self):
        for name in self.names:
            setattr(self, name, self.maps.pop(name.replace("_", "-"))) 

    def find_location(self, seed) -> int:
        for name in self.names:
            name = getattr(self, name)
            for key, value in name.items():
                if key[0] <= seed <= key[1]:
                    seed = seed + (value[0] - key[0])
                    break
        return seed

    def lowest_location(self):
        lowest = float("inf")
        for seed in self.seeds:
            lowest = min(self.find_location(seed), lowest)
        return lowest


if "__main__" == __name__:
    seeds = Day05("input.txt")
    seeds.extract_mapping()
    seeds.split_mapping()
    print(seeds.lowest_location())
