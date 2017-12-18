from enum import Enum
class Color(Enum):
    BLACK = 0
    RED = 1

class Node:
    def __init__(self, key, value, left, right, count, color):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.count = count
        self.color = color

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
        result = self.__search(self.root, key)
        return 'None' if result is None else result.value

    def rank(self, key):
        return self.__rank(self.root, key)

    def floor(self, key):
        return self.__floor(self.root, key).key

    def height(self):
        return self.__height(self.root)

    def __rank(self, node, key):
        if node is None:
            return -1

        if key < node.key:
            return self.__rank(node.left, key)
        if key == node.key:
            return self.__size(node.left)
        if key > node.key:
            return 1 + self.__rank(node.right, key)

    def __floor(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self.__floor(node.left, key)
        if key == node.key:
            return node
        result = self.__floor(node.right, key)
        if result is None:
            return node
        else:
            return result

    def __size(self, node):
        if node is None:
            return 0
        return self.__size(node.left) + self.__size(node.right) + 1

    def __height(self, node):
        if node is None:
            return 0

        leftHeight = self.__height(node.left)
        rightHeight = self.__height(node.right)
        return 1 + (leftHeight if leftHeight > rightHeight else rightHeight)

    def __search(self, node, key):
        if node is None:
            return None;

        if key < node.key:
            return self.__search(node.left, key)
        elif key > node.key:
            return self.__search(node.right, key)
        else:
            return node

    def __put(self, node, key, value):
        if node is None:
            return Node(key, value, None, None, 1, Color.RED)

        if key < node.key:
            node.left = self.__put(node.left, key, value)
        elif key > node.key:
            node.right = self.__put(node.right, key, value)
        else:
            node.value = value

        if self.__isRed(node.right) and not self.__isRed(node.left):
            node = self.__rotateLeft(node)
        if self.__isRed(node.left) and self.__isRed(node.left.left):
            node = self.__rotateRight(node)
        if self.__isRed(node.left) and self.__isRed(node.right):
            node = self.__flipColor(node)

        return node

    def __isRed(self, node):
        if node is None:
            return False

        return node.color is Color.RED

    def __rotateLeft(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = Color.RED
        return x

    def __rotateRight(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = Color.RED
        return x

    def __flipColor(self, node):
        node.left.color = Color.BLACK
        node.right.color = Color.BLACK
        node.color = Color.RED
        return node
 
    def __printPreOrder(self, node):
        if node is None:
            print('none')
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
# startRoot = int(input())
# print(list(map(int, items)))
# tree = BST(items)
# tree.printSubtree(startRoot)

####### READ FROM TEST FILE #############

f = open('BST/test.txt', 'r')
N = f.readline()
items = list(map(int, f.readline().split()))
tree = BST(items)

#print(tree.get(775))

tree = BST(list(map(int, '7 10 29 32 40 52 55 76 83 103 116 122'.split(' '))))
tree.print()

# tree = BST([1,2,3,4,5])
# tree.print()