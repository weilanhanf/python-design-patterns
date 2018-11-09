#!/user/bin/env python
# -*- coding: utf-8 -*-
# 路由系统；著名的MVC框架中，其中的C（Controller）就是M（Model）和V（View）的中介者。

#构造三个子系统，即三个类（在中介者模式中，这些类叫做同事类）
class colleague():
    mediator = None
    def __init__(self,mediator):
        self.mediator = mediator
class purchaseColleague(colleague):
    def buyStuff(self,num):
        print("PURCHASE:Bought %s"%num)
        self.mediator.execute("buy",num)
    def getNotice(self,content):
        print("PURCHASE:Get Notice--%s"%content)
class warehouseColleague(colleague):
    total=0
    threshold=100
    def setThreshold(self,threshold):#设置阈值
        self.threshold=threshold
    def isEnough(self):
        if self.total<self.threshold:
            print("WAREHOUSE:Warning...Stock is low... ")
            self.mediator.execute("warning",self.total)
            return False
        else:
            return True
    def inc(self,num):
        self.total+=num
        print("WAREHOUSE:Increase %s"%num)
        self.mediator.execute("increase",num)
        self.isEnough()
    def dec(self,num):
        if num>self.total:
            print("WAREHOUSE:Error...Stock is not enough")
        else:
            self.total-=num
            print("WAREHOUSE:Decrease %s"%num)
            self.mediator.execute("decrease",num)
        self.isEnough()
class salesColleague(colleague):
    def sellStuff(self,num):
        print("SALES:Sell %s"%num)
        self.mediator.execute("sell",num)
    def getNotice(self, content):
        print("SALES:Get Notice--%s" % content)

#当各个类在初始时都会指定一个中介者，而各个类在有变动时，也会通知中介者，由中介者协调各个类的操作。
#中介者实现
class abstractMediator():
    purchase=""
    sales=""
    warehouse=""
    def setPurchase(self,purchase):
        self.purchase=purchase
    def setWarehouse(self,warehouse):
        self.warehouse=warehouse
    def setSales(self,sales):
        self.sales=sales
    def execute(self,content,num):
        pass
class stockMediator(abstractMediator):
    def execute(self,content,num):
        print("MEDIATOR:Get Info--%s"%content)
        if  content=="buy":
            self.warehouse.inc(num)
            self.sales.getNotice("Bought %s"%num)
        elif content=="increase":
            self.sales.getNotice("Inc %s"%num)
            self.purchase.getNotice("Inc %s"%num)
        elif content=="decrease":
            self.sales.getNotice("Dec %s"%num)
            self.purchase.getNotice("Dec %s"%num)
        elif content=="warning":
            self.sales.getNotice("Stock is low.%s Left."%num)
            self.purchase.getNotice("Stock is low. Please Buy More!!! %s Left"%num)
        elif content=="sell":
            self.warehouse.dec(num)
            self.purchase.getNotice("Sold %s"%num)
        else:
            pass

#中介者模式中的execute是最重要的方法，它根据同事类传递的信息，直接协调各个同事的工作。
#在场景类中，设置仓储阈值为200，先采购300，再卖出120，实现如下
if  __name__=="__main__":
    mobile_mediator=stockMediator()#先配置
    mobile_purchase=purchaseColleague(mobile_mediator)
    mobile_warehouse=warehouseColleague(mobile_mediator)
    mobile_sales=salesColleague(mobile_mediator)
    mobile_mediator.setPurchase(mobile_purchase)
    mobile_mediator.setWarehouse(mobile_warehouse)
    mobile_mediator.setSales(mobile_sales)

    mobile_warehouse.setThreshold(200)
    mobile_purchase.buyStuff(300)
    mobile_sales.sellStuff(120)