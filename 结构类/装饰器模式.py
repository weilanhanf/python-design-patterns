#!/user/bin/env python
# -*- coding: utf-8 -*-


#又提到了那个快餐点餐系统，不过今天我们只以其中的一个类作为主角：饮料类。首先，回忆下饮料类：
class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name

class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0

class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0

#除了基本配置，快餐店卖可乐时，可以选择加冰，如果加冰的话，要在原价上加0.3元；
# 卖牛奶时，可以选择加糖，如果加糖的话，要原价上加0.5元。怎么解决这样的问题？
# 可以选择装饰器模式来解决这一类的问题。首先，定义装饰器类：
class drinkDecorator():
    def getName(self):
        pass
    def getPrice(self):
        pass

class iceDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    def getName(self):
        return self.beverage.getName() + " +ice"
    def getPrice(self):
        return self.beverage.getPrice() + 0.3

class sugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    def getName(self):
        return self.beverage.getName() + " +sugar"
    def getPrice(self):
        return self.beverage.getPrice() + 0.5

#构建好装饰器后，在具体的业务场景中，就可以与饮料类进行关联。以可乐+冰为例，示例业务场景如下：
if  __name__=="__main__":
    coke_cola=coke()
    print("Name:%s"%coke_cola.getName())
    print("Price:%s"%coke_cola.getPrice())
    ice_coke=iceDecorator(coke_cola)
    print("Name:%s" % ice_coke.getName())
    print("Price:%s" % ice_coke.getPrice())

