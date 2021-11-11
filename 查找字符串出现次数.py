
count = 0
strnum = '10.155.24.132'
try:
    f = open(file='baidu_x_system.log',mode='r+',encoding='utf-8')
    da = f.readlines()
    for line in da:
        if strnum in line:
            count += 1
        else:
            pass
    print(strnum,"出现的次数为：",count)
except Exception:
    print("没有该字段")
finally:
    print("走你")
