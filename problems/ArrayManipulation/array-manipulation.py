# 0    0    0    0    0    0    0    0    0    0

# 100  100
#      100  100  100  100
#           100  100
#                               50   50   50
#                10   10   10   10   10

# 100  0    -100 0    0    0    0    0    0    0
# 100  100  -100 0    0    -100 0    0    0    0
# 100  100  0    0    -100 -100 0    0    0    0
# 100  100  0    0    -100 -100 50   0    0    -50
# 100  100  0    10   -100 -100 50   0    -10  -50

# 100  200  200  210  110  10   60   60   50   0

def arrayManipulation(n, queries):
    #
    # Write your code here.
    #
    a = []
    for i in range(n):
      a.append(0)

    for q in queries:
      i = q[0] - 1
      j = q[1] - 1
      k = q[2]
      a[i] = a[i] + k
      if j + 1 < len(a):
        a[j + 1] = a[j + 1] - k
    
    # update real value for array
    for i in range(1, n):
      a[i] = a[i-1] + a[i]

    maxNum = a[0]
    for i in range(n):
      if a[i] > maxNum:
        maxNum = a[i]
    
    return maxNum

print(arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4,100]]))
print(arrayManipulation(10, [[1, 2, 100], [2, 5, 100], [3, 4, 100], [7, 9, 50], [4, 8, 10]]))
