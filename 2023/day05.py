with open("input.txt", "r") as f:
    seeds_to_plant = list()
    seeds_map = dict()
    for line in f.readlines():
        if line.startswith("seeds:"):
            seeds_to_plant.extend(int(seed) for seed in line.split()[1:])
    print(seeds_to_plant)
if "__main__" == __name__:
    pass
