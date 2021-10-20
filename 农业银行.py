import random

bank = {'15': {'account': '39583496', 'account_type': 1, 'username': '15', 'password': 115151, 'country': '1215fs', 'province': '15sfd', 'street': 'd1s5', 'door_num': '1sdf23', 'money': 0, 'bank_name': '中国农业银行昌平沙河支行'}}
choose = {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"bye"}

# 系统界面
welcome = '''
**********************************
*      中国农业银行账户管理系统       *
**********************************
*               选项              *
'''
welcome_item='''*              {0}.{1}             *'''
def bank_welcome():
    print(welcome,end="")
    for i in choose.keys():
        print(welcome_item.format(i,choose[i]))
    print("**********************************")
    print("一类账户【金卡】：最大转账额为5万，转出最大5万，转入没限制;")
    print("二类账户【普通卡】：最大转账额为2万，转出最大2万，转入没限制;")

# 用户信息
user = '''
    -----------账户信息-------------
    账号：%s
    账号类型：%s
    姓名：%s
    密码：%s
    地址：
        国家：%s
        省份：%s
        街道：%s
        门牌号：%s
    账户余额：%s
    开户行：%s
    -------------------------------     
'''

# 开户
def userInput():
    account = str(random.randint(10000000,99999999))
    while True:
        account_type = input("请选择账户类型")
        if account_type == "1" or account_type == "2":
            account_type = int(account_type)
            break
        else:
            print("别瞎输")
    username = input("请输入姓名：")
    while True:
        password = input("请输入密码（六位数字）：")
        if password.isdigit() and len(password) == 6:
            password = int(password)
            break
        else:
            print("请输入正确格式的密码")
    print("请输入地址")
    country = input("\t国家：")
    province = input("\t省份：")
    street = input("\t街道：")
    door_num = input("\t门牌号：")
    money = 0
    bank_name = "中国农业银行昌平沙河支行"
    judge =  addJudge(account,account_type,username,password,country,province,street,door_num,money,bank_name)
    if judge == 1:
        print("开户成功")
        print(user % (account, account_type, username, password, country, province, street, door_num, money, bank_name))
    elif judge == 2:
        print("用户已存在")
    else:
        print("用户已满")
# 开户判断
def addJudge(account,account_type,username,password,country,province,street,door_num,money,bank_name):
    if username in bank.keys():
        return 2
    elif len(bank)>=100:
        return 3
    else:
        bank[username] = {
            "account":account,
            "account_type":account_type,
            "username":username,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door_num":door_num,
            "money":money,
            "bank_name":bank_name
        }
        return 1

# 存钱
def saveMoney():
    account = input("请输入账号：")
    while True:
        money = input("请输入存入的金额：")
        if money.isdigit():
            money = int(money)
            break
        else:
            print("别瞎输")
    for a,b in bank.items():
        if account == b["account"]:
            b["money"]+=money
            return print("存钱成功")

    return print("账户不存在！！")

# 取钱
def drawMoney():
    account = input("请输入账号：")
    while True:
        password = input("请输入密码（六位数字）：")
        if password.isdigit() and len(password) == 6:
            password = int(password)
            break
        else:
            print("请输入正确格式的密码")
    while True:
        money = input("请输入取出的金额：")
        if money.isdigit():
            money = int(money)
            break
        else:
            print("别瞎输")
    judge = drawMoneyJudge(account,password,money)
    if judge == 1:
        print("账号不存在")
    elif judge == 2:
        print("密码错误")
    elif judge == 3:
        print("钱不够！！")
    elif judge == 0:
        print("取钱成功")
# 取钱判断
def drawMoneyJudge(account,password,money):
    for a,b in bank.items():
        if account == b["account"]:
            if password == b["password"]:
                if money <= b["money"]:
                    if b["account_type"] == 1 :

                        if money>50000:
                            print("一类卡单次限额5万元")
                            return
                        else:
                            b["money"]-=money
                            return 0
                    if b["account_type"] == 2 :
                        if money>20000:
                            print("一类卡单次限额2万元")
                            return 
                        else:
                            b["money"]-=money
                            return 0
                else:
                    return 3
            else:
                return 2
    return 1

# 转账
def transferMoney():
    account = input("请输入转出账号：")
    account1 = input("请输入转入账号：")
    while True:
        password = input("请输入转出账号密码（六位数字）：")
        if password.isdigit() and len(password) == 6:
            password = int(password)
            break
        else:
            print("请输入正确格式的密码")
    while True:
        money = input("请输入转账的金额：")
        if money.isdigit():
            money = int(money)
            break
        else:
            print("别瞎输")
    tran = transferMoneyJudge(account,account1,password,money)
    if tran == 1:
        print("账号不存在")
    elif tran == 2:
        print("密码错误")
    elif tran == 3:
        print("钱不够！！")
    else:
        print("转账成功")

# 转账判断
def transferMoneyJudge(account,account1,password,money):
    judge = drawMoneyJudge(account,password,money)
    for a,b in bank.items():
        if account1 == b["account"]:
            if judge == 0:
                b["money"]+=money;
                return 0
            else:
                return judge
    return 1

# 查询
def inquire():
    account = input("请输入账号：")
    while True:
        password = input("请输入密码（六位数字）：")
        if password.isdigit() and len(password) == 6:
            password = int(password)
            break
        else:
            print("请输入正确格式的密码")
    for a,b in bank.items():
        if account == b["account"]:
            if password == b["password"]:
                return print(user % (
                        b["account"],
                        b["account_type"],
                        b["username"],
                        b["password"],
                        b["country"],
                        b["province"],
                        b["street"],
                        b["door_num"],
                        b["money"],
                        b["bank_name"]
                        ))
            else:
                return print("密码错误")
    return print("账号不存在")


# 主模块
bank_welcome()
while True:
    num = input("请输入选择：")
    if num == "1":
        userInput()
    elif num == "2":
        saveMoney()
    elif num == "3":
        drawMoney()
    elif num == "4":
        transferMoney()
    elif num == "5":
        inquire()
    elif num == "6":
        print(6)
        break
    else:
        print("看清楚了，别瞎输")