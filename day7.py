import xlrd

# 打开excle
wb = xlrd.open_workbook(filename=r"C:\Users\高志远\Desktop\python\day7\任务\2020年每个月的销售情况.xlsx",encoding_override=True)

# 全年的销售总额
'''
sum = 0
for i in range(12):
    table = wb.sheet_by_index(i)
    data = table.col_values(2)
    data2 = table.col_values(4)
    for j in range(1,len(data)):
        for h in range(1,len(data2)):
            if j == h:
                sum+=data[j]*data2[h]
print(sum)
'''
# 每种衣服的销售（件数）占比 二月
'''
table_two = wb.sheet_by_name("2月")
dict = {}
inventory = {}
for i in range(1,table_two.nrows):
    data = table_two.row_values(i)
    if data[1] in dict.keys():
        dict[data[1]] += data[4]
    else:
        dict[data[1]] = data[4]
for i in range(1,table_two.nrows):
    data = table_two.row_values(i)
    if data[1] not in inventory.keys():
        inventory[data[1]] = data[3]
print(dict)
print(inventory)
for a in dict.keys():
    for b in inventory.keys():
        if a == b:
            print("%s的销售量为%s,库存量为%s,销售占比为%s"%(a,dict[a],inventory[b],format(dict[a]/inventory[b],'.1%')))
'''
# 最畅销的衣服是那种
'''
table_two = wb.sheet_by_name("2月")
dict = {}
max = 0
for i in range(1,table_two.nrows):
    data = table_two.row_values(i)
    if data[1] in dict.keys():
        dict[data[1]] += data[4]
    else:
        dict[data[1]] = data[4]
for i,j in dict.items():
    if j > max:
        max = j
for i in dict.keys():
    if dict[i] == max:
        print('本月最畅销的衣服是',i)
'''
# 每个季度最畅销的衣服
'''
names = wb.sheet_names()
dict = {"第一季度":{},"第二季度":{},"第三季度":{},"第四季度":{}}
for i in names:
    table = wb.sheet_by_name(i)
    if i == "2月" or i == "3月" or i == "4月":
        for j in range(1,table.nrows):
            data = table.row_values(j)
            if data[1] in dict["第一季度"].keys():
                dict["第一季度"][data[1]] += data[4]
            else:
                dict["第一季度"][data[1]] = data[4]
    elif i == "5月" or i == "6月" or i == "7月":
        for j in range(1,table.nrows):
            data = table.row_values(j)
            if data[1] in dict["第二季度"].keys():
                dict["第二季度"][data[1]] += data[4]
            else:
                dict["第二季度"][data[1]] = data[4]
    elif i == "8月" or i == "9月" or i == "10月":
        for j in range(1,table.nrows):
            data = table.row_values(j)
            if data[1] in dict["第三季度"].keys():
                dict["第三季度"][data[1]] += data[4]
            else:
                dict["第三季度"][data[1]] = data[4]
    elif i == "11月" or i == "12月" or i == "1月":
        for j in range(1,table.nrows):
            data = table.row_values(j)
            if data[1] in dict["第四季度"].keys():
                dict["第四季度"][data[1]] += data[4]
            else:
                dict["第四季度"][data[1]] = data[4]
for i,j in dict.items():
    max(j.values())
    for a in j.keys():
        if j[a] == max(j.values()):
            print(i,"最大销量的是%s，销量为%s"%(a,j[a]))
'''
# 每件衣服的月销售（件数）占比
'''
table_two = wb.sheet_by_name("2月")
dict = {}
for i in range(1,table_two.nrows):
    data = table_two.row_values(i)
    if data[1] in dict.keys():
        dict[data[1]] += data[4]
    else:
        dict[data[1]] = data[4]
sum = sum(dict.values())
for i,j in dict.items():
    print("%s的月销售占比为%s"%(i,format(j/sum,'.1%')))
'''
# 每件衣服的销售额占比
'''
table_two = wb.sheet_by_name("2月")
dict = {}
for i in range(1,table_two.nrows):
    data = table_two.row_values(i)
    if data[1] in dict.keys():
        dict[data[1]] += data[4]*data[2]
    else:
        dict[data[1]] = data[4]*data[2]
sum = sum(dict.values())
for i,j in dict.items():
    print("%s的销售额占比为%s"%(i,format(j/sum,'.1%')))
'''
# 全年销量最低的衣服
'''
names = wb.sheet_names();
dict = {}
for i in names:
    table = wb.sheet_by_name(i)
    for j in range(1,table.nrows):
        data = table.row_values(j)
        if data[1] in dict.keys():
            dict[data[1]] += data[4]
        else:
            dict[data[1]] = data[4]
for a,b in dict.items():
    if b == min(dict.values()):
        print("本年销售最低的衣服是%s，销量为%s件"%(a,b))
'''