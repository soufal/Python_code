from math import sqrt

"""
练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
class Point:
    (x,y): 点再二维平面的坐标。
Move_to:
    直接将点移动到另一个位置的方法。
Move_by:
    移动指定的增量。
Distance:
    计算点到另一个点距离方法。    
"""

class Point(object):

    def __init__(self, x=0, y=0):
        """
        初始化方法，默认点的坐标为（0,0）。
        :param x: 点的x坐标。
        :param y: 点的y坐标。
        """
        self.x = x
        self.y = y

    def Move_to(self, x, y):
        """
        把点移动到新的位置。
        :param x: 移动位置的x坐标，
        :param y: 移动位置的y坐标。
        :return: None
        """
        self.x = x
        self.y = y

    def Move_by(self, dx, dy):
        """
        把点移动到新的位置。
        :param x: 移动位置的x坐标，
        :param y: 移动位置的y坐标。
        :return: None
        """
        self.x += dx
        self.y += dy

    def Distance(self, other_point):
        """
        计算同另一个点的距离。
        :param other_point: 指定计算的点。
        :return: distance:两点之间的距离。
        """
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        """
        格式化输出对象。
        :return: 格式化的对象。
        """
        return '(%s, %s)' % (str(self.x), str(self.y))

def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.Move_by(-1, 2)
    print(p2)
    p2.Move_to(1,1)
    print(p2)
    print(p1.Distance(p2))


if __name__ == '__main__':
    main()
