from random import randint
import sys
RAND_MIN = 0
RAND_MAX = 1000000000

class Container:
    def __init__(self, value=None):
        self.value = value

class Pair:
    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second

class Node:
    def __init__(self, key, value, priority, left, right, parent):
        self.key = key
        self.value = value
        self.priority = priority
        self.left = left
        self.right = right
        self.parent = parent

    def toString(self):
        return str(self.key) + ' - ' + str(self.value) + ' - ' + str(self.priority) + ' COUNT: ' + str(self.count)

# Slower version
class TreapTree:
    def __init__(self, root=None, count=0):
        self.count = count
        self.root = root
        if self.root is not None:
            self.root.parent = None

    def fromArray(self, keys=[]):
        for i in range(0, len(keys)):
            self.insert(i, keys[i], randint(RAND_MIN, RAND_MAX))

    def insert(self, key, value, priority):
        newNodeRef = Container()
        self.root = self.__insert(self.root, key, value, priority, newNodeRef)
        self.count = self.count + 1

        if newNodeRef.value is not None:
            self.root = self.__moveUp(newNodeRef.value)

    def test(self, key):
        t = self.__search(self.root, key)
        print(self.__key(t))

    def moveToFront(self, i, j):
        p1 = self.split(j) # [0..j] and [j+1..len]

        p2 = p1.first.split(i-1) # [0..i-1] and [i..j]
        mergedTree = p2.second.merge(p2.first) # [i..j] + [0..i-1]

        self.root = mergedTree.merge(p1.second).root
        return self

    def moveToBack(self, i, j):
        p1 = self.split(i-1) # [0..i-1] and [i..len]

        p2 = p1.second.split(j - i) # [i..j] and [j+1..len]
        mergedTree = p2.second.merge(p2.first) # [j+1..len] + [i..j]

        self.root = p1.first.merge(mergedTree).root
        return self

    def size(self):
        return self.__size(self.root)

    def search(self, key):
        result = self.__search(self.root, key)
        return None if result is None else result.value

    def merge(self, rightTree):
        self.root = self.__merge(self.root, rightTree.root)
        return self

    def split(self, key):
        self.insert(key, key, sys.maxsize)
        return Pair(TreapTree(self.root.left, self.count*2), TreapTree(self.root.right, self.count*2))
    def print(self):
        self.__printPreOrder(self.root)

    def toArray(self):
        a = [None]*self.__size(self.root)
        self.__toArray(self.root, a)
        return a

    def __toArray(self, node, a):
        if node is None:
            return

        k = self.__key(node)
        a[k] = node.value
        self.__toArray(node.left, a)
        self.__toArray(node.right, a)

    def __insert(self, node, key, value, priority, newNodeRef):
        if node is None:
            newNodeRef.value = Node(key, value, priority, None, None, None)
            newNodeRef.value.count = self.count
            return newNodeRef.value

        if key <= self.__key(node):
            node.left = self.__insert(node.left, key, value, priority, newNodeRef)
            node.left.parent = node
        else:
            node.right = self.__insert(node.right, key, value, priority, newNodeRef)
            node.right.parent = node

        return node

    def __search(self, node, key):
        if node is None:
            return None

        k = self.__key(node)
        if key < k:
            return self.__search(node.left, key)
        elif key > k:
            return self.__search(node.right, key)
        else:
            return node

    def __merge(self, leftNode, rightNode):
        if leftNode is None:
            return rightNode

        if rightNode is None:
            return leftNode

        if leftNode.priority >= rightNode.priority:
            leftNode.right = self.__merge(leftNode.right, rightNode)
            leftNode.right.parent = leftNode
            return leftNode
        else:
            rightNode.left = self.__merge(leftNode, rightNode.left)
            rightNode.left.parent = rightNode
            return rightNode

    def __moveUp(self, node):
        if node.parent is None:
            return node

        heapRoot = node.parent
        leftPriority = -1 if heapRoot.left is None else heapRoot.left.priority 
        rightPriority = -1 if heapRoot.right is None else heapRoot.right.priority

        if heapRoot.priority >= self.__max(leftPriority, rightPriority):
            return self.__moveUp(heapRoot)

        if leftPriority >= rightPriority:
            t = self.__rotateRight(heapRoot)
        else:
            t = self.__rotateLeft(heapRoot)

        if t.parent is None:
            return t

        if t.parent.left is heapRoot:
            t.parent.left = t
        elif t.parent.right is heapRoot:
            t.parent.right = t

        return self.__moveUp(t)

    def __key(self, node):
        if node is None:
            return -1

        result = self.__size(node.left) + self.__key(self.__findNearestParentThatSmaller(node)) + 1
        return result

    def __findNearestParentThatSmaller(self, node):
        if node.parent is None:
            return None

        if node.parent.left is node:
            return self.__findNearestParentThatSmaller(node.parent)

        if node.parent.right is node:
            return node.parent

    def __size(self, node):
        if node is None:
            return 0

        return 1 + self.__size(node.left) + self.__size(node.right)

    def __rotateRight(self, node):
        # the given node in this case is the max priority node used to split the tree
        # block of code below is to move that max-priority-node upto the tree and
        # the comparision here just to keep the node which has split-key lying on the left-treap-tree after split 
        if self.__key(node) - 1 == node.left.key:
            temp = node.left.priority
            node.left.value = node.value
            node.left.priority = node.priority
            node.priority = temp

            keyTemp = node.left.key
            node.left.key = node.key
            node.key = keyTemp

            return node

        t = node.left
        node.left = t.right
        t.right = node
        t.parent = node.parent
        node.parent = t
        if node.left is not None:
            node.left.parent = node
        return t

    def __rotateLeft(self, node):
        t = node.right
        node.right = t.left
        t.left = node
        t.parent = node.parent
        node.parent = t
        if node.right is not None:
            node.right.parent = node
        return t

    def __printPreOrder(self, node):
        if node is None:
            print('none')
            return

        print(node.toString())
        self.__printPreOrder(node.left)
        self.__printPreOrder(node.right)

    def __max(self, v1, v2):
        return (v1 if v1 >= v2 else v2)

def main():
    f = open('input03.txt', 'r')
    def readline():
        #return input()
        return f.readline()

    firstLine = list(map(int, readline().split(' ')))
    N = firstLine[0]
    M = firstLine[1]

    arr = list(map(int, readline().split(' ')))
    tree = TreapTree()
    tree.fromArray(arr)
    for i in range(0, M):
        q = list(map(int, readline().split(' ')))
        if q[0] == 1:
            tree.moveToFront(q[1] - 1, q[2] - 1)
        else:
            tree.moveToBack(q[1] - 1, q[2] - 1)

    result = tree.toArray()
    k = result[0] - result[len(arr) - 1]
    k = -k if k < 0 else k
    print(k)

    print(' '.join(map(str, result)))

main()