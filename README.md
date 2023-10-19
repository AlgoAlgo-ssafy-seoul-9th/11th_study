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

```

</div>

</details>

<br><br>

## [3번 - 유전법칙](https://school.programmers.co.kr/learn/courses/15008/lessons/121685)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./[PCCP%20모의고사%20#1]/2번%20-%20체육대회/민웅.py)

```py

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
