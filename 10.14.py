'''

Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条
任务：打折：随机获得优惠券（9折10，5折5，1折2，面单1.
            单个商品打折9折10，5折5，1折2，面单1）

'''
import random
# 商品列表
# 名称 价格
goods = [
         ['可乐',3],
         ['冰红茶',3],
         ['口香糖',10],
         ['水杯',50],
         ['全部商品']
         ]
pre = [['九折',0.9,10],['五折',0.5,5],['一折',0.1,2],['免单',0,1]]
zhe = random.choice(pre)
shang = random.choice(goods)
print(shang[0]+zhe[0],'共有%s张优惠卷'%zhe[2])
shopcart = {}
ran = random.randint(50,100)
reality = ran
print("您的初始可用余额为%s"%ran)
print('商品列表')
for i in range(len(goods)-1):
    print(i,":",goods[i])
print("点击q或Q结算并退出")
while True:
    num = input("请选择商品编号：")
    if num.isdigit():  #数字判断
        num = int(num)
        if num == 4:
            print('请输入正确的编号')
        elif num <len(goods): #编号存在判断
            if ran >= goods[num][1]:   #余额是否能买下商品判断
                # 加入购物车
                if goods[num][0] in shopcart:
                    shopcart[goods[num][0]]+=1  #商品存在购物车，数量加一
                else:
                    shopcart[goods[num][0]] =1 #加入购物车
                # 是否是打折商品
                if shang[0] == goods[num][0]:
                    print(shang[0])
                    # 是否有优惠卷
                    if zhe[2]>1:
                        ran -= goods[num][1]*zhe[1]
                        zhe[2]-=1
                        print("已自动使用%s优惠卷,剩余%s个"%(shang[0],zhe[2]))
                    elif zhe[2] == 1:
                        ran -= goods[num][1] * zhe[1]
                        zhe[2] -= 1
                        print("最后一个优惠卷用完了")
                    else:
                        ran -= goods[num][1]
                else:
                    ran -= goods[num][1]
                print('买了', goods[num][0], '可用余额为', ran)
            else:
                print("钱不够了")
        else:
            print('请输入正确的编号')
    # 退出打印小票
    elif num == 'q' or num == 'Q':
        discount = 0
        print('商品',' ','个数')
        for i,j in shopcart.items():
            print(i," ",j)
        if shang[0] == '全部商品':
            if zhe[0] == '九折':
                discount = (reality-ran)*0.9
            elif zhe[0] == '五折':
                discount = (reality-ran)*0.5
            elif zhe[0] == '一折':
                discount = (reality - ran) * 0.1
            elif zhe[0] == '免单':
                discount = 0
        else:
            discount = reality-ran
        print('实际花费',' ',discount)
        break
    else:
        print('请输入编号')
    print("您的可用余额为%s"%ran)
