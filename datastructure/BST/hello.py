class MaxPQ:
    def __init__(self, a=[], callInsert=False):
        if callInsert == False:
            self.pq = a
            return

        self.pq = []
        for key in a:
            self.insert(key)

    def insert(self, key):
        self.pq.append(key)
        k = len(self.pq) - 1
        while (k > 1 and self.pq[k] > self.pq[k//2]):
            self.exchange(k, k//2)
            k = k//2

    def removeMax(self):
        pq = self.pq
        self.exchange(len(pq) - 1, 1)
        self.pq.pop(len(pq) - 1)

        k = 1
        while (2*k < len(pq)):
            if 2*k + 1 > len(pq) - 1:
                greaterChildIndex = 2*k
            else:
                greaterChildIndex = 2*k if pq[2*k] > pq[2*k + 1] else 2*k + 1

            if pq[k] >= pq[greaterChildIndex]:
                break

            self.exchange(k, greaterChildIndex)
            k = greaterChildIndex

    def exchange(self, x, y):
        tmp = self.pq[x]
        self.pq[x] = self.pq[y]
        self.pq[y] = tmp

###########
class MinPQ:
    def __init__(self, a=[''], callInsert=False):
        if callInsert == False:
            self.pq = a
            return

        self.pq = []
        for key in a:
            self.insert(key)

    def insert(self, key):
        self.pq.append(key)
        k = len(self.pq) - 1
        while (k > 1 and self.less(self.pq[k], self.pq[k//2])):
            self.exchange(k, k//2)
            k = k//2

    def removeMin(self):
        pq = self.pq
        self.exchange(len(pq) - 1, 1)
        returnValue = self.pq.pop(len(pq) - 1)

        k = 1
        while (2*k < len(pq)):
            if 2*k + 1 > len(pq) - 1:
                smallerChildIndex = 2*k
            else:
                smallerChildIndex = 2*k if self.less(pq[2*k], pq[2*k + 1]) else 2*k + 1

            if self.less(pq[k], pq[smallerChildIndex]):
                break

            self.exchange(k, smallerChildIndex)
            k = smallerChildIndex

        return returnValue

    def exchange(self, x, y):
        tmp = self.pq[x]
        self.pq[x] = self.pq[y]
        self.pq[y] = tmp

    def less(self, x, y):
        return x.compareTo(y) < 0

    def isEmpty(self):
        return len(self.pq) == 1

###########
class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def compareTo(self, node):
        return self.value - node.value

##### K-way merging #####
sortedArrays = [
    [1, 3, 5, 7, 10, 11],
    [2, 4, 6, 8, 13, 15],
    [0, 9, 10, 11, 18, 19]
]

indices = []
for k in range(len(sortedArrays)):
    indices.append(0)

minPQ = MinPQ()
for k in range(len(sortedArrays)):
    unmergedValue = sortedArrays[k][indices[k]]
    node = Node(k, unmergedValue)
    minPQ.insert(node)

def fillUpTheHeap(sortedArrays, indices, index):
    if (indices[index] < len(sortedArrays[index]) - 1):
        indices[index] = indices[index] + 1
        nextValue = sortedArrays[index][indices[index]]
        minPQ.insert(Node(index, nextValue))
        return

    for k in range(len(sortedArrays)):
        if indices[index] >= len(sortedArrays[index]) - 1:
            continue

        indices[k] = indices[k] + 1
        nextValue = sortedArrays[k][indices[k]]
        minPQ.insert(Node(k, nextValue))
        break

output = []
while not (minPQ.isEmpty()):
    node = minPQ.removeMin()
    output.append(node.value)
    fillUpTheHeap(sortedArrays, indices, node.index)

#### Console ####
print(output)

##########
# minPQ = MinPQ(['', 12, 6, 8, 4, 3, 5, 1], True)
# maxPQ = MaxPQ(['', 6, 12], True)
# print('init: %s' % minPQ.pq)
# minPQ.removeMin()
# print('removeMax(): %s' % minPQ.pq)
# minPQ.removeMin()
# print('removeMax(): %s' % minPQ.pq)
# minPQ.insert(0)
# print('removeMin(): %s' % minPQ.pq)
# minPQ.insert(1)
# print('removeMin(): %s' % minPQ.pq)