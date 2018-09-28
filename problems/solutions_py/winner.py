# http://codeforces.com/problemset/problem/2/A#
n = int(input())
scoreByName = {}
nameScorePairs = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    total = scoreByName.get(name, 0) + score
    scoreByName[name] = total
    nameScorePairs.append((name, total))

maxScore = 0
for name, score in scoreByName.items():
    if score >= maxScore:
        maxScore = score

for name, score in nameScorePairs:
    if score >= maxScore and scoreByName[name] == maxScore:
        print(name)
        break