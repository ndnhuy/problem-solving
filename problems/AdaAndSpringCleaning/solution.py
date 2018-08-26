class Node:
  def __init__(self, key, next=None):
    self.key = key
    self.next = next
    self.size = 0

class SeparateChainingHashMap:
  def __init__(self, initSize=100):
    l = initSize // 5
    self.tableSize = initSize if l == 0 else l
    self.arr = [None]*self.tableSize
    self.size = 0
    self.collisionCount = 0
    self.hashTime = 0
  
  def put(self, key):
    i = self.__hashCode(key) % len(self.arr)
    if self.arr[i] is not None:
      t = self.arr[i]
      p = t
      while t is not None and t.key != key:
        p = t
        t = t.next

      if t is None:
        p.next = Node(key)
        self.size = self.size + 1
        self.arr[i].size = self.arr[i].size + 1
    else:
      self.arr[i] = Node(key)
      self.size = self.size + 1
      self.arr[i].size = self.arr[i].size + 1

  def __hashCode(self, key):
    # hashCode = 0
    # for c in key:
    #   hashCode = (31 * hashCode + ord(c)) % self.tableSize
    # return hashCode;
    return (hash(key) & 0x7fffffff) % self.tableSize


class HashMap:
  def __init__(self, initSize=17):
    self.arr = [None]*initSize
    self.size = 0
    self.collisionCount = 0

  def values(self):
    return list(filter(lambda x : x is not None, self.arr))

  def put(self, key):
    if self.size >= len(self.arr) // 2:
      cloneArr = [None]*len(self.arr)*2
      for i in range(0, len(self.arr)):
        cloneArr[i] = self.arr[i]
      self.arr = cloneArr

    i = self.__hashCode(key) % len(self.arr)
    if self.__isOccupied(key, i):
      self.collisionCount = self.collisionCount + 1
    while self.__isOccupied(key, i):
      i = (i + 1) % len(self.arr)

    if self.arr[i] is None:
      self.arr[i] = key
      self.size = self.size + 1

  def __isOccupied(self, key, i):
    return self.arr[i] is not None and self.arr[i] != key

  def get(self, key):
    start = self.__hashCode(key) % len(self.arr)
    end = len(self.arr) - 1 if start == 0 else start - 1
    i = start
    while i != end and self.arr[i] is not None and self.arr[i] != key:
      i = (i + 1) % len(self.arr)

    if self.arr[i] is None:
      return None

    if self.arr[i] == key:
      return self.arr[i]
    
    return None

  def __hashCode(self, key):
    hashCode = 17
    for c in key:
      hashCode = 31 * hashCode + ord(c)
    
    return hashCode

def count(s, n, k):
  m = SeparateChainingHashMap(len(s))
  i = 0
  j = k - 1
  while j < n:
    m.put(s[i:i+k])
    i = i + 1
    j = j + 1

  return m.size;

def read(f=None):
  if f is None:
    return input()
  else:
    return f.readline()

f = open('test.txt', 'r')

T = int(read(f))
for i in range(0, T):
  NK = list(map(int, read(f).split()))
  s = read(f)
  print(count(s, NK[0], NK[1]))

f.close()
