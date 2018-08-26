# from random import *
# s = ''
# n = 100000
# while (len(s) < n):
#   s = s + chr(randint(97, 122))

# f = open('test.txt', 'w')
# f.write(str(n) + '\n')
# f.write(s)
# f.close()
import time

def now():
  return int(round(time.time() * 1000))

def hashCode(key):
  hashCode = 0
  for c in key:
    hashCode = (31 * hashCode + ord(c)) % 20000
  
  return hashCode;

f = open('test2.txt', 'r')
out = open('output.txt', 'w')

totalTime = 0

s = f.readline()
k = 330

i = 0
j = k - 1
n = 100000
while j < n:
    t1 = now()
    h = hashCode(s[i:i+k])
    t2 = now()

    duration = (t2 - t1) / 1000
    totalTime = totalTime + duration
    out.write(str(duration) + '\n')

    i = i + 1
    j = j + 1

print('Total = ' + str(totalTime))

f.close()
out.close()