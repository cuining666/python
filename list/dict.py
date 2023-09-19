# __author: ioi
# date: 2021/5/26
menu = {
    "江苏": {
        "南京": {
            "玄武区": {},
            "白下区": {},
            "秦淮区": {},
            "建邺区": {},
            "鼓楼区": {},
            "下关区": {},
            "栖霞区": {},
            "雨花台区": {},
            "浦口区": {},
            "江宁区": {},
            "六合区": {},
            "溧水县": {},
            "高淳县": {}
        },
        "苏州": {
            "金阊区": {},
            "平江区": {},
            "沧浪区": {},
            "虎丘区": {},
            "吴中区": {},
            "相城区": {},
            "常熟市": {},
            "张家港市": {},
            "昆山市": {},
            "吴江市": {},
            "太仓市": {}
        },
        "无锡": {
            "崇安区": {},
            "南长区": {},
            "北塘区": {},
            "滨湖区": {},
            "锡山区": {},
            "惠山区": {},
            "江阴市": {},
            "宜兴市": {}
        }
    },
    "上海": {
        "上海市": {
            "黄浦区": {},
            "卢湾区": {},
            "徐汇区": {},
            "长宁区": {},
            "静安区": {},
            "普陀区": {},
            "闸北区": {},
            "虹口区": {},
            "杨浦区": {},
            "宝山区": {},
            "闵行区": {},
            "嘉定区": {},
            "松江区": {},
            "金山区": {},
            "青浦区": {},
            "南汇区": {},
            "奉贤区": {},
            "浦东新区": {},
            "崇明县": {}
        }
    }
}
current_layer = menu
parent_layers = []
while True:
    for key in current_layer:
        # Python 3.6以后，格式化字符串还有更为简洁的书写方式，就是在字符串前加上字母f，我们可以使用下面的语法糖来简化上面的代码
        print(f'{key}:{current_layer[key]}')
    choice = input(">>>").strip()
    if len(choice) == 0: continue
    if choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if parent_layers:
            current_layer = parent_layers.pop()
    elif choice == 'q':
        break
    else:
        print("无此项")
