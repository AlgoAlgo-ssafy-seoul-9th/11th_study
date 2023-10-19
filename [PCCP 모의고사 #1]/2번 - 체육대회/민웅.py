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