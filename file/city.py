# __author: ioi
# date: 2021/5/29
# 只读模式打开文件
f = open('city.txt', 'r', encoding='utf8')
city_str = ''
for line in f:
    city_str = ''.join([city_str, line.strip()])
f.close()
# 文件内容转换为字典类型
city_dict = eval(city_str)
current_layer = city_dict
parent_layers = []
while True:
    # 只写模式打开文件，该模式每次打开会清空文件内容
    # with语句可以避免打开文件后忘记关闭，还支持同时对多个文件进行上下文管理
    with open('area.txt', 'w', encoding='utf8') as area_file:
        for key in current_layer:
            # 将内容写入文件
            area_file.write(''.join([key, '\n']))
    choice = input(">>>")
    if choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if parent_layers:
            current_layer = parent_layers.pop()
    elif choice == 'q':
        break
    else:
        ask = input("当前无此地区，是否需要添加[y/n]:")
        if ask == 'y':
            s = {choice: {}}
            # 将新字典添加到当前字典中，如果当前字典包含键相同的想，则替换它
            current_layer.update(s)
            parent_layers.append(current_layer)
            current_layer = current_layer[choice]
