# __author: ioi
# date: 2021/5/24
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("{}*{}={}".format(j, i, i * j), end="   ")
        j += 1
    print()
    i += 1
