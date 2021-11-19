class BTNode:
    # 생성자
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left  # 왼쪽 자식을 위한 링크
        self.right = right  # 오른쪽 자식을 위한 링크


class BTree:
    def __init__(self):
        self.root = None
        self.Flag = 0

    def buildTree(self):
        g = BTNode(12)
        d = BTNode(15, g)
        b = BTNode(10, None, d)
        e = BTNode(25)
        f = BTNode(55)
        c = BTNode(30, e, f)
        self.root = BTNode(20, b, c)
    # 구현해야 할 멤버 함수

    def inorder1(self, node):
        if node is not None:
            self.inorder1(node.left)
            print(node.item, end=" ")
            self.inorder1(node.right)

    def RVLorder(self):
        self.RVLorder1(self.root)
        print()

    def RVLorder1(self, node):
        if node is not None:
            self.RVLorder1(node.right)
            print(f"{node.item}", end="")
            self.R_L_check(node)
            self.RVLorder1(node.left)

 #  R,L 판단하고 붙이는 함수

    def R_L_check(self, node):
        if node.left and node.right:
            print(",L,R")
        elif node.left and not node.right:
            print(",L")
        elif not node.left and node.right:
            print(",R")
        else:
            print("")

    def test(self):
        print(self.RVLorder1(self.root))


bt = BTree()
bt.buildTree()
print(bt.test())
