#!/user/bin/env python
# -*- coding: utf-8 -*-

#构造药品类和工作人员类
class Medicine:
    name=""
    price=0.0
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def accept(self,visitor):
        pass
#药品类中有两个子类，抗生素和感冒药
class Antibiotic(Medicine):
    def accept(self,visitor):
        visitor.visit(self)
class Coldrex(Medicine):
    def accept(self,visitor):
        visitor.visit(self)

#工作人员分为划价员和药房管理员
class Visitor:
    name=""
    def setName(self,name):
        self.name=name
    def visit(self,medicine):
        pass
class Charger(Visitor):
    def visit(self,medicine):
        print("CHARGE: %s lists the Medicine %s. Price:%s " % (self.name,medicine.getName(),medicine.getPrice()))
class Pharmacy(Visitor):
    def visit(self,medicine):
        print("PHARMACY:%s offers the Medicine %s. Price:%s" % (self.name,medicine.getName(),medicine.getPrice()))


"""
在药品类中，有一个accept方法，其参数是个visitor；
而工作人员就是从Visitor类中继承而来的，
也就是说，他们就是Visitor，都包含一个visit方法，其参数又恰是medicine。
药品作为处理元素，依次允许（Accept）Visitor对其进行操作，
这就好比是一条流水线上的一个个工人，对产品进行一次次的加工。
整个业务流程还差一步，即药方类的构建（流水线大机器）
"""

class ObjectStructure:
    pass
class Prescription(ObjectStructure):
    medicines=[]
    def addMedicine(self,medicine):
        self.medicines.append(medicine)
    def rmvMedicine(self,medicine):
        self.medicines.append(medicine)
    def visit(self,visitor):
        for medc in self.medicines:
            medc.accept(visitor)
#药方类将待处理药品进行整理，并组织Visitor依次处理。

if __name__=="__main__":
    yinqiao_pill=Coldrex("Yinqiao Pill",2.0)
    penicillin=Antibiotic("Penicillin",3.0)
    doctor_prsrp=Prescription()
    doctor_prsrp.addMedicine(yinqiao_pill)
    doctor_prsrp.addMedicine(penicillin)
    charger=Charger()
    charger.setName("Doctor Strange")
    pharmacy=Pharmacy()
    pharmacy.setName("Doctor Wei")
    doctor_prsrp.visit(charger)
    doctor_prsrp.visit(pharmacy)