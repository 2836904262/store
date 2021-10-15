import random
import openAnAccout

# 字典数据库
user = {'82097403': ['12', 123456, {'国家': '12', '省份': '12', '街道': '12', '门牌号': '12'}, 123, '中国工商银行的昌平支行']}

# 界面搭建
business = {1:'开户',2:'存钱',3:'取钱',4:'转账',5:'查询',6:'Bye'}
print('*'*18)
print('*   %s   *'%('中国工商银行'))
print('*   %s   *'%('账户管理系统'))
print('*      %s      *'%('V1.0'))
print('*'*18)
for i,j in business.items():
    print('*%s.%s          *'%(i,j))
print('*'*18)
while True:
        # 选择业务
        num = input("请输入选择")
        if num.isdigit():
            num = int(num)
            if num in business.keys():
                # 开户
                if num == 1:
                    #随机产生一个账号
                    ID = ""
                    for i in range(8):
                        ID += str(random.randint(0, 9))
                    print("这是你的账号",ID)
                    name = input("请输入姓名：")
                    while True:
                        password = input("请输入密码（六位数字）：")
                        if password.isdigit():
                            if len(password) == 6:
                                password = int(password)
                                # print("666")
                                break
                            else:
                                print("请输入六位数字")
                        else:
                            print("请输入数字")
                    address = {}
                    print("请输入地址：")
                    address['国家'] = input("国家：")
                    address['省份'] = input("省份：")
                    address['街道'] = input("街道：")
                    address['门牌号'] = input("门牌号：")
                    balance = input("请输入余额：")
                    if balance.isdigit():
                        balance = int(balance)
                    else:
                        print("请输入数字")
                    bank = "中国工商银行的昌平支行"
                    openAnAccout.accout(ID,name,password,address,balance,bank,user)
                # 存钱
                elif num == 2:
                    ID = input("请输入账号：")
                    money = int(input("请输入存入的金额："))
                    if openAnAccout.saveMoney(ID,money,user) == False:
                        print("没有该用户")
                    else:
                        print("存钱成功")
                #取钱
                elif num == 3:
                    ID = input("请输入账号：")
                    password = int(input("请输入密码："))
                    money = int(input("请输入取钱金额："))
                    openAnAccout.drawMoney(ID,password,money,user)
                #转账
                elif num == 4:
                    ID1 = input('请输入转出的账户：')
                    ID2 = input("请输入转入的账户：")
                    password = int(input("请输入转出账户的密码："))
                    money = int(input("请输入转出的金额："))
                    print(openAnAccout.transfer(ID1,ID2,password,money,user))
                #查询账户
                elif num == 5:
                    ID = input("请输入查询的账户：")
                    password = int(input("请输入密码："))
                    openAnAccout.inquire(ID,password,user)
                else:
                    break
            else:
                print("请输入正确的编号")
        elif num == 'q':
            for i,j in user.items():
                print(i,j)
        else:
            print("请输入编号")
