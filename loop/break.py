# __author: ioi
# date: 2021/5/24
# 跳出两层循环
exit_flag = False
for i in range(10):
    if i > 5:
        break
    print(i)
    for j in range(10):
        if j == 6:
            exit_flag = True
            break
        print("layer2:%d", j)
    if exit_flag:
        break
