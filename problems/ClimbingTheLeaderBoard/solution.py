# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
def climbingLeaderboard(scores, alice):
  ranks = []
  knownRankIndex = None
  for aliceScore in alice:
    if len(scores) == 0 or (len(ranks) > 0 and ranks[len(ranks) - 1] == 1):
      ranks.append(1)
      continue

    if len(ranks) == 0:
      result = findRankFromBeginning(scores, aliceScore)
    else:
      result = findRankFromKnownRank(scores, aliceScore, knownRankIndex, ranks[len(ranks) - 1])
    
    ranks.append(result['rank'])
    knownRankIndex = result['index']

  return ranks

def findRankFromBeginning(scores, aliceScore):
  rank = 1
  i = 0
  while (scores[i] > aliceScore):
    i = i + 1

    if i >= len(scores):
      return {
        'index': len(scores),
        'rank': rank + 1
      }

    if scores[i] != scores[i-1]:
      rank = rank + 1

  return {
    'index': i,
    'rank': rank
  }

def findRankFromKnownRank(scores, aliceScore, knownRankIndex, knownRank):
  i = knownRankIndex
  rank = knownRank

  if i == len(scores):
    i = i - 1
    rank = rank - 1

  if i < 0:
    return {
      'index': 0,
      'rank': 1
    }

  while (scores[i] < aliceScore):
    i = i - 1
    if i < 0:
      return {
        'index': 0,
        'rank': 1
      }

    if scores[i] != scores[i+1]:
      rank = rank - 1
  
  if aliceScore < scores[i]:
    rank = rank + 1
    i = i + 1

  return {
    'index': i,
    'rank': rank
  }

scores = list(map(int, '295 294 291 287 287 285 285 284 283 279 277 274 274 271 270 268 268 268 264 260 259 258 257 255 252 250 244 241 240 237 236 236 231 227 227 227 226 225 224 223 216 212 200 197 196 194 193 189 188 187 183 182 178 177 173 171 169 165 143 140 137 135 133 130 130 130 128 127 122 120 116 114 113 109 106 103 99 92 85 81 69 68 63 63 63 61 57 51 47 46 38 30 28 25 22 15 14 12 6 4'.split()))
alice = list(map(int, '5 5 6 14 19 20 23 25 29 29 30 30 32 37 38 38 38 41 41 44 45 45 47 59 59 62 63 65 67 69 70 72 72 76 79 82 83 90 91 92 93 98 98 100 100 102 103 105 106 107 109 112 115 118 118 121 122 122 123 125 125 125 127 128 131 131 133 134 139 140 141 143 144 144 144 144 147 150 152 155 156 160 164 164 165 165 166 168 169 170 171 172 173 174 174 180 184 187 187 188 194 197 197 197 198 201 202 202 207 208 211 212 212 214 217 219 219 220 220 223 225 227 228 229 229 233 235 235 236 242 242 245 246 252 253 253 257 257 260 261 266 266 268 269 271 271 275 276 281 282 283 284 285 287 289 289 295 296 298 300 300 301 304 306 308 309 3'.split()))
result = climbingLeaderboard(scores, alice)
print(result)