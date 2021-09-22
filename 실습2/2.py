class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

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

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"


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
    inFile = open("input.txt", "r")
    lst = []
    while True:
        line = inFile.readline()
        if line == "":
            break
        date = [int(i) for i in line.split()]

        lst.append(Date(date[0], date[1], date[2]))
    for i in range(len(lst)):
        print(lst[i])
    min_, max_ = find_min_max(lst)
    print("earlist date", min_)
    print("latest date", max_)
    inFile.close()


main()
