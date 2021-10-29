import pymysql

host = "localhost"
root = "root"
password = "root"
database = "company"



# 增删改
def updata(sql,param):
    # 连接数据库
    con = pymysql.connect(host=host, user=root, password=password, database=database)
    # 打开控制台
    cursor = con.cursor()
    # 执行
    cursor.execute(sql,param)
    # 提交
    con.commit()
    # 关闭
    cursor.close()
    con.close()
# 查询
def select(sql,param,mode="all",size=1):
    # 连接数据库
    con = pymysql.connect(host=host, user=root, password=password, database=database)
    # 打开控制台
    cursor = con.cursor()
    # 执行
    cursor.execute(sql, param)
    #提取数据
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    # 提交
    con.commit()
    # 关闭
    cursor.close()
    con.close()





