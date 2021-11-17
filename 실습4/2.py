class Stack:
    def __init__(self):
        self.top = []

    def push(self, item):
        self.top.insert(0, item)
    
    def clear(self):
        self.top = []

    def __str__(self):
        return f"{self.top}"


def main():
    s = Stack()

    while True:
        n = int(input("Enter a decimal number: "))
        if n == -1:
            break
        number = n
        while True:
            rest = number % 2
            s.push(rest)
            number = int(number / 2)
            if number == 1:
                s.push(number)
                break
        binary = "".join(map(str, s.top))
        print(f"{n} ==> {binary}")
        s.clear()


main()
