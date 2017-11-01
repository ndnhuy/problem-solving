class Node:
    def __init__(self, key, value, left, right, count):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.count = count

class BST:
    def __init__(self, keys=[]):
        self.root = None
        
        if keys != []:
            for key in keys:
                self.put(key, key)

    def print(self):
        self.__printPreOrder(self.root)

    def printSubtree(self, key):
        self.__printPreOrder(self.__search(self.root, key))

    def put(self, key, value):
        self.root = self.__put(self.root, key, value)

    def get(self, key):
        return self.__search(self.root, key).value

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if node is None:
            return 0

        leftHeight = self.__height(node.left)
        rightHeight = self.__height(node.right)
        return 1 + (leftHeight if leftHeight > rightHeight else rightHeight)

    def __search(self, node, key):
        if key < node.key:
            return self.__search(node.left, key)
        elif key > node.key:
            return self.__search(node.right, key)
        else:
            return node

    def __put(self, node, key, value):
        if node is None:
            return Node(key, value, None, None, 1)

        if key < node.key:
            node.left = self.__put(node.left, key, value)
        elif key > node.key:
            node.right = self.__put(node.right, key, value)
        else:
            node.value = value

        return node
 
    def __printPreOrder(self, node):
        if node is None:
            return

        print(node.value)
        self.__printPreOrder(node.left)
        self.__printPreOrder(node.right)

    def __printInOrder(self, node):
        if node is None:
            return

        self.__printInOrder(node.left)
        print(node.value)
        self.__printInOrder(node.right)

# lines = []
# N = int(input())
# items = list(map(int, input().split( )))
# tree = BST(items)
# print(tree.height())

####### READ FROM TEST FILE #############

f = open('test.txt', 'r')
N = f.readline()
items = list(f.readline().split())
tree = BST(items)
tree.print()