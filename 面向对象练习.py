
'''
高度，容积，颜色，材质
能存放液体

'''
#任务一：
# 分析一个水杯的属性和功能，使用类描述并创建对象
# 高度，容积，颜色，材质
# 能存放液体
class water_Cup:
    __height = "18"
    __vmm = 0
    __color = "pink"
    __material = "玻璃"
    def save_water(self):
        print(self.__height)

cup = water_Cup()
cup.__height = 'dsjifds'
print(cup.save_water())
VM = cup.save_water()
print(cup.vmm)


#任务二：
# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
class computer:
    size = ""
    price = ""
    cputype = "i5"
    cashsize = "128G"
    servicestart = "12h"
    def type(self):
        print(self.cputype,"型号的笔记本可以打字")

    def game(self):
        print(self.cputype, "型号的笔记本可以玩王者游戏")
    def video(self):
        print(self.cputype,"型号的笔记本可以看好多电视剧")
    def getsize(self):
        return self.size
    def setsize(self,size):
        self.size = size

    def getprice(self):
        return self.price
    def setprice(self,price):
        self.price = price

com = computer()
com.setsize("14")
com.setprice("5000")
p = com.getprice()
s = com.getsize()
com.type()
com.game()
com.video()
print(s,p)




















