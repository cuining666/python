# __author: ioi
# date: 2021/5/25
salary = 5000
product = ['iphone6s', 'mac book', 'coffee', 'python book', 'bicycle']
price = [5800, 9000, 32, 80, 1500]
shopingcart_product = []
shopingcart_price = []
balance = 5000
for i in range(len(product)):
    print("{}. {} {}".format(i + 1, product[i], price[i]))
while True:
    s = input(">>>:")
    if s == "quit":
        print('您已购买以下商品：')
        for j in range(len(shopingcart_product)):
            print("{} {}".format(shopingcart_product[j], shopingcart_price[j]))
        print("您的余额为：", balance)
        print("欢迎下次光临")
        break
    else:
        num = int(s)
        if balance < price[num - 1]:
            print("余额不足，", balance - price[num - 1])
        else:
            shopingcart_product.append(product[num - 1])
            shopingcart_price.append(price[num - 1])
            balance -= price[num - 1]
            print("已加入{}到您的购物车，当前余额：{}".format(product[num - 1], balance))
