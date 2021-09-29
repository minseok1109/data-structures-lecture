class Arraylist:
    def __init__(self):
        self.items = []

    def add(self, elem):
        return self.items.append(elem)

    def remove(self, elem):
        if elem in self.items:
            self.items.remove(elem)
            print(f"{elem} removed")
        else:
            print("No such element")

    def insert(self, pos, elem):
        self.items.insert(pos, elem)

    def delete(self, pos):
        self.items.pop(pos)

    def isEmpty(self):
        return print(len(self.items) == 0)

    def getEntry(self, pos):
        return self.items[pos]

    def size(self):
        print(len(self.items))

    def clear(self):
        self.items = []

    def find(self, item):
        print(self.items.index(item))

    def replace(self, pos, elem):
        self.items[pos] = elem

    def sort(self):
        self.items.sort()

    def merge(self, lst):
        self.items.extend(lst)

    def duplicate(self):
        self.items = list(dict.fromkeys(self.items))

    def search(self, elem):
        if elem in self.items:
            print(f"{elem} found")
        else:
            print("No such element")

    def print(self, msg="ArrayList"):
        return print(msg, len(self.items), self.items)


def main():
    array = Arraylist()
    print("Enter a command: i(nsert), d(elete), e(mpty), g(etEntry), c(lear), a(dd), "
          "dup, remove, search, f(ind), r(eplace), s(ort), m(erge), p(rint):")

    while True:
        user_input = input().split(' ')
        if user_input[0] in ['a', 'remove', 'f', 'search']:
            command, elem = user_input
        elif user_input[0] in ['d', 'g', ]:
            command, pos = user_input
        elif len(user_input) == 3:
            command, pos, elem = user_input
        elif len(user_input) == 1:
            command = ''.join(user_input)
        elif len(user_input) > 3:
            command = ''.join(user_input[:1])
            lst = user_input[1:]

        if command == 'q':
            break
        elif command == 'a':
            array.add(elem)
        elif command == 'p':
            array.print()
        elif command == 'remove':
            array.remove(elem)
        elif command == 'i':
            array.insert(int(pos), elem)
        elif command == 'd':
            array.delete(int(pos))
        elif command == 'e':
            array.isEmpty()
        elif command == 'g':
            print(array.getEntry(int(pos)))
        elif command == 's':
            array.sort()
        elif command == 'f':
            array.find(elem)
        elif command == 'r':
            array.replace(int(pos), elem)
        elif command == 'm':
            array.merge(lst)
        elif command == 'c':
            array.clear()
        elif command == 'dup':
            array.duplicate()
        elif command == 'search':
            array.search(elem)


main()
