f = open('output.txt', 'w')

maxNum = 0
for i in range(0, len(m.arr)):
  if m.arr[i] is not None:
    if m.arr[i].size > maxNum:
      maxNum = m.arr[i].size

    size = str(m.arr[i].size)
  else:
    size = 'None'
  
  f.write(str(i) + ' ' + size + '\n')

f.write('MaxNum = ' + str(maxNum))

f.close()




f = open('test.txt', 'r')

t = int(round(time.time() * 1000))
T = int(f.readline())
for i in range(0, T):
  NK = list(map(int, f.readline().split()))
  s = f.readline()
  print(count(s, NK[0], NK[1]))

t1 = int(round(time.time() * 1000))
print((t1 - t) / 1000)

f.close()

  