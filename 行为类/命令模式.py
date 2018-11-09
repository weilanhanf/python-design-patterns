#!/user/bin/env python
# -*- coding: utf-8 -*-

#主食子系统，凉菜子系统，热菜子系统,后台三个子系统
class backSys():
    def cook(self,dish):
        pass
class mainFoodSys(backSys):
    def cook(self,dish):
        print("MAINFOOD:Cook %s"%dish)
class coolDishSys(backSys):
    def cook(self,dish):
        print("COOLDISH:Cook %s"%dish)
class hotDishSys(backSys):
    def cook(self,dish):
        print("HOTDISH:Cook %s"%dish)

#前台服务员系统与后台系统的交互，我们可以通过命令的模式来实现，
#服务员将顾客的点单内容封装成命令，直接对后台下达命令，后台完成命令要求的事，

#前台系统构建如下
class waiterSys():
    menu_map=dict()
    commandList=[]
    def setOrder(self,command):
        print("WAITER:Add dish")
        self.commandList.append(command)

    def cancelOrder(self,command):
        print("WAITER:Cancel order...")
        self.commandList.remove(command)

    def notify(self):
        print("WAITER:Notify...")
        for command in self.commandList:
            command.execute()

#前台系统中的notify接口直接调用命令中的execute接口，执行命令。命令类构建
class Command():
    receiver = None
    def __init__(self, receiver):
        self.receiver = receiver
    def execute(self):
        pass
class foodCommand(Command):
    dish=""
    def __init__(self,receiver,dish):
        self.receiver=receiver
        self.dish=dish
    def execute(self):
        self.receiver.cook(self.dish)

class mainFoodCommand(foodCommand):
    pass
class coolDishCommand(foodCommand):
    pass
class hotDishCommand(foodCommand):
    pass

"""
Command类是个比较通过的类，foodCommand类是本例中涉及的类，相比于Command类进行了一定的改造。
由于后台系统中的执行函数都是cook，因而在foodCommand类中直接将execute接口实现，
如果后台系统执行函数不同，需要在三个子命令系统中实现execute接口。
这样，后台三个命令类就可以直接继承，不用进行修改了。
"""


#菜单类辅助业务
class menuAll:
    menu_map=dict()
    def loadMenu(self):#加载菜单，这里直接写死
        self.menu_map["hot"] = ["Yu-Shiang Shredded Pork", "Sauteed Tofu, Home Style", "Sauteed Snow Peas"]
        self.menu_map["cool"] = ["Cucumber", "Preserved egg"]
        self.menu_map["main"] = ["Rice", "Pie"]
    def isHot(self,dish):
        if dish in self.menu_map["hot"]:
            return True
        return False
    def isCool(self,dish):
        if dish in self.menu_map["cool"]:
            return True
        return False
    def isMain(self,dish):
        if dish in self.menu_map["main"]:
            return True
        return False

#业务场景
if  __name__=="__main__":
    dish_list=["Yu-Shiang Shredded Pork","Sauteed Tofu, Home Style","Cucumber","Rice"]#顾客点的菜
    waiter_sys=waiterSys()
    main_food_sys=mainFoodSys()
    cool_dish_sys=coolDishSys()
    hot_dish_sys=hotDishSys()
    menu=menuAll()
    menu.loadMenu()
    for dish in dish_list:
        if menu.isCool(dish):
            cmd=coolDishCommand(cool_dish_sys,dish)
        elif menu.isHot(dish):
            cmd=hotDishCommand(hot_dish_sys,dish)
        elif menu.isMain(dish):
            cmd=mainFoodCommand(main_food_sys,dish)
        else:
            continue
        waiter_sys.setOrder(cmd)
    waiter_sys.notify()

