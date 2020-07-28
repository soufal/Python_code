class Person(object):
    """定义一个父类Person人"""

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
        print("%s正在愉快的玩耍。" % self._name)

    def watch_tv(self):
        if self._age >= 18:
            print("%s正在观看爱情片。" % self._name)
        else:
            print("%s只能观看动画片。" % self._name)

class Student(Person):
    """定义一个学生类，继承自Person"""

    def __init__(self, name, age, grade):
        """
        super()执行父类的构造函数，使得我们能够调用父类的属性。
        """
        # 使用super()继承父类的属性
        super().__init__(name, age)
        # 定义子类自己的属性
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print("%s的%s正在学习%s。" % (self._grade, self._name, course))

class Teacher(Person):
    """定义一个Teacher类，继承自Person"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print("%s%s正在讲%s。" % (self.name, self.title, course))

def main():
    stu = Student("吴吴吴", 26, "大学")
    stu.study("python")
    stu.watch_tv()
    t = Teacher("张张张", 24, "专家")
    t.teach('python')
    t.watch_tv()

if __name__ == '__main__':
    main()