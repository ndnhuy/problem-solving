#!/bin/python3

#
# Complete the findSuffix function below.
#
def findSuffix(collections, queryString):
    #
    # Write your code here.
    #
    c = 0
    for i in range(0, len(collections)):
      if collections[i] == queryString:
        c = c + 1

    return c


if __name__ == '__main__':
    f = open('input.txt', 'r')

    strings_count = int(f.readline())

    strings = []

    for _ in range(strings_count):
        strings_item = f.readline()
        strings.append(strings_item)

    q = int(f.readline())

    for q_itr in range(q):
        queryString = f.readline()

        res = findSuffix(strings, queryString)

        #f.write(str(res) + '\n')
        print(res)

    f.close()
