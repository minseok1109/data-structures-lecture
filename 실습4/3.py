import copy

inFile = open(
    '/Users/bang/Documents/project/자료구조/실습4/maze.txt', 'r', encoding="euc-kr")
lines = inFile.readlines()
pos = lines.pop(0).strip()
maze = []
for item in lines:
    maze.append(list(item.strip()))

col, row = map(int, pos.split(' '))
inFile.close()

inFile1 = open(
    '/Users/bang/Documents/project/자료구조/실습4/input1.txt', 'r', encoding="euc-kr")
lines = inFile1.readlines()
inFile1.close()

pos_list = []
for item in lines:
    pos_list.append(item.strip())


def isValid(x, y, load):
    if x < 0 or x > col - 1 or y < 0 or y > row - 1:
        return False
    else:
        return load[x][y] == '0' or load[x][y] == 'E'


def DFS(start_pos, maze):
    load = copy.deepcopy(maze)
    start = [start_pos]
    while len(start) != 0:
        a, b = "".join(start.pop()).split(' ')
        x = int(a)
        y = int(b)
        if load[x - 1][y - 1] == 'E':
            return True
        else:
            load[x - 1][y - 1] = '.'
            # 좌
            if isValid(x - 1, y - 2, load):
                start.append(f"{x} {y - 1}")
            # 우
            if isValid(x - 1, y, load):
                start.append(f"{x} {y + 1}")
            # 상
            if isValid(x - 2, y - 1, load):
                start.append(f"{x - 1} {y}")
            # 하
            if isValid(x, y - 1, load):
                start.append(f"{x + 1} {y}")
    return False


def main():
    while pos_list:
        start_pos = pos_list.pop(0)
        start_x, start_y = start_pos.split(' ')
        if DFS(start_pos, maze):
            print(f"({start_x}, {start_y}) 에서 출발 ==> O, 성공")
        else:
            print(f"({start_x}, {start_y}) 에서 출발 ==> X, 실패")


main()
