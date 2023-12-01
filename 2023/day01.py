with open("input.txt", "r") as f:
    num = list()
    tempnum = list()
    for line in f:
        for char in line:
            if char.isdigit():
                tempnum.append(char)
        num.append(int(tempnum[0] + tempnum[-1]))
        tempnum.clear()
print(sum(num))
