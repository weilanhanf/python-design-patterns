#!/user/bin/env python
# -*- coding: utf-8 -*-

from copy import copy, deepcopy

class simpleLayer:
    """
    　　　设计一个图层对象，用background表示背景的RGBA，简单用content表示内容，除了直接绘画，还可以设置透明度。
　　"""
    background=[0,0,0,0]
    content="blank"
    def getContent(self):
        return self.content
    def getBackground(self):
        return self.background
    def paint(self,painting):
        self.content=painting
    def setParent(self,p):
        self.background[3]=p
    def fillBackground(self,back):
        self.background=back
    def clone(self):
        return copy(self)
    def deep_clone(self):
        return deepcopy(self)


"""
if  __name__=="__main__":
    dog_layer=simpleLayer()
    dog_layer.paint("Dog")
    dog_layer.fillBackground([0,0,255,0])
    print("Background:",dog_layer.getBackground())
    print("Painting:",dog_layer.getContent())
    another_dog_layer=dog_layer.clone()
    # 通过复制（clone）这个动作实现画一只同样的狗
    print("Background:", another_dog_layer.getBackground())
    print("Painting:", another_dog_layer.getContent())
"""

#深浅拷贝

if  __name__=="__main__":
    dog_layer=simpleLayer()
    dog_layer.paint("Dog")
    dog_layer.fillBackground([0,0,255,0])
    print("Original Background:",dog_layer.getBackground())
    print("Original Painting:",dog_layer.getContent())
    #another_dog_layer=dog_layer.clone()
    another_dog_layer=dog_layer.deep_clone()
    another_dog_layer.setParent(128)
    another_dog_layer.paint("Puppy")
    print("Original Background:", dog_layer.getBackground())
    print("Original Painting:", dog_layer.getContent())
    print("Copy Background:", another_dog_layer.getBackground())
    print("Copy Painting:", another_dog_layer.getContent())

# 浅拷贝时，setParent()方法即新对象的构建函数在类another_dog_layer中并没有二次执行
# 而是直接从内存中dog_layer中拷贝过来(用的类dog_layer的)
# 深拷贝时,新对象的所有方法都是二次执行的