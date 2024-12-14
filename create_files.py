import os

year = "2024"

os.mkdir(year)
dir = os.path.join(os.getcwd(), year, "day")
for x in range(1, 26):
    dirx = os.path.join(dir + f"{x:02d}")
    os.mkdir(dirx)
    os.chdir(dirx)
    with open(f"day{x:02d}.go", "w", encoding="utf-8") as f:
        pass
    
    os.chdir("..")
