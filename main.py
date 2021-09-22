# coding=utf-8
# class Bag:
#     def __init__(self):
#         self.items = []
#
#     # 구현 해야할 멤버 함수
#     def contains(self, e):
#         return e in self.items
#
#     def insert(self, e):
#         self.items.append(e)
#
#     def remove(self, e):
#         self.items.remove(e)
#
#     def count(self):
#         return len(self.items)
#
#     def __str__(self):
#         return f"가방 속 물건은: {self.items}"
#
#
# myBag = Bag()
# myBag.insert("휴대폰")
# myBag.insert("지갑")
# myBag.insert("손수건")
# myBag.insert('빗')
# myBag.insert('연필')
# print("가방속 물건: ", myBag)
#
# myBag.insert('빗')
# myBag.remove('손수건')
# myBag.insert('자료 구조 책')
# print("가방속 물건: ", myBag)
# print("가방속 물건 갯수: %d" % myBag.count())
# print("가방속 지갑 유무: %s" % myBag.contains('지갑'))
# print("가방속 손수건 유무: %s" % myBag.contains('손수건'))

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
        if self.month in [1, 3, 5, 7, 8, 10 ,12]:
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

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}/"


def find_min_max(lst):
    Min = lst[0]
    Max = lst[0]

    for i in range(1, len(lst)):
        if lst[i] > Max:
            Max = lst[i]
        if lst[i] < Min:
            Min = lst[i]
    return Min, Max


def main():
    inFile = open("실습2/input2.txt", "r")
    lst = []
    while True:
        line = inFile.readline()
        if line == "":
            break
        date = [int(i) for i in line.split()]
        lst.append(Date(date[0], date[1], date[2], date[3]))
    # for i in range(len(lst)):
    #     print(lst[i])
        print(lst[0])
    inFile.close()


main()
