# coding=utf-8
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def lastDayOfTheMonth(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
                return 29
            return 28

    def increment(self):
        if self.day == self.lastDayOfTheMonth():
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1
        return self

    def incrementN(self):
        for i in range(self.n):
            self.increment()
        return self

    def countDays(self, other):
        count = 0
        if self > other:
            while other != self:
                other.increment()
                count -= 1
        else:
            while self != other:
                self.increment()
                count += 1
        return count

    def __gt__(self, other):
        return self.year > other.year or self.month > other.month or self.day > other.day

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}\t "


def main():
    inFile = open("input3.txt")
    lst = []
    while True:
        line = inFile.readline()
        if line == "":
            break
        date = [int(i) for i in line.split()]
        lst.append((Date(date[0], date[1], date[2]), Date(date[3], date[4], date[5])))
    for i in range(len(lst)):
        print(lst[i][0], end="")
        print(lst[i][1], end="\t")
        print("==>", end="\t")
        print(f"{lst[i][0].countDays(lst[i][1])}일 경과")


    inFile.close()


main()
