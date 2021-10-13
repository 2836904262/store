# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# 1、请循环遍历出所有的key
# for key,value in dict.items():
#     print('key=',key)

# 2、请循环遍历出所有的value
# for key,value in dict.items():
#     print('value=', value)
# 3、请在字典中增加一个键值对,"k4":"v4"
# dict["k4"]="v4"
# print(dict)

# ----------------------------------------
# 苹果  32.8
# 香蕉  22
# 葡萄  15.5
# 请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
# 用水果名称做key，金额做value，创建一个字典
# info = {
#     '苹果':32.8,
#     '香蕉': 22,
#     '葡萄': 15.5
# }
# fruits = input('请输入水果名称：')
# if fruits in info.keys():
#     print("%s的费用是%s元"%(fruits,info[fruits]))
# else:
#     print("没买这个水果")

# ---------------------------------
# 小明，小刚去超市里购买水果
# 小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
# 以姓名做key，value仍然是字典

# Friuts = {
# 	'苹果':12.3,  # 水果和单价
# 	'草莓':4.5,
#     '香蕉':6.3,
#     '葡萄':5.8,
#     '橘子':6.4,
#     '樱桃':15.8
# }
# info = {
#     '小明': {
#         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
#         'money':{}
#     },
#     '小刚': {
#         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
#         'money': {}
#     }
# }
# for name,value in info.items():
#     for fruits1,value1 in value.items():
#         men = 0
#         for fruits2,value2 in info[name]['fruits'].items():
#             for i, unit in Friuts.items():
#                 if i == fruits2:
#                     men +=value2*unit
#         info[name]['money']=men
# print(info)
# def money(name):
#     men = 0
#     for fruits,value in info[name].items():
#         for fruits2,value2 in value.items():
#             # print(fruits2, value2)
#             for i,unit in Friuts.items():
#                 if i == fruits2:
#                     men+=value2*unit
#     return men
# print(money('小刚'))
# info['小刚']['money']=money('小刚')
# print(info['小刚']['money'])

# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）
# list = [1,5,3,4,3,2,5,3,6,2]
# def num(list):
#     dict = {}
#     for i in list:
#         if i in dict.keys():
#             dict[i]+=1
#         else:
#             dict[i]=1
#     for i,j in dict.items():
#         print("%s有%s个"%(i,j))
#     return
# num(list)

# 有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# list = ['年龄','性别','编号','任职公司','薪资','部门编号']
# dict = {}
# for i in names:
#     dict2 = {}
#     for j in range(len(list)):
#         dict2[list[j]]=i[j+1]
#     dict[i[0]]=dict2
# print(dict)