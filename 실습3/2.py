class Arraylist:
    def __init__(self):
        self.items = []


    def insert(self, pos, elem):
        self.items.insert(pos, elem)

    def delete(self, pos1, pos2):
        if pos1 == pos2:
            self.ites.pop(pos1)
        else:
            for i in range(pos1, pos2+1):
                self.items.pop(i)
        

    def size(self):
        return len(self.items)

    def replace(self, pos, elem):
        self.items[pos-1] = elem

    def print(self):
        for idx, line in enumerate(self.items):
            print(idx+1, line)


def main():
    array = Arraylist()
    inFile = open('/Users/bang/Documents/project/자료구조/실습3/input.txt', 'r', encoding="euc-kr")
    lines = inFile.readlines()
    for line in lines:
        array.insert(array.size()+1, line.rstrip('\n'))
    inFile.close()


    while True:
        user_input = input().split(' ')
        if len(user_input) == 2:
            command = user_input[0]
            pos = int(user_input[1])

        elif len(user_input) == 1:
            command = user_input[0]
        elif len(user_input) == 3:
            command = user_input[0]
            pos1 = int(user_input[1])
            pos2 = int(user_input[2])
        if command == 'q':
            break
        elif command == 'p':
            array.print()
        elif command == 'i':
            while True:
                elem = input()
                if elem == '*':
                    break
                array.insert(pos-1, elem)
                pos +=1
        elif command == 'd':
            array.delete(pos1, pos2)
        elif command == 'r':
            elem = input()
            array.replace(pos, elem)


main()
