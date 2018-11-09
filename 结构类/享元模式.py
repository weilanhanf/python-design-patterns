#!/user/bin/env python
# -*- coding: utf-8 -*-


#假设有一个网上咖啡选购平台，客户可以在该平台上下订单订购咖啡，平台会根据用户位置进行线下配送。
# 假设其咖啡对象构造如下：
class Coffee:
    name = ''
    price =0
    def __init__(self,name):
        self.name = name
        self.price = len(name)#在实际业务中，咖啡价格应该是由配置表进行配置，或者调用接口获取等方式得到，此处为说明享元模式，将咖啡价格定为名称长度，只是一种简化
    def show(self):
        print("Coffee Name:%s Price:%s"%(self.name,self.price))

"""
#对应客户顾客类
class Customer:
    name=""
    def __init__(self,name):
        self.name=name
    def order(self,coffee_name):
        print("%s ordered a cup of coffee:%s"%(self.name,coffee_name))
        return Coffee(coffee_name)
"""

"""
按照一般的处理流程，用户在网上预订咖啡，其代表用户的Customer类中生成一个Coffee类，直到交易流程结束。整个流程是没有问题的。
但是在高并发的情况下，也就是说单位时间内购买咖啡的用户越来越多，生成的咖啡实例就会越来越多，系统资源消耗越来越大
避免重复实例的出现，是节约系统资源的一个突破口。引入咖啡工厂类
"""
class CoffeeFactory():
    coffee_dict = {}
    def getCoffee(self, name):
        if self.coffee_dict.__contains__(name) == False:
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]
    def getCoffeeCount(self):
        return len(self.coffee_dict)

# 咖啡工厂中，getCoffeeCount直接返回当前实例个数。重写后的Customer
class Customer:
    coffee_factory=""
    name=""
    def __init__(self,name,coffee_factory):
        self.name=name
        self.coffee_factory=coffee_factory
    def order(self,coffee_name):
        print("%s ordered a cup of coffee:%s"%(self.name,coffee_name))
        return self.coffee_factory.getCoffee(coffee_name)


#假设业务中短时间内有多人订了咖啡，业务模拟如下
if __name__=="__main__":
    coffee_factory=CoffeeFactory()
    customer_1=Customer("A Client",coffee_factory)
    customer_2=Customer("B Client",coffee_factory)
    customer_3=Customer("C Client",coffee_factory)
    c1_capp=customer_1.order("cappuccino")
    c1_capp.show()
    c2_mocha=customer_2.order("mocha")
    c2_mocha.show()
    c3_capp=customer_3.order("cappuccino")
    c3_capp.show()
    print("Num of Coffee Instance:%s"%coffee_factory.getCoffeeCount())
