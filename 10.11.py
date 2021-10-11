# 实现输入十个数字并打印10个数求和的结果。
# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
# list = []
# for i in range(10):
#     num = float(input("请输入第{}个数字：".format(i+1)))
#     list.append(num)
# sum = 0
# max = 0
# for i in range(len(list)):
#     sum+=list[i]
#     if list[i] >= max :
#         max = list[i]
# print(len(list))
# average = sum/len(list)
# print("这十个数的和为：",sum)
# print("这十个数的最大数是：",max)
# print("这十个数的平均数是：",average)

# 使用random模块，如何产生 50~150之间的数？
# import random
#
# num = random.randint(50,150)
# print(num)

# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。)
# list = []
# for i in range(3):
#     list.append(float(input("请输入第{}条线长：".format(i+1))))
# list.sort()
# if list[0]+list[1]>list[2]:
#     if list[0] == list[1] and list[0] == list[2]:
#         print("可以生成三角形,是等边三角形")
#     elif list[0] == list[1] or list[1] == list[2] or list[0] == list[2]:
#         print("可以生成三角形,是等腰三角形")
#     elif list[0]*list[0]+list[1]*list[1] == list[2]*list[2]:
#         print("可以生成三角形,是直角三角形")
#     else:
#         print("可以生成三角形,是普通三角形")
# else:
#     print("不可以生成三角形")

# 有以下两个数，使用+，-号实现两个数的调换。
# A = 56
# B = 78
# C = 0
# print("A=",A)
# print("B=",B)
# one = input("请输入符号+或-：")
# if one == "+" or one == "-":
#     C = A
#     A = B
#     B = C
#     print("A=",A)
#     print("B=",B)
# else:
#     print("输入错误！！")

# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）3次睡眠10秒，5次关闭程序
# import time
#
# root = "root"
# admin = "admin"
# i = 1
# while True:
#     if i == 4:
#         time.sleep(10)
#     if i == 6:
#         print("错误过多，请重新登录吧")
#         break
#     root1 = input("请输入用户名：")
#     admin1 = input("请输入密码：")
#     if root1 == root and admin1 == admin:
#         print("用户名密码正确，登录成功")
#         break
#     else:
#         print("用户名或密码错误，请重新输入")
#     i+=1

# 图形打印（三角，空心三角，菱形，空心菱形）
# rows = int(input("请输入列数："))
# for i in range(0,rows+1):
#     for j in range(0, rows+1 - i):
#         print(end=" ")
#     for k in range(rows+1 - i, rows+1):
#         print("*", end=" ")
#     print("")

for i in range(1,10):
    for k in range(1,10-i):
        print(end=" ")
    for j in range(1,i):
        if i>3:
        print("*",end=" ")
    print("")

# 乘法表的打印
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{}x{}={}\t'.format(j, i, i * j), end='' )
#     print('\n')

# 乘法表的倒叙打印
# for i in range(1,10):
#     for j in range(1,11-i):
#         print('{}x{}={}\t'.format(j,10-i, (10-i) * j), end='' )
#     print("\n")

# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# forg = 0
# well = 20
# dayw = 0
# dayb = 0
# while True:
#     forg+=3
#     dayw+=1
#     if forg>=well:
#         break
#     forg-=2
#     dayb+=1
# print(dayw,dayb)

# 变量名合法验证
# char = 1
# Oax_li = 1
# fLul = 1
# BYTE = 1
# print(char,Oax_li,fLul,BYTE)
# # Cy%ty = 1 不合法
# # $123 = 1  不合法
# # 3_3 = 1   不合法
# T_T = 1
# print(T_T)

# 继续完成上午的猜数字游戏的需求功能。
# 1.添加计数打印功能
# 2.添加次数金币功能和锁定系统功能。
# import random
# import time
#
# ran = random.randint(1,100)
# gold = 5000
# sl = 0
# while True:
#     print("你现在的金币数是",gold)
#     if gold <=0 :
#         print("你的金币用完了!!")
#         break
#     num = int(input("请猜数："))
#     if num == ran :
#         con = input("猜对了！！就是{}，按1继续，按其他键结束".format(num))
#         gold+=3000
#         if con == "1":
#             ran = random.randint(1,100)
#         else:
#             break
#     elif num < ran:
#         print("猜小了,扣500")
#         sl+=1
#         gold -= 500
#         if sl == 3:
#             time.sleep(5)
#             sl = 0
#     elif num > ran:
#         print("猜大了，扣500")
#         sl+=1
#         gold -= 500
#         if sl == 3:
#             time.sleep(5)
#             sl = 0


# 用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
# factorial = int(input("请输入阶乘数："))
# num = 1
# if factorial == 0:
#     print("0!=",1)
# else:
#     for i in range(1,factorial+1):
#         num*=i
#     print("{}!=".format(factorial),num)
