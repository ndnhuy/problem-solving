from random import randint
import time
RAND_MIN = 0
RAND_MAX = 1999999999

class Pair:
    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second

class Node:
    def __init__(self, key, value, priority, left, right, size=1):
        self.key = key
        self.value = value
        self.priority = priority
        self.left = left
        self.right = right
        self.size = size

    def toString(self):
        return str(self.key) + ' - ' + str(self.value) + ' - ' + str(self.priority) + ' - ' + str(self.size)

class TreapTree:
    def __init__(self, root=None):
        self.root = root

    def height(self):
        return self.__height(self.root)

    def fromArray(self, keys=[]):
        for i in range(0, len(keys)):
            self.insert(i, keys[i])
        return self

    def print(self):
        self.__printPreOrder(self.root)
        return self

    def insert(self, key, value):
        self.__insert(self.root, key, value)

    def split(self, key):
        splitRes = self.__split(self.root, key)
        return Pair(TreapTree(splitRes.first), TreapTree(splitRes.second))

    def merge(self, rightTree):
        self.root = self.__merge(self.root, rightTree.root)
        return self

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

    def toArray(self):
        a = [None]*self.__size(self.root)
        self.__toArray(self.root, a)
        return a

    def __toArray(self, node, a, smallerNodeCount=0):
        if node is None:
            return

        k = self.__key(node, smallerNodeCount)
        a[k] = node.value
        self.__toArray(node.left, a, smallerNodeCount)
        self.__toArray(node.right, a, smallerNodeCount + self.__size(node.left) + 1)

    def __insert(self, t, key, value):
        splitResult = self.__split(t, key)
        l = self.__merge(splitResult.first, Node(key, value, randint(RAND_MIN, RAND_MAX), None, None))
        r = splitResult.second
        self.root = self.__merge(l, r)

    def __split(self, t, key, smallerNodeCount=0):
        if t is None:
            return Pair(None, None)

        if key < self.__key(t, smallerNodeCount):
            splitResult = self.__split(t.left, key, smallerNodeCount)
            t.left = splitResult.second
            self.__updateSize(splitResult.first)
            self.__updateSize(t)
            return Pair(splitResult.first, t)
        
        if key >= self.__key(t, smallerNodeCount):
            splitResult = self.__split(t.right, key, smallerNodeCount + self.__size(t.left) + 1)
            t.right = splitResult.first
            self.__updateSize(t)
            self.__updateSize(splitResult.second)
            return Pair(t, splitResult.second)

    def __merge(self, leftRoot, rightRoot):
        if leftRoot is None:
            return rightRoot

        if rightRoot is None:
            return leftRoot

        if leftRoot.priority <= rightRoot.priority:
            rightRoot.left = self.__merge(leftRoot, rightRoot.left)
            self.__updateSize(rightRoot)
            return rightRoot

        if leftRoot.priority > rightRoot.priority:
            leftRoot.right = self.__merge(leftRoot.right, rightRoot)
            self.__updateSize(leftRoot)
            return leftRoot

    def __key(self, node, smallerNodeCount):
        return self.__size(node.left) + smallerNodeCount

    def __updateSize(self, node):
        if node is None:
            return

        node.size = 1 + self.__size(node.left) + self.__size(node.right)

    def __size(self, node):
        return 0 if node is None else node.size

    def __height(self, node):
        if node is None:
            return 0
        return 1 + self.__max(self.__height(node.left), self.__height(node.right))

    def __max(self, l, r):
        return l if l > r else r

    def __printPreOrder(self, node):
        if node is None:
            print('none')
            return

        print(node.toString())
        self.__printPreOrder(node.left)
        self.__printPreOrder(node.right)

tree = TreapTree()
def main():
    f = open('input16.txt', 'r')
    def readline():
        #return input()
        return f.readline()

    firstLine = list(map(int, readline().split(' ')))
    N = firstLine[0]
    M = firstLine[1]

    arr = list(map(int, readline().split(' ')))
    t1 = time.time()
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
