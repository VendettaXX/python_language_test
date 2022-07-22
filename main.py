# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# python classmethod test
import string
import time



class Base:
    year = 0
    day = 0
    month = 0

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        print(f'year is {year},month is {month},day is {day}')

    def __repr__(self):
        print(f'year is {self.year},month is {self.month},day is {self.day}')

    # Press the green button in the gutter to run the script.


class Derived(Base):
    # def __init__(self, year, month, day):
    #     print(f'this is Derived construction')

    @classmethod
    def get_data(cls, string_data):
        year, month, day = map(int, string_data.split('-'))
        data1 = cls(year, month, day)
        return data1


if __name__ == '__main__':
    d = Derived.get_data("2016-08-01")
    string.ascii_letters()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
