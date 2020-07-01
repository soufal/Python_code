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


if __name__ == '__main__':
    main()
