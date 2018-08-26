# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

def sherlockAndAnagrams(s):
  sum = 0
  for subStringLen in range(1, len(s) + 1):
    sum = sum + calculateAnagrams(s, subStringLen)
  return sum

def calculateAnagrams(s, subStrLen):
  anagrams = {}
  start = 0
  while (start + subStrLen <= len(s)):
    subStr = s[start:start+subStrLen]
    hashValue = computeHash(subStr)
    if hashValue in anagrams:
      anagrams[hashValue].append(subStr)
    else:
      anagrams[hashValue] = []
    
    start = start + 1
  
  # calculate the number of anagrams
  sum = 0
  for key in anagrams:
    n = len(anagrams[key])
    sum = sum + n * (n + 1) / 2
  return int(sum)

def computeHash(s):
  return sorting(s)

def sorting(str):
  s = list(str)
  i = 0
  while (i < len(s)):
    k = i
    while (k > 0 and s[k] < s[k-1]):
      tmp = s[k]
      s[k] = s[k-1]
      s[k-1] = tmp
      k = k-1
    
    i = i+1
  return ''.join(s)