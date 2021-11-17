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
        c = BTNode(30)
        self.root = BTNode(20, b, c)

    def inorder(self):
        self.inorder1(self.root)
        print()

    def inorder1(self, node):
        if self.root is not None:
            self.inorder1(self.left)
            print(self.data, end=" ")
            self.inorder1(self.right)

    def preorder(self):
        if self.root is not None:
            print(self.root.item, end=" ")
            self.preorder(self.root.left)
            self.preorder(self.root.right)

    def postorder(self):
        self.postorder(self.root.left)
        self.postorder(self.root.right)
        print(self.root.item, end=" ")

    def nodeCount(self):
        if self.root is None:
            return 0
        else:
            return 1 + self.nodeCount(self.root.left) + self.nodeCount(self.root.right)

    def leafCount(self):
        if self.root is None:
            return 0
        elif self.left.item is None and self.rigth.item is None:
            return 1
        else:
            return self.nodeCount(self.root.left) + self.nodeCount(self.root.right)

    def height(self):
        if self.root is None:
            return 0
        hLeft = self.height(self.root.left)
        hRight = self.height(self.root.right)
        if hLeft > hRight:
            return hLeft + 1
        else:
            return hRight + 1
    # def print(self):
        

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