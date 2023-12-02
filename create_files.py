import os

year = "2023"

os.mkdir(year)
dir = os.path.join(year + "/", "day")
for x in range(1, 26):
    with open(f"{dir}{x:02d}.py", "w", encoding="utf-8") as f:
        pass
