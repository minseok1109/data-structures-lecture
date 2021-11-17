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
        return self.front == (self.rear+1) % MAX_SIZE

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
        self.count +=1

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.max_size
            self.count -=1
            return self.items[self.front]

    def resize(self):
        newItems = [None] * 2 * self.max_size
        scan = (self.front + 1) % self.max_size
        for i in range(self.count):
            newItems[i+1] = self.items[scan]
            scan = (scan + 1) % self.max_size
        
        self.items = newItems
        self.front = 0
        self.rear = self.count
        self.max_size = 2 * self.max_size

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % self.max_size]

    def size(self):
        return f"size: {self.count}"

    def print(self):
        temp = []
        if self.rear > self.front:
            temp = self.items[self.front + 1: self.rear+1]
        else:
            temp = self.items[self.front+1:MAX_SIZE] + \
                self.items[0:self.rear+1]
        return f"{temp}"

def main():
    q = CircularQueue()
    print("Enter a command: e(nqueue), d(equeue), s(size), p(rint), or q(uit)")

    while True:
        user_input = input().split()
        if len(user_input) == 2:
            command, item = user_input
        else:
            command = "".join(user_input)
        if command == 'e':
            q.enqueue(item)
        elif command == 'd':
            print(q.dequeue())
        elif command == 's':
            print(q.size())
        elif command == 'p':
            print(q.print())
        elif command == 'peek':
            print(q.peek())
        elif command == 'q':
            break

main()

