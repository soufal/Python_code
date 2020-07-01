from time import sleep

class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化时钟属性：
        1、定义时、分、秒。
        2、并且设置默认值。
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """
        时钟走字
        """
        # 秒数增加
        self._second += 1
        # 如果秒加到60，则分增加1,并将秒数重置为0
        if self._second == 60:
            self._second = 0
            self._minute += 1
            # 如果分钟加到60，则时增加1,并将分钟数重置为0
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                # 如果小时数加到24，则将其置为0
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """
        显示时间
        """
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

def main(input_hour, input_minute, input_second):
    clock = Clock(input_hour, input_minute, input_second)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main(23,59,50)
