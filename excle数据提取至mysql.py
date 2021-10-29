
import xlrd
from DBUtils import *

# 打开excle
wb = xlrd.open_workbook(filename=r"C:\Users\高志远\Desktop\python\day7\任务\2020年每个月的销售情况.xlsx",encoding_override=True)

# 所有工作簿
names = wb.sheet_names();

# 循环工作簿
for i in names:
    # 获取工作簿
    table = wb.sheet_by_name(i)

    # 获取有效行数
    nrows = table.nrows

    # 循环行数从1开始
    for j in range(1,nrows):

        # 获取到第五列为止，以列表形式返回
        data = table.row_values(j,end_colx=5)

        # 添加数据到数据库
        sql = "insert into clothes value(%s,%s,%s,%s,%s,%s)"
        param = [data[0],data[1],float(data[2]),int(data[3]),int(data[4]),i]
        updata(sql,param)










