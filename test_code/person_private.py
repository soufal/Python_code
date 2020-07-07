class Person(object):
    """
    @property装饰器
    包装getter和setter方法，使得对属性的访问既安全又方便。

    @__slots__: 限定自定义类型的对象只能绑定某些属性。
    """

    # 限定Person对象只能绑定_name, _age和_gender对象
    __slots__ = ('_name', '_age', '_gender')
    def __init__(self, name, age):
        self._name = name
        self._age = age


    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @name.setter
    def name(self, name):
        self._name = name

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

def main():
    person = Person("soufal", 26)
    print(person.age)
    person.age = 11
    print(person.age)

    print(person.name)
    person.name = 'jk'
    print(person.name)
    person._gender = '女'
    print(person._gender)


class Person_one(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    # 使用__slots__装饰器
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main_one():
    person = Person_one('王大锤', 22)
    person.play()
    person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True
    # print(person._is_gay)


if __name__ == '__main__':
    main_one()
