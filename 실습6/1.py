class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def size(self):
        node = self.top
        count = 0
        while node is not None:
            node = node.next
            count += 1
        return count

    def clear(self):
        self.top = None

    def push(self, item):
        n = Node(item, self.top)
        self.top = n

    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.next
            return n.item

    def peek(self):
        if not self.isEmpty():
            return self.top.item

    def print(self):
        node = self.top
        while node is not None:
            print(node.item, end=" ")
            node = node.next
        print()


def main():
    stack = LinkedStack()
    print("Enter a command: pop, push, peek, size, empty, p(rint), m(atch), q(uit)")
    while True:
        print("> ", end="")
        line = input().split()
        command = line[0]
        if command == 'push':
            item = line[1]
            stack.push(item)
        elif command == 'pop':
            print(stack.pop())
        elif command == 'peek':
            print(stack.peek())
        elif command == 'empty':
            print(stack.isEmpty())
        elif command == 'size':
            print(stack.size())
        elif command == 'p':
            stack.print()
        elif command == 'q':
            break


main()
