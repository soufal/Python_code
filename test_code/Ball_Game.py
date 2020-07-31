#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/7/31 16:18
# @Author : soufal
# @File : Ball_Game.py
# @Desc : 使用pygame实现“大球吃小球”游戏

from enum import Enum, unique
from math import sort
from random import randint

import pygame


@unique
class Color(Enum):
    """
    颜色
    """

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """
        获得随机颜色
        """
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

class Ball(object):
    """
    球类
    """

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """
        初始化方法
        :param x:
        :param y:
        :param radius:
        :param sx:
        :param sy:
        :param color:
        """

def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800,600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 定义变量来表示小球在屏幕上的位置
    x, y =50, 50
    running = True
    # 开启一个事件循环处理发生的时间
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # 设置窗口的背景色（颜色是由红绿蓝三原色构成的元组）
        screen.fill((242, 242, 242))
        # 绘制一个圆（参数分别是：屏幕，颜色，圆心位置，半径，0表示填充圆）
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)

        # # 通过指定的文件名加载图像
        # ball_image = pygame.image.load('./')
        # # 在窗口上渲染图像
        # screen.blit(ball_image, (50,50))

        # 刷新当前窗口（渲染窗口将绘制的图像呈现出来）
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()