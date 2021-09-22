# coding=utf-8
class Date:
    def __init__(self, year, month, day, n):
        self.year = year
        self.month = month
        self.day = day
        self.n = n

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

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}\t "


def main():
    inFile = open("input2.txt")
    lst = []
    while True:
        line = inFile.readline()
        if line == "":
            break
        date = [int(i) for i in line.split()]
        lst.append(Date(date[0], date[1], date[2], date[3]))
    for i in range(len(lst)):
        print(lst[i], lst[i].n, "일 후\t", "==>\t", end="")
        print(lst[i].incrementN())

    inFile.close()


main()
