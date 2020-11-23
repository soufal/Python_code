#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/8/7 16:53
# @Author : soufal
# @File : prime_file.py
# @Desc : 判断1-9999之间的素数，并写入文件

from math import sqrt


def is_prime(n):
    """
    判断是否为素数函数
    :param n: 待判断的数字
    :return: 返回是否为素数
    """
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames
if __name__ == '__main__':
    main()
