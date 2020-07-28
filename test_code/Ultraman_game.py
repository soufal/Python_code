#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/7/28 10:30
# @Author : soufal
# @File : Ultraman_game.py
# @Desc : 奥特曼打小怪兽游戏

from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):
    """战斗者抽象类"""

    # 通过__slots__来限定对象可以绑定的成员变量
    # _name: 名字
    # _hp：生命值
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        初始化方法
        :param name: 名字
        :param hp: 生命值
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """
        攻击方法(仅作为一个抽象类被继承)
        :param other:被攻击的对象
        :return:
        """
        pass


class Ultraman(Fighter):
    """
    奥特曼类，继承自战斗者
    """

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """
        初始化方法
        :param name: 名字
        :param hp:  生命值
        :param mp: 魔法值
        """

        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        """
        普通攻击，随机攻击被攻击者15~25的生命值
        :param other: 被攻击者
        :return: null
        """
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """
        终极必杀技（攻击攻击者至少50点或四分之三的血）。并消耗一定的魔法值。
        :param other: 被攻击者
        :return: 攻击成功返回True，否则进行普通攻击并返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """
        魔法攻击
        :param others: 被攻击的群体
        :return: 使用魔法攻击成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """
        恢复魔法值
        :return: 恢复的魔法值
        """
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return ('~~~%s奥特曼~~~\n' % self._name) + ('生命值：%d\n' % self._hp) + ('魔法值：%d\n' % self._mp)

class Monster(Fighter):
    """
    小怪兽
    """
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值：%d\n' % self._hp


def is_any_alive(monsters):
    """
    判断是否还存在存活的小怪兽
    :param monsters: 所有的怪兽
    :return: 存在返回True，否则返回False
    """
    for monster in monsters:
        if monster.alive > 0:
            return True
        else:
            return False

def select_alive_one(monsters):
    """
    选择一只活着的小怪兽
    :param monster: 选择的怪兽名
    :return: 返回所选怪兽
    """
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    """
    显示奥特曼和小怪兽的信息
    :param ultraman: 奥特曼
    :param monsters: 小怪兽
    :return: 奥特曼和小怪兽的信息
    """
    print(ultraman)
    for monster in monsters:
        print(monster, end=" ")

def main():
    u = Ultraman("奥特曼", 1000, 120)
    m1 = Monster('特斯拉', 250)
    m2 = Monster('哥斯拉', 500)
    m3 = Monster('狄仁杰', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print("==========第%02d回合==========" % fight_round)
        m = select_alive_one(ms)    # 选中其中一只小怪兽进行战斗
        skill = randint(1, 10)      # 通过随机数选择使用哪种技能
        if skill <= 6:      # 60%的概率使用普通攻击
            print("%s使用普通攻击打了%s。" % (u.name, m.name))
            u.attack(m)
            print("%s的魔法值恢复了%d点。" % (u.name, u.resume()))
        elif skill <= 9:    # 30%的概率使用魔法攻击（可能会因魔法值不足而失败）
            if u.magic_attack(ms):
                print("%s使用魔法攻击。" % u.name)
            else:
                print("%s使用魔法失败。" % u.name)
        else: # 10%的概率使用了终极必杀技（如果魔法值不足则使用普通攻击）
            if u.huge_attack(m):
                print("%s使用终极必杀技打了%s。" % (u.name, m.name))
            else:
                print("%s使用普通攻击打了%s。" % (u.name, m.name))
                u.attack(m)
                print("%s的魔法值恢复了%d点。" % (u.name, u.resume()))
        if m.alive > 0:     # 如果有小怪兽没有死，则反打奥特曼
            print("%s回击了%s。" % (m.name, u.name))
            m.attack(u)

        display_info(u, ms)     # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print("\n=============战斗结束！=============\n")
    if u.alive > 0:
        print("%s奥特曼胜利！" % u.name)
    else:
        print("小怪兽胜利！")

if __name__ == '__main__':
    main()
