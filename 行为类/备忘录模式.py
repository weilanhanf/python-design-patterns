#!/user/bin/env python
# -*- coding: utf-8 -*-

import random

#以模拟一个战斗角色为例。首先，创建游戏角色
class GameCharacter():
    vitality = 0
    attack = 0
    defense = 0
    def displayState(self):
        print('Current Values:')
        print('Life:%d' % self.vitality)
        print('Attack:%d' % self.attack)
        print('Defence:%d' % self.defense)
    def initState(self,vitality,attack,defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense
    def saveState(self):
        return Memento(self.vitality, self.attack, self.defense)
    def recoverState(self, memento):
        self.vitality = memento.vitality
        self.attack = memento.attack
        self.defense = memento.defense
class FightCharactor(GameCharacter):
    def fight(self):
        self.vitality -= random.randint(1,10)

# GameCharacter定义了基本的生命值、攻击值、防御值以及实现角色状态控制的方法，FightCharactor实现具体的“战斗”接口。
#为实现保存进度的细节，还需要一个备忘录，来保存进度。
class Memento:
    vitality = 0
    attack = 0
    defense = 0
    def __init__(self, vitality, attack, defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense

#业务逻辑中可以进行类的调度了
if __name__=="__main__":
    game_chrctr = FightCharactor()
    game_chrctr.initState(100,79,60)
    game_chrctr.displayState()
    memento = game_chrctr.saveState()
    game_chrctr.fight()
    game_chrctr.displayState()
    game_chrctr.recoverState(memento)
    game_chrctr.displayState()