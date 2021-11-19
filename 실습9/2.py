class PriorityQueue:
    def __init__(self):
        self.items = []
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def enqueue(self, item):
        self.items.append(item)
        self.count += 1
        self.moveUp(0, self.count - 1)

    def moveUp(self, first, last):
        while last > first:
            parent = (last - 1) // 2
            if self.items[parent] < self.items[last]:
                self.swap(parent, last)
                last = parent
            else:
                break

    def swap(self, x, y):
        self.items[x], self.items[y] = self.items[y], self.items[x]

    def dequeue(self):
        if not self.isEmpty():
            item = self.items[0]
            self.count -= 1
            self.items[0] = self.items[self.count]
            self.moveDown(0, self.count - 1)
            self.items.pop(-1)
            return item

    def moveDown(self, first, last):
        leftChild = 2 * first + 1
        while leftChild <= last:
            if leftChild == last:
                maxChild = leftChild
            else:
                rightChild = 2 * first + 2
                if self.items[leftChild] <= self.items[rightChild]:
                    maxChild = rightChild
                else:
                    maxChild = leftChild
            if self.items[first] < self.items[maxChild]:
                self.swap(first, maxChild)
                first = maxChild
                leftChild = 2 * first + 1
            else:
                break

    def print(self):
        a = self.items.sort(reverse=True)
        for i in a:
            print(i, end=" ")
        print()
    #
    # def display(self):
    #
    # def sort(self):


def main():
    pq = PriorityQueue()
    print("Enter a command: e(enqueue), d(dequeue), empty, s(size)")
    print("p(print), pp(pretty print), sort, or q(quit)")
    while True:
        print("> ", end="")
        line = input().split()
        command = line[0]
        if command == 'e':
            item = line[1]
            pq.enqueue(item)
        elif command == 'd':
            print(pq.dequeue())
        elif command == 'empty':
            print(pq.isEmpty())
        elif command == 'p':
            pq.print()
        elif command == 'pp':
            pq.display()
        elif command == 's':
            print(f"size: {pq.size()}")
        elif command == 'sort':
            print(pq.sort())
        elif command == 'q':
            break


main()
