class Student:
    def __init__(self, number, name, score):
        self.number = number
        self.name = name
        self.score = score

    def __str__(self):
        return f"[{self.number}, {self.name}, {self.score}]"


class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ":" + str(self.value)


class HashTable:
    def __init__(self, size):
        self.table = [None] * size
        self.tableSize = size

    def hash(self, key):
        sum = 0
        for ch in str(key):
            sum += ord(ch)
        return sum % self.tableSize

    def insert(self, key, value):
        idx = self.hash(key)
        if self.table[idx] is not None:
            entry = Entry(key, value)
            node = Node(entry)
            node.next = self.table[idx]
            self.table[idx] = node
        else:
            self.table[idx] = Node(Entry(key, value))

    def search(self, key):
        search_idx = self.hash(key)
        if self.table[search_idx] is None:
            return None
        elif self.table[search_idx].item.key == key:
            return self.table[search_idx]
        else:
            next = self.table[search_idx].next
            while next is not None:
                if next.item.key == key:
                    return next
                else:
                    next = next.next
            return None

    def delete(self, key):
        search_idx = self.hash(key)
        if self.table[search_idx] is None:
            return False
        elif self.table[search_idx].item.key == key:
            if self.table[search_idx].next is not None:
                self.table[search_idx] = self.table[search_idx].next
            else:
                self.table[search_idx] = None        
        else:
            now = self.table[search_idx]
            while now.next is not None:
                if now.next.item.key == key:
                    now.next = None
                elif now.next is not None:
                    now = now.next
                else:
                    return False

    def print(self):
        for i in range(self.tableSize):
            if self.table[i] is None:
                print(f"[{i}]")
                continue
            else:
                node = self.table[i]
                print(f"[{i}]\t{node.item}")
                while node.next is not None:
                    node = node.next
                    print(f"\t{node.item}")


def main():
    inFile = open(
        "/Users/bang/Documents/project/자료구조/실습8/student.txt", "r")
    ht = HashTable(5)
    while True:
        line = inFile.readline()
        if line == '':
            break
        lst = line.split()
        s = Student(int(lst[0]), lst[1], float(lst[2]))
        ht.insert(lst[0], s)
    ht.print()
    print("Enter a command: i(nsert), d(elete), s(earch), p(rint), or q(uit)")
    while True:
        command = input("> ")
        if command == 'i':
            print("Enter student number, name, score: ", end="")
            line = input().split()
            s = Student(int(line[0]), line[1], float(line[2]))
            ht.insert(line[0], s)
        elif command == "d":
            print("Enter student number: ", end="")
            number = input()
            if ht.delete(number) == False:
                print(str(number) + " not found")
            else:
                print(str(number) + " deleted")
        elif command == "s":
            print("Enter student number: ", end="")
            number = input()
            s = ht.search(number)
            if s is not None:
                print(s.item.value)
            else:
                print(str(number) + " not found")
        elif command == 'p':
            ht.print()
        elif command == 'q':
            break


main()
