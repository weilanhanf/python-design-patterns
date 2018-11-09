#!/user/bin/env python
# -*- coding: utf-8 -*-


class Shape:
    name=""
    param=""
    def __init__(self,*param):
        pass
    def getName(self):
        return self.name
    def getParam(self):
        return self.name,self.param

class Pen:
    shape=""
    type=""
    def __init__(self,shape):
        self.shape=shape
    def draw(self):
        pass


#形状对象和画笔对象是最为抽象的形式。接下来，构造多个形状，如矩形和圆形
class Rectangle(Shape):
    def __init__(self,long,width):
        self.name="Rectangle"
        self.param="Long:%s Width:%s"%(long,width)
        print("Create a rectangle:%s"%self.param)
class Circle(Shape):
    def __init__(self,radius):
        self.name="Circle"
        self.param="Radius:%s"%radius
        print("Create a circle:%s"%self.param)

#紧接着是构造多种画笔，如普通画笔和画刷：
class NormalPen(Pen):
    def __init__(self,shape):
        Pen.__init__(self,shape)
        self.type="Normal Line"
    def draw(self):
        print("DRAWING %s:%s----PARAMS:%s"%(self.type,self.shape.getName(),self.shape.getParam()))
class BrushPen(Pen):
    def __init__(self,shape):
        Pen.__init__(self,shape)
        self.type="Brush Line"
    def draw(self):
        print("DRAWING %s:%s----PARAMS:%s" % (self.type,self.shape.getName(), self.shape.getParam()))

#业务中的逻辑如下：
if __name__=="__main__":
    normal_pen=NormalPen(Rectangle("20cm","10cm"))
    brush_pen=BrushPen(Circle("15cm"))
    normal_pen.draw()
    brush_pen.draw()