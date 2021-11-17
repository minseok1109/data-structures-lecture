MAX_SIZE = 3


class CircularQueue:
    def __init__(self):
        self.items = [None] * MAX_SIZE
        self.front = 0
        self.rear = 0
        self.count = 0
        self.max_size = MAX_SIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear+1) % self.max_size

    def clear(self):
        self.front = 0
        self.rear = 0
        self.count = 0
        self.max_size = MAX_SIZE

    def enqueue(self, item):
        if self.isFull():
            self.resize()

        self.rear = (self.rear+1) % self.max_size
        self.items[self.rear] = item
        self.count += 1

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.max_size
            self.count -= 1
            return self.items[self.front]

    def resize(self):
        newItems = [None] * 2 * self.max_size
        scan = (self.front+1) % self.max_size
        for i in range(self.count):
            newItems[i+1] = self.items[scan]
            scan = (scan + 1) % self.max_size

        self.items = newItems
        self.front = 0
        self.rear = self.count
        self.max_size = 2 * self.max_size

    def resize2(self):
        newItems = [None] * 2 * self.max_size
        scan = (self.front) % self.max_size
        for i in range(self.count):
            newItems[i+2] = self.items[scan]
            scan = (scan + 1) % self.max_size

        self.items = newItems
        self.front = 0
        self.rear = self.count
        self.max_size = 2 * self.max_size

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % self.max_size]

    def size(self):
        return self.count

    def print(self):
        temp = []
        if self.rear > self.front:
            temp = self.items[self.front + 1: self.rear+1]
        # elif self.count > self.rear:
        #     temp = self.items[self.front + 1: self.count+1]
        else:
            temp = self.items[self.front+1:MAX_SIZE] + \
                self.items[0:self.rear+1]
        return f"{temp}"


class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

    def addFront(self, item):
        # if self.isFull():
        #     self.resize()
        if self.items[0] != None:
            self.resize2()
            self.items[self.front+1] = item
            self.front = (self.front + MAX_SIZE) % MAX_SIZE
            self.count += 1
            self.rear = self.count
        else:
            self.items[self.front] = item
            self.front = (self.front + MAX_SIZE) % MAX_SIZE
            self.count += 1
            self.rear = self.count

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear - 1
            if self.rear < 0:
                self.rear = MAX_SIZE - 1
            return item

    def getRear(self):
        return self.items[self.rear]


def main():
    c = CircularDeque()
    print("Enter a command: af(addFront), df(deleteFront), gf(getFront), s(ize), ar(addRear), dr(deleteRear), gr(getRear), p(rint), or q(uit)")
    while True:
        user_input = input().split()
        if len(user_input) == 2:
            command, item = user_input
        else:
            command = "".join(user_input)
        if command == 'ar':
            c.addRear(item)
        elif command == 'af':
            c.addFront(item)
        elif command == 'gf':
            print(c.getFront())
        elif command == 'gr':
            print(c.getRear())
        elif command == 'p':
            print(c.print())
        elif command == 'dr':
            print(c.deleteRear())
        elif command == 'df':
            print(c.deleteFront())
        elif command == 'q':
            break
        elif command == 's':
            print(f"size: {c.size()}")


main()
