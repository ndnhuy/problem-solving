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
        newNode = Node(key, value, None, None, 1)
        if node is None:
            return newNode

        iter = node
        while True:
            if key <= node.key:
                if iter.left == None:
                    iter.left = newNode
                    break
                iter = iter.left
            else:
                if iter.right == None:
                    iter.right = newNode
                    break
                iter = iter.right
        return node
 
    def __printPreOrder(self, node):
        if node is None:
            return
            
        stack = []
        iter = node
        stack.append(iter)
        while (len(stack) != 0):
            iter = stack.pop(len(stack) - 1)
            print(iter.value)
            if iter.right is not None:
                stack.append(iter.right)
            if iter.left is not None:
                stack.append(iter.left)

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

f = open('test1.txt', 'r')
N = f.readline()
items = list(f.readline().split())
tree = BST(items)
tree.print()