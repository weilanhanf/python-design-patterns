#!/user/bin/env python
# -*- coding: utf-8 -*-


# class MyIter(object):
#     def __init__(self, n):
#         self.index = 0
#         self.n = n
#     def __iter__(self):
#         # return self.n
#         return MyIter(self.n)
#
#     def __next__(self):
#         if self.index < self.n:
#             value = self.index**2
#             self.index += 1
#             return value
#         else:
#             raise StopIteration()
#
# if __name__=="__main__":
#     x_square=MyIter(10)
#
#     # for x in x_square:
#     #     print(x)
#
#     for x in x_square:
#         print(x)


#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
大话设计模式
设计模式——迭代器模式
迭代器模式(Iterator Pattern):提供方法顺序访问一个聚合对象中各元素，而又不暴露该对象的内部表示.
"""
#迭代器抽象类
class Iterator(object):
    def First(self):
        pass

    def Next(self):
        pass

    def Isdone(self):
        pass

    def CurrItem(self):
        pass

#聚集抽象类
class Aggregate(object):

    def CreateIterator(self):
        pass

#具体迭代器类
class ConcreteIterator(Iterator):

    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.curr = 0

    def First(self):
        return self.aggregate[0]

    def Next(self):
        ret = None
        self.curr += 1
        if self.curr < len(self.aggregate):
            ret = self.aggregate[self.curr]
        return ret

    def Isdone(self):
        return True if self.curr+1 >= len(self.aggregate) else False

    def CurrItem(self):
        return self.aggregate[self.curr]

#具体聚集类
class ConcreteAggregate(Aggregate):

    def __init__(self):
        self.ilist = []

    def CreateIterator(self):
        return ConcreteIterator(self)

class ConcreteIteratorDesc(Iterator):
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.curr = len(aggregate)-1

    def First(self):
        return self.aggregate[-1]

    def Next(self):
        ret = None
        self.curr -= 1
        if self.curr >= 0:
            ret = self.aggregate[self.curr]
        return ret

    def Isdone(self):
        return True if self.curr-1<0 else False

    def CurrItem(self):
        return self.aggregate[self.curr]

if __name__=="__main__":
    ca = ConcreteAggregate()
    ca.ilist.append("大鸟")
    ca.ilist.append("小菜")
    ca.ilist.append("老外")
    ca.ilist.append("小偷")

    itor = ConcreteIterator(ca.ilist)
    print(itor.First())
    while not itor.Isdone():
        print(itor.Next())
    print("————倒序————")
    itordesc = ConcreteIteratorDesc(ca.ilist)
    print(itordesc.First())
    while not itordesc.Isdone():
        print(itordesc.Next())