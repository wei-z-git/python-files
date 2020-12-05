# 定义仓库
repository = dict()
# 定义购物清单对象
# mock shop_list = [('10001', 4)]
shop_list = []

# 初始化商品
def init_repo():
    goods1 = ("10001", "馒头", 88.0)
    goods2 = ("10002", "花卷", 68.0)
    goods3 = ('10003', "包子", 87)
    goods4 = ('10004', '牛腩', 39)
    goods5 = ('10005', '鸡蛋', 13)
    goods6 = ('10006', '米饭', 50)
    # 入库 ，条码做key
    repository[goods1[0]] = goods1
    repository[goods2[0]] = goods2
    repository[goods3[0]] = goods3
    repository[goods4[0]] = goods4
    repository[goods5[0]] = goods5
    repository[goods6[0]] = goods6


def show_goods():
    print('\n')
    print('♡'*32 + ' 欢迎光临馒头便利店 '+'♡'*32+'\n')
    print('馒头便利店的商品清单:')
    print('%13s%40s%10s' % ('条码', '商品名称', '单价'))
    # 遍历所有list列表
    for goods in repository.values():
        print('%15s%40s%13s' % goods)


def show_list():
    print('=' * 100)
    if not shop_list:
        print('购物车为空')
    else:
        title = "%-5s|%15s|%40s|%10s|%4s|%10s" % \
                ('ID', '条码', '商品名称', '单价', '数量', '小计')
        print(title)
        print('-'*100)
        # 计算总价价格
        sum = 0
        for i, item in enumerate(shop_list):
            # 转换商品id为索引+1
            id = i + 1
            # 获取该购物明细的第一个元素：商品条码
            code = '10001'
            # repository[条码，key值][元组序号] 对应key的元组的内容
            # 获取商品名和单价
            name = repository[code][1]
            price = repository[code][2]
            # 获取要购买的数量
            number = item[1]
            amount = number * price
            # 总计
            sum = sum + amount
            # line
            line = "%-5s|%17s|%41s|%12s|%6s|%12s" % \
                   (id, code, name, price, number, amount)
            print(line)
            print('-'*100)
            print("      总计", sum)
            print('='*100)


def add():
    # 输入条码
    code = input('请输入条码：\n')
    if code not in repository:
        print("条码不存在")
        return
    # 根据条码查找商品
    # goods = repository[code]
    # 等待输入数量
    number = input("请输入购买数量：\n")
    shop_list.append([code, int(number)])


def edit():
    id = input('请输入编辑商品的id')
    index = int(id) - 1
    item = shop_list[index]  # python列表复制均为引用，故复制后的改变原有的也改变
    print(shop_list)
    number = input('请输入新的数量: \n')
    item[1] = int(number)


def delete():
    id = input('请输入要删除的id')
    index = id - 1
    item = shop_list[index]
    print(shop_list)
    del shop_list[index]


def payment():
    # 先打印清单
    show_list()
    print('\n'*3)
    print('欢迎下次光临')
    import os
    os._exit(0)


cmd_dict = {'a': add, 'e': edit, 'd': delete, 'p': payment, 's': show_goods}


def show_conmmand():
    cmd = input('请输入操作指令：\n' +
                "添加（a)  修改（e） 删除（d） 结算（p） 超市商品(s) \n")
    if cmd not in cmd_dict:
        print('wrong')
    else:
        cmd_dict[cmd]()


init_repo()
show_goods()

while True:
    # 为了能循环进行，使用while
    show_list()
    show_conmmand()


# init_repo()
# show_goods()
# show_list()
# add()
# show_list()
# edit()
# show_list()
# # show_goods()
# # print(repository['10001'])


