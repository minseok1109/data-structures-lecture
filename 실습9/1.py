class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BTree:
    def __init__(self):
        self.root = None

    def buildTree(self):
        g = BTNode(12)
        d = BTNode(15, g)
        b = BTNode(10, None, d)
        e = BTNode(25)
        f = BTNode(55)
        c = BTNode(30, e, f)
        self.root = BTNode(20, b, c)

    def inorder(self):
        self.inorder1(self.root)
        print()

    def inorder1(self, node):
        if node is not None:
            self.inorder1(node.left)
            print(node.item, end=" ")
            self.inorder1(node.right)

    def preorder(self):
        self.preorder1(self.root)
        print()

    def preorder1(self, node):
        if node is not None:
            print(node.item, end=" ")
            self.preorder1(node.left)
            self.preorder1(node.right)

    def postorder(self):
        self.postorder1(self.root)
        print()

    def RVL(self):
        self.RVL1(self.root)
        print()

    def RVL1(self, node):
        if node is not None:
            self.RVL1(node.right)
            print(f"{node.item}", end="")
            self.check_left_right(node)
            self.RVL1(node.left)

    def check_left_right(self, node):
        left = False
        right = False
        if node.left and node.right:
            left = right = True
            print(",L,R")
            return left, right
        elif node.left and not node.right:
            left = True
            right = False
            print(",L")
            return left, right
        elif not node.left and node.right:
            right = True
            left = False
            print(",R")
            return left, right
        else:
            print("")
            return left, right

    def check_left_right1(self, node):
        left = False
        right = False
        if node.left and node.right:
            left = right = True
            return left, right
        elif node.left and not node.right:
            left = True
            right = False
            return left, right
        elif not node.left and node.right:
            right = True
            left = False
            return left, right
        else:
            return left, right

    def postorder1(self, node):
        if node is not None:
            self.postorder1(node.left)
            self.postorder1(node.right)
            print(node.item, end=" ")

    def nodeCount(self):
        return self.nodeCount1(self.root)

    def nodeCount1(self, node):
        if node is None:
            return 0
        return 1 + self.nodeCount1(node.left) + self.nodeCount1(node.right)

    def leafCount(self):
        return self.leafCount1(self.root)

    def leafCount1(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.leafCount1(node.left) + self.leafCount1(node.right)

    def height(self):
        return self.height1(self.root)

    def height1(self, node):
        if node is None:
            return 0
        hLeft = self.height1(node.left)
        hRight = self.height1(node.right)
        if hLeft > hRight:
            return hLeft + 1
        else:
            return hRight + 1

    def print(self):
        left, right = self.check_left_right1(self.root)
        self.RVL1(self.root)


def main():
    bt = BTree()
    print("Enter a command: bt(build tree), inorder(traversal), pre(order traversal")
    print("post(order traversal), nc(node count), lc(leaf count), h(eight),")
    print("pp(pretty print), or q(uit)")

    while True:
        print("> ", end="")
        line = input().split()
        command = line[0]
        if command == 'bt':
            bt.buildTree()
        elif command == 'inorder':
            bt.inorder()
        elif command == 'pre':
            bt.preorder()
        elif command == 'post':
            bt.postorder()
        elif command == 'nc':
            print(f"node count = {bt.nodeCount()}")
        elif command == 'lc':
            print(f"leaf count = {bt.leafCount()}")
        elif command == 'h':
            print(f"height = {bt.height()}")
        elif command == 'pp':
            bt.print()
        elif command == 'q':
            break


main()
