# 添加用户
def accout(ID,name,password,address,balance,bank,user):
    if len(user)>=100:
        return 3
    elif ID in user.keys():
        return 2
    else:
        user[ID] = [name,password,address,balance,bank]
        print("开户成功")
        return 1

# 存钱
def saveMoney(ID,money,user):
    if ID in user.keys():
        user[ID][3]+=money
        return True
    else:
        return False

# 取钱
def drawMoney(ID,password,money,user):
    if ID in user.keys():
        if user[ID][1] == password:
            if money<=user[ID][3]:
                user[ID][3]-=money

                return print("取钱成功")
            else:
                print("账户余额不足")
                return 3
        else:
            print("密码错误")
            return 2
    else:
        print("账号错误")
        return 1

# 转账
def transfer(ID1,ID2,password,money,user):
    if ID1 in user.keys() and ID2 in user.keys():
        if password == user[ID1][1]:
            if money <= user[ID1][3]:
                user[ID1][3] -= money
                user[ID2][3] += money
                return print("转账成功")
            else:
                print("账户余额不足")
                return 3
        else:
            print("密码错误")
            return 2
    else:
        print("账号错误")
        return 1

# 查询
def inquire(ID,password,user):
    if ID in user.keys():
        if user[ID][1] == password:
            print("当前账户：",ID)
            print("姓名：", user[ID][0])
            print("密码：",user[ID][1])
            print("余额：", user[ID][3])
            print("用户居住地址：", user[ID][2])
            print("当前账户的开户行：", user[ID][4])
            return
        else:
            return print("密码错误")
    else:
        return print("该用户不存在")

