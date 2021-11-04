'''
1.蛋挞篮子初始500个蛋挞，最多500个蛋挞，每个蛋挞三元
2.三个厨师同时制作蛋挞，蛋挞篮子满后，休息三秒，工作时间5分钟，工资结算：蛋挞个数*12
3.六个购买者同时购买蛋挞，每人3000元，篮子清空后，休息三秒，购买5分钟或钱花完停止购买
4.统计今日盈利，卖出蛋挞个数，六人共消费，和单独消费情况
'''

from threading import Thread
import time

EggTart = 500
tim = 0

# 一共制作了多少蛋塔
eggcon = 0
# 一共卖出了多少蛋挞
eggcon2 = 0

# 时间类
class Timefive(Thread):

    def run(self) -> None:
        global tim
        while True:
            time.sleep(1)
            tim += 1


# 厨师类
class Cook(Thread):

    username = ""
    count = 0

    def run(self) -> None:

        global EggTart
        global eggcon
        global tim

        while True:
            if tim >= 2000:
                print(f"{self.username}制作了{self.count}个蛋挞，预计收入{self.count*12}元")
                print(f"一共制作了{eggcon}个蛋挞，卖出了{eggcon2}个蛋挞，收益情况为{eggcon2 * 3}，需要支付给蛋挞师父的工资为{eggcon * 12}")
                break

            if EggTart < 500:
                EggTart += 1
                self.count += 1
                eggcon +=1
                print(f"{self.username}制作了1个蛋挞,篮子里还有{EggTart}个蛋挞")
            elif EggTart == 500:
                time.sleep(3)

# 消费者类
class Per(Thread):

    username = ""
    money = 3000
    count = 0

    def run(self) -> None:

        global EggTart
        global eggcon2

        while True:
            if tim >= 2000:
                print(f"{self.username}购买了{self.count}个蛋挞，花费了{3000-self.money}元")
                break
            if EggTart > 0:
                if self.money >= 3:
                    EggTart -= 1
                    self.money -= 3
                    self.count += 1
                    eggcon2 +=1
                    print(f"{self.username}购买了1个蛋挞，花费了3块钱,篮子里还有{EggTart}个蛋挞,还剩{self.money}元")
                else:
                    break
            if EggTart == 0:
                time.sleep(3)


# 创建对象
cook1 = Cook()
cook2 = Cook()
cook3 = Cook()
per1 = Per()
per2 = Per()
per3 = Per()
per4 = Per()
per5 = Per()
per6 = Per()

cook1.username = "厨师长1号"
cook2.username = "厨师长2号"
cook3.username = "厨师长3号"
per1.username = "吃货1号"
per2.username = "吃货2号"
per3.username = "吃货3号"
per4.username = "吃货4号"
per5.username = "吃货5号"
per6.username = "吃货6号"

# 开启线程
cook1.start()
cook2.start()
cook3.start()

per1.start()
per2.start()
per3.start()
per4.start()
per5.start()
per6.start()

ti = Timefive()
ti.start()







