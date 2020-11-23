#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/8/6 17:18
# @Author : soufal
# @File : file_operate.py
# @Desc : 文件加异常

import time

def main():
    f = None
    try:
        f = open('test.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('文件不存在，无法打开！')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
    finally:
        # 总是执行代码块，适合用于释放外部资源
        if f:
            f.close()

    # 使用with关键字来指定文件对象的上下文环境
    # 并在离开上下文环境时自动释放文件资源
    try:
        with open('test.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('文件不存在，无法打开！')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')

    # 使用for-in循环逐行读取
    with open('test.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('test.txt', mode='r', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)
if __name__ == '__main__':
    main()


