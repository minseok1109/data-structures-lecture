class Node:
    def __init__(self, it, nt=None):
        self.item = it
        self.next = nt


class UnsortedLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.next
            count += 1
        return count

    def clear(self):
        self.head = None

    def insertFirst(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def insertLast(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = Node(data)

    def remove(self, data):
        if self.isEmpty():
            raise Exception("List is empty")
        prev = None
        curr = self.head
        while curr is not None:
            if curr.item == data:
                break
            prev = curr
            curr = curr.next
        if curr is None:
            return False
        elif prev is None:
            self.head = self.head.next
        else:
            prev.next = curr.next
        return True

    def find(self, data):
        if self.isEmpty():
            raise Exception("List is empty")
        node = self.head
        while node is not None:
            if node.item == data:
                return node
            node = node.next
        return node

    def print(self):
        node = self.head
        while node is not None:
            print(node.item, end=" ")
            node = node.next
        print()


def main():
    lst = UnsortedLinkedList()
    print("Enter a command: inf(insertFirst), inl(insertLast), e(mpty), c(lear)")
    print("r(emove), f(ind), p(rint): ")
    while True:
        print('> ', end="")
        line = input().split()
        command = line[0]
        if command == 'inf':
            lst.insertFirst(line[1])
        elif command == 'inl':
            lst.insertLast(line[1])
        elif command == 'e':
            print(lst.isEmpty())
        elif command == 'c':
            lst.clear()
        elif command == 'p':
            lst.print()
        elif command == 's':
            print(lst.size())
        elif command == 'r':
            elem = line[1]
            try:
                if lst.remove(elem):
                    print(elem, "removed")
                else:
                    print("No such element")
            except Exception as e:
                print(e)
        elif command == 'f':
            elem = line[1]
            try:
                if lst.find(elem):
                    print(elem, "found")
                else:
                    print("No such element")
            except Exception as e:
                print(e)
        elif command == 'q':
            break


main()
