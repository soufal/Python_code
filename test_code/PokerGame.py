#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/7/29 10:10
# @Author : soufal
# @File : PokerGame.py
# @Desc : 扑克游戏Demo

import random

class Card(object):
    """
    单张手牌类
    """
    def __init__(self, suit, face):
        """
        初始化方法
        :param suit: 花色
        :param face: 点数
        """
        self._suit = suit
        self._face = face

    @property
    def suit(self):
        return self._suit

    @property
    def face(self):
        return self._face

    def __str__(self):
        """
        格式化输出
        :return: 返回当前牌的花色和点数
        """
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return "%s%s" % (self._suit, face_str)

    def __repr__(self):
        """
        实现自定义类的“自我描述” 功能
        重写 __repr__ 方法
        :return: 自定义类的相关信息
        """
        return self.__str__()

class Poker(object):
    """
    一副牌类
    """
    def __init__(self):
        """
        初始化方法
        """
        self._cards = [Card(suit, face)
                       for suit in '♠♥♣♦'
                       for face in range(1, 14)]
        # 用于标记牌是否发完
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shffle(self):
        """
        洗牌（随机乱序）
        """
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """
        发牌
        :return: 当前发出的牌
        """
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """
        判断牌是否发完
        :return: Ture or False
        """
        return self._current < len(self._cards)

class Player(object):
    """
    玩家类
    """
    def __init__(self, name):
        """
        初始化方法
        :param name: 玩家姓名
        """
        self._name = name
        self._cards_in_hands = []

    @property
    def name(self):
        return self._name

    @property
    def cards_in_hands(self):
        return self._cards_in_hands

    def get_card(self, card):
        """
        摸牌
        :param card: 摸到的牌
        :return:
        """
        self._cards_in_hands.append(card)

    def arrange(self, card_key):
        """
        玩家整理手上的牌
        :param card_key: 排序规则
        :return:
        """
        self._cards_in_hands.sort(key=card_key)


def get_key(card):
    """
    排序规则：先根据花色再根据点数进行排序
    :param card: 待排序的牌
    :return: 排序后的牌
    """
    return (card.suit, card.face)

def main():
    p = Poker()
    p.shffle()
    players = [Player('东'), Player('西'), Player('南'), Player('北')]
    for _ in range(13):
        for player in players:
            player.get_card(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player.cards_in_hands)

if __name__ == '__main__':
    main()