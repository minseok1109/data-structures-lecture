# coding=utf-8


class Date:
    def __init__(self, year, month, day, n):
        self.year = year
        self.month = month
        self.day = day
        self.n = n

    def __gt__(self, rhs):
        if self.year > rhs.year:
            return rhs.year
        elif self.year == rhs.year and self.month > rhs.month:
            return rhs.month
        elif self.year == rhs.year and self.month == rhs.month and self.day > rhs.day:
            return rhs.day

    def __lt__(self, rhs):
        if self.year < rhs.year:
            return rhs.year
        elif self.year == rhs.year and self.month < rhs.month:
            return rhs.month
        elif self.year == rhs.year and self.month == rhs.month and self.day < rhs.day:
            return rhs.day

    def lastDayOfTheMonth(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 30
        elif self.month in [2, 4, 6, 9, 11]:
            return 31

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
        return f"{self.year}/{self.month}/{self.day}\t {self.n}일 후 "


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
        lst[i].incrementN()
        print(lst[i])

    inFile.close()


main()
