class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0

    def size(self):
        return len(self.top)

    def clear(self):
        self.top = []

    def push(self, item):
        self.top.insert(0, item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(0)

    def peek(self):
        if not self.isEmpty():
            return self.top[0]

    def __str__(self):
        return f"{self.top}"


def checkBrackcet(line):
    a = Stack()
    for ch in line:
        if ch in "([{":
            a.push(ch)
        elif ch in ")]}":
            if a.isEmpty():
                return False
            else:
                left = a.pop()
                if (ch == ')' and left != '(') or (ch == '}' and left != '{') or (ch == ']' and left != '['):
                    return False
    return a.isEmpty()


def main():
    s = Stack()
    a = Stack()
    print("Enter a command: pop, push, peek, size, empty, p(rint), m(atch), q(uit)")

    while True:
        user_input = input().split(' ')
        if user_input[0] == 'push':
            command, item = user_input
        elif len(user_input) == 1:
            command = "".join(user_input)

        if command == 'pop':
            print(s.pop())
        elif command == 'push':
            s.push(item)
        elif command == 'peek':
            print(s.peek())
        elif command == 'size':
            print(s.size())
        elif command == 'empty':
            print(s.isEmpty())
        elif command == 'p':
            print(s)
        elif command == 'm':
            inFile = open(
                '/Users/bang/Documents/project/자료구조/실습4/input.txt', 'r', encoding="euc-kr")
            lines = inFile.readlines()
            for line in lines:
                if checkBrackcet(line.strip()):
                    print(line, end="")
                    print("matched")
                else:
                    print(line, end="")
                    print("not matched")
            inFile.close()
        elif command == 'q':
            break


main()
