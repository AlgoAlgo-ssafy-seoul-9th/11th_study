# 19637_IF문 좀 대신써줘_please write `if` for me
import sys
input = sys.stdin.readline

def bs(score, power):
    left, right = 0, len(score) - 1
    while left <= right:
        mid = (left + right) // 2
        if score[mid] >= power:
            right = mid - 1
        else:
            left = mid + 1
    return left

N, M = map(int, input().split())
title = []
score = []

for _ in range(N):
    t, s = input().split()
    if score and score[-1] == s:
        continue
    else:
        title.append(t)
        score.append(int(s))

for _ in range(M):
    power = int(input())
    idx = bs(score, power)
    print(title[idx])