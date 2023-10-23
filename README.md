# 11th_study

알고리즘 스터디 11주차

[백준 문제집](https://www.acmicpc.net/workbook/view/17173)
[프로그래머스 PCCP 모의고사 1회](https://school.programmers.co.kr/learn/courses/15008/15008-pccp-%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC-1%ED%9A%8C)

# [PCCP 모의고사 #1]

## [1번 - 외톨이 알파벳](https://school.programmers.co.kr/learn/courses/15008/lessons/121683)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./[PCCP%20모의고사%20#1]/1번%20-%20외톨이%20알파벳/민웅.py)

```py
def solution(input_string):
    alpha_dict = {}
    ans = []
    length = len(input_string)
    idx = 0
    while True:
        if idx == length:
            break
        text = input_string[idx]
        temp = idx+1
        while True:
            if temp < length:
                if input_string[temp] == text:
                    temp += 1
                else:
                    break
            else:
                break
        idx = temp-1

        if text in alpha_dict.keys():
            if text not in ans:
                ans.append(text)
        else:
            alpha_dict[text] = 0
        idx += 1
    ans = sorted(ans)
    if ans:
        answer = ''.join(ans)
    else:
        answer = 'N'
    return answer

```

### [병국](./[PCCP%20모의고사%20#1]/1번%20-%20외톨이%20알파벳/병국.py)

```py

```

### [상미](./[PCCP%20모의고사%20#1]/1번%20-%20외톨이%20알파벳/상미.py)

```py

```

### [서희](./[PCCP%20모의고사%20#1]/1번%20-%20외톨이%20알파벳/서희.py)

```py

```

### [성구](./[PCCP%20모의고사%20#1]/1번%20-%20외톨이%20알파벳/성구.py)

```py
from collections import defaultdict

def solution(input_string):
    # 중복 제거하기 위해 set
    answer = set([])
    # 이전 값과 비교하기 위해 0패딩
    input_string= f'0{input_string}'
    # 개수 비교용 dictionary
    alpha = defaultdict(int)
    # 반복으로 떠돌이 문자 찾기
    for i in range(1, len(input_string)):
        # 이전 문자와 같으면 체크 안함
        if input_string[i] != input_string[i-1]:
            alpha[input_string[i]] += 1
        # 만약 2이상이면 추가
            if alpha[input_string[i]] >= 2:
                answer.add(input_string[i])
    # answer가 있다면 순서대로 출력 아니면 N
    return ''.join(sorted(answer)) if answer else 'N'
```

</div>

</details>

<br><br>

## [2번 - 체육대회](https://school.programmers.co.kr/learn/courses/15008/lessons/121684)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./[PCCP%20모의고사%20#1]/2번%20-%20체육대회/민웅.py)

```py
from itertools import permutations

def solution(ability):
    global ans
    answer = 0
    # 종목 수
    l = len(ability[0])
    # 학생 수
    students = len(ability)
    temp_lst = []

    for i in range(students):
        temp_lst.append(i)

    perm = permutations(temp_lst, l)

    for c in perm:
        score = 0
        idx = 0
        for j in range(l):
            score += ability[c[j]][idx]
            idx += 1

        if score > answer:
            answer = score
    return answer

```

### [병국](./[PCCP%20모의고사%20#1]/2번%20-%20체육대회/병국.py)

```py

```

### [상미](./[PCCP%20모의고사%20#1]/2번%20-%20체육대회/상미.py)

```py

```

### [서희](./[PCCP%20모의고사%20#1]/2번%20-%20체육대회/서희.py)

```py

```

### [성구](./[PCCP%20모의고사%20#1]/2번%20-%20체육대회/성구.py)

```py
# 최댓값 저장
maxV = 0

# 전체 순회
def dfs(N, M, ability, j, val, stack):
    global maxV
    # 만약 모든 종목을 탐색했다면
    if j == M:
        # 최대 체크
        maxV = max(maxV, val)
        return

    # 학생 순회
    for x in range(N):
        # 출전한 종목이 없다면
        if not stack[x]:
            # 출전해보고
            stack[x] = 1
            # 점수 확인
            dfs(N, M, ability, j+1, val + ability[x][j], stack)
            # 출전취소
            stack[x] = 0
    return


def solution(ability):
    global maxV
    # 길이를 미리 저장
    N , M = len(ability), len(ability[0])
    # visited
    stack = [0] * N

    dfs(N, M, ability, 0, 0, stack)
    return maxV
```

</div>

</details>

<br><br>

## [4번 - 운영체제](https://school.programmers.co.kr/learn/courses/15008/lessons/121685)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./[PCCP%20모의고사%20#1]/4번%20-%20운영체제/민웅.py)

```py
import heapq
from collections import deque


def solution(program):
    answer = [0]*11
    # [점수, 호출시간, 실행시간]

    program.sort(key=lambda x: [x[1], x[0]])

    q = deque(program)
    t = 0
    hq = []
    while True:
        # 프로그램도 다 호출했고, 실행도 끝났으면 종료
        if not hq and not q:
            break
        # 이전 프로그램 실행종료시간 전까지 호출된 프로그램 다 넣기(우선순위 기준으로 정렬하고 heapq로)
        while q and q[0][1] <= t:
            p = q.popleft()
            heapq.heappush(hq, (p[0], p))

        if hq:
            # 우선순위 제일 높은거로 실행하고 종료
            p = heapq.heappop(hq)[1]
            # 시간 계산
            wait_time = t - p[1]
            answer[p[0]] += wait_time
            t += p[2]
        else:
            t = q[0][1]

    answer[0] = t
    return answer

```

### [병국](./[PCCP%20모의고사%20#1]/4번%20-%20운영체제/병국.py)

```py

```

### [상미](./[PCCP%20모의고사%20#1]/4번%20-%20운영체제/상미.py)

```py

```

### [서희](./[PCCP%20모의고사%20#1]/4번%20-%20운영체제/서희.py)

```py

```

### [성구](./[PCCP%20모의고사%20#1]/4번%20-%20운영체제/성구.py)

```py

```

</div>

</details>

<br><br>

# IF문 좀 대신 써줘

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./IF문%20좀%20대신%20써줘/민웅.py)

```py
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
```

## [병국](./IF문%20좀%20대신%20써줘/병국.py)

```py

```

## [상미](./IF문%20좀%20대신%20써줘/상미.py)

```py

```

## [서희](./IF문%20좀%20대신%20써줘/서희.py)

```py

```

## [성구](./IF문%20좀%20대신%20써줘/성구.py)

```py

```

</div>

</details>

<br><br>

# 전구와 스위치

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./전구와%20스위치/민웅.py)

```py


```

## [병국](./전구와%20스위치/병국.py)

```py

```

## [상미](./전구와%20스위치/상미.py)

```py

```

## [서희](./전구와%20스위치/서희.py)

```py

```

## [성구](./전구와%20스위치/성구.py)

```py

```

</div>

</details>

<br><br>

# 그래프 트리 분할

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./그래프%20트리%20분할/민웅.py)

```py


```

## [병국](./그래프%20트리%20분할/병국.py)

```py

```

## [상미](./그래프%20트리%20분할/상미.py)

```py

```

## [서희](./그래프%20트리%20분할/서희.py)

```py

```

## [성구](./그래프%20트리%20분할/성구.py)

```py

```

</div>

</details>

<br><br>
