# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
def climbingLeaderboard(scores, alice):
  ranks = []
  toIndex = len(scores) - 1
  for aliceScore in alice:
    if len(scores) == 0:
      ranks.append(1)

    k = findClosestScorePosition(scores, aliceScore, toIndex)

    if aliceScore < scores[k]:
      ranks.append(rank(scores, k, toIndex) + 1)
    if aliceScore >= scores[k]:
      ranks.append(rank(scores, k))
    
    toIndex = k

  return ranks

def findClosestScorePosition(scores, aliceScore, toIndex):
  return binarySearchClosest(scores, aliceScore, 0, toIndex)

def rank(scores, k, knownIndex, knownRank):
  rank = knownRank
  for i in reversed(range(k, knownIndex + 1)):
    if i < knownIndex and scores[i] != scores[i+1]:
      rank = rank - 1
  return rank

def binarySearchClosest(arr, value, fromIndex, toIndex):
  if fromIndex < 0:
    fromIndex = 0
  if toIndex >= len(arr):
    toIndex = len(arr) - 1

  if fromIndex >= toIndex:
    return fromIndex

  mid = (fromIndex + toIndex) // 2
  if value > arr[mid]:
    return binarySearchClosest(arr, value, fromIndex, mid - 1)
  if value < arr[mid]:
    return binarySearchClosest(arr, value, mid + 1, toIndex)

  return mid